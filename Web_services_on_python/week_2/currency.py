from bs4 import BeautifulSoup
from decimal import Decimal
import requests



def convert(amount, cur_from, cur_to, date, requests):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    response = requests.get(url + date)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, "lxml")
    # print(soup.prettify())
    if cur_from != 'RUR':
        value_from = Decimal(str(soup.find('charcode', text=cur_from).find_next_sibling('value')
                                 .string).replace(',','.'))
        print(value_from)

        if int(soup.find('charcode', text=cur_from).find_next_sibling('nominal').string) != 1:
            value_from /= int(soup.find('charcode', text=cur_from).find_next_sibling('Nominal').string)


        value_to = Decimal(str(soup.find('charcode', text=cur_to).find_next_sibling('value')
                               .string.string).replace(',','.'))

        if int(soup.find('charcode', text=cur_to).find_next_sibling('nominal').string) != 1:
            value_to /= int(soup.find('charcode', text=cur_to).find_next_sibling('nominal').string)

        print(Decimal(value_from), Decimal(value_to))
        result = (value_from  / value_to) * amount
    else:
        value_to = Decimal(str(soup.find('charcode', text=cur_to).find_next_sibling('value')
                               .string.string).replace(',', '.'))

        if int(soup.find('charcode', text=cur_to).find_next_sibling('nominal').string) != 1:
            value_to /= int(soup.find('charcode', text=cur_to).find_next_sibling('nominal').string)

        result = amount / value_to
    return round(result, 4)  # не забыть про округление до 4х знаков после запятой


# print(convert(Decimal("1000.1000"), 'EUR', 'JPY', "17/02/2005", requests))
