def backspace_compare(first: str, second: str):
    def edit_string(s):
        res = []
        for char in s:
            if char == '#':
                if res:
                    res.pop()
            else:
                res.append(char)
        return ''.join(res)

    return edit_string(first) == edit_string(second)  


if __name__ == '__main__':
    s1 = "ab#c"
    s2 = "ad#c"
    print(backspace_compare(s1, s2))