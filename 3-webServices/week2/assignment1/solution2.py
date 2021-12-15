import os
import re
from bs4 import BeautifulSoup


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

    lks = body.find_all("a")
    for lk in lks:
        local_mx = 1
        for tag in lk.find_next_siblings():
            if tag.name == "a":
                local_mx += 1
            else:
                break
        linkslen = max(linkslen, local_mx)

    potential_lists = body.find_all(["ul", "ol"])
    for lst in potential_lists:
        if not lst.find_parents(["ul", "ol"]):
            lists += 1

    return [imgs, headers, linkslen, lists]


def get_links(path, page):

    with open(os.path.join(path, page), encoding="utf-8") as file:
        links = set(re.findall(r"(?<=/wiki/)[\w()]+", file.read()))
        if page in links:
            links.remove(page)
    return links


def get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks):
    """возвращает словарь обратных ссылок (ключ - страница, значение - страница
    с которой возможен переход по ссылке на страницу, указанную в ключе)"""

    if end_page in checked_pages or not checked_pages:
        return backlinks

    new_checked_pages = set()

    for checked_page in checked_pages:
        # unchecked_pages.remove(checked_page)
        linked_pages = get_links(path, checked_page) & unchecked_pages

        for linked_page in linked_pages:
            backlinks[linked_page] = backlinks.get(linked_page, checked_page)
            new_checked_pages.add(linked_page)

    # checked_pages = new_checked_pages & unchecked_pages
    checked_pages = new_checked_pages

    return get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks)


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    backlinks = get_backlinks(
        path,
        end_page,
        set(os.listdir(path)),
        {
            start_page,
        },
        dict(),
    )

    current_page, bridge = end_page, [end_page]

    while current_page != start_page:
        current_page = backlinks.get(current_page)
        bridge.append(current_page)

    return bridge[::-1]


def get_statistics(path, start_page, end_page):

    pages = build_bridge(path, start_page, end_page)
    statistic = {}

    for page in pages:
        statistic[page] = parse(os.path.join(path, page))

    return statistic
