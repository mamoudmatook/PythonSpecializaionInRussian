import re
from bs4 import BeautifulSoup
import unittest


def parse(path_to_file):
    imgs = headers = linkslen = lists = 0
    soup = None
    with open(path_to_file, "r", encoding="utf-8") as html:
        soup = BeautifulSoup(html, "lxml")

    body = soup.find(id="bodyContent")
    imgs = len((body.find_all("img", width=lambda x: int(x or 0) > 199)))
    headers = len(
        [
            i.text
            for i in body.find_all(name=re.compile(r"[hH1-6]{2}"))
            if i.text[0] in "ETC"
        ]
    )
    # current_a = body.find_next("a")
    # while current_a:
    #     local_mx = 1
    #     for next_a in current_a.find_next_siblings():
    #         if next_a.name == "a":
    #             local_mx += 1
    #         else:
    #             break
    #     linkslen = max(local_mx, linkslen)
    #     current_a = current_a.find_next("a")

    lks = body.find_all('a')
    for lk in lks:
        local_mx = 1
        for tag in lk.find_next_siblings():
            if tag.name == 'a':
                local_mx += 1
            else:
                break
        linkslen = max(linkslen, local_mx)

    potential_lists = body.find_all(["ul", "ol"])
    for lst in potential_lists:
        if not lst.find_parents(["ul", "ol"]):
            lists += 1

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ("wiki/Stone_Age", [13, 10, 12, 40]),
            ("wiki/Brain", [19, 5, 25, 11]),
            ("wiki/Artificial_intelligence", [8, 19, 13, 198]),
            ("wiki/Python_(programming_language)", [2, 5, 17, 41]),
            ("wiki/Spectrogram", [1, 2, 4, 7]),
        )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == "__main__":
    unittest.main()
