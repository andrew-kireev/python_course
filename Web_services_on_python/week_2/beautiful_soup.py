from bs4 import BeautifulSoup
import unittest
import re

def parse(path_to_file):
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    f = open(path_to_file, 'r', encoding='utf-8')
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find(id="bodyContent")
    imgs = 0
    for img in body.find_all('img', width=True):
        if int(img['width']) >= 200:
            imgs += 1

    headers = 0
    for head in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for header in body.find_all(head):
            if re.match(r'\b[E,T,C]', header.text) is not None:
                headers += 1

    linkslen = 0
    for a in body.find_all('a'):
        siblings = a.find_next_siblings()
        len_a = 1
        for next_ in siblings:
            if next_.name == 'a':
                len_a += 1
            else:
                break
        if len_a > linkslen:
            linkslen = len_a

    lists = 0
    for ul in body.find_all('ul'):
        if ul.parent.name == 'div':
            lists += 1
    for ol in body.find_all('ol'):
        if ol.parent.name == 'div':
            lists += 1
    lists = 0
    html_lists = body.find_all(['ul', 'ol'])
    for html_list in html_lists:
        if not html_list.find_parents(['ul', 'ol']):
            lists += 1

    print(lists)
    f.close()
    return [imgs, headers, linkslen, lists]

class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
    parse('wiki/Stone_Age')
