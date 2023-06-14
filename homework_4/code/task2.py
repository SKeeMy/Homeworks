import requests


def count_dots_on_i(url: str) -> int:
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        return html.count("i")
    except (requests.exceptions.RequestException, ValueError):
        raise ValueError(f"Unreachable {url}")
