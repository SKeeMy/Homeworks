from bs4 import BeautifulSoup
from typing import Optional, Dict, List
from datetime import datetime
from decimal import Decimal
import requests
import aiohttp
import asyncio


def get_exchange_rate() -> Decimal:
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    usd = soup.find("CharCode", text="USD").find_next_sibling(
        "Value").string.replace(",", ".")
    return Decimal(usd)


async def get_html(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def get_data_from_page(session: aiohttp.ClientSession, url: str) -> Dict:
    html = await get_html(session, url)
    soup = BeautifulSoup(html, "html.parser")

    code = soup.find(
        "span", {"class": "price-section__category"}).text.split()[-1]
    name = soup.find("h1", {"class": "title"}).text.strip()

    raw_price = soup.find(
        "span", {"class": "price-section__current-value"}).text
    price = Decimal(raw_price.replace(",", ""))

    raw_pe = soup.find("div", {"class": "snapshot__data-item snapshot__data-item--small"}).find("span", {
        "class": "snapshot__data-value"}).text
    pe = Decimal("".join([c for c in raw_pe if c.isdigit() or c == "."]))

    raw_growth = soup.find("td", {"class": "snapshot__td snapshot__td--big-number"}).find("span", {
        "class": "snapshot__value"}).text
    sign = 1 if "▲" in raw_growth else -1
    growth = sign * \
        Decimal("".join([c for c in raw_growth if c.isdigit() or c == "."]))

    min_price, max_price = Decimal("inf"), Decimal("-inf")
    min_date, max_date = None, None
    graph_data = soup.find_all("span", {"class": "charts-data-block__cell"})
    data_len = len(graph_data)
    for i, data in enumerate(graph_data):
        if i % 2 == 0:
            date = datetime.strptime(data.text, "%b %d, %Y")
            min_price = min(price, min_price)
            if price > max_price:
                max_price = price
                max_date = date
            if date == datetime.strptime(graph_data[3].text, "%b %d, %Y"):
                min_date = date
        else:
            price = Decimal(data.text.replace(",", ""))

    exchange_rate = get_exchange_rate()
    min_price *= exchange_rate
    max_price *= exchange_rate

    potential_profit = (max_price - min_price) / min_price * Decimal("100")

    return {
        "code": code,
        "name": name,
        "price": price,
        "pe": pe,
        "growth": growth,
        "min_price": min_price,
        "max_price": max_price,
        "min_date": min_date,
        "max_date": max_date,
        "potential_profit": potential_profit
    }


async def parse_data(session: aiohttp.ClientSession, urls: List[str]) -> List[Dict]:
    parsed_data = []
    for url in urls:
        try:
            data = await get_data_from_page(session, url)
            parsed_data.append(data)
        except Exception as e:
            print(f"Error occurred while parsing page: {url}\n{e}")
    return parsed_data


async def generate_report(data: List[Dict], file_path: str, key: str, reversed: Optional[bool] = False):
    data_sorted = sorted(data, key=lambda x: x[key], reverse=reversed)
    json_data = data_sorted[:10]
    with open(file_path, "w") as f:
        f.write(str(json_data))
    print(f"Report generated at: {file_path}")


async def start():
    url = "https://markets.businessinsider.com/index/components/s&p_500"
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, url)
        soup = BeautifulSoup(html, "html.parser")

        urls = []
        for row in soup.find_all("tr", {"class": "table__row"}):
            try:
                url = row.find("a", {"class": "link"}).get("href")
                urls.append(f"https://markets.businessinsider.com{url}")
            except:
                pass

        tasks = [parse_data(session, urls[i:i + 25])
                 for i in range(0, len(urls), 25)]
        results = await asyncio.gather(*tasks)

        data = []
        for result in results:
            data.extend(result)

        await generate_report(data, "top_10_most_expensive_companies.json", "price", reversed=True)
        await generate_report(data, "top_10_lowest_PE_companies.json", "pe")
        await generate_report(data, "top_10_highest_growth_companies.json", "growth", reversed=True)
        await generate_report(data, "top_10_highest_potential_profit_companies.json", "potential_profit", reversed=True)


if __name__ == "__main__":
    asyncio.run(start())
