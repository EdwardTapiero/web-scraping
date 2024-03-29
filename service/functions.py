import threading

import requests
from bs4 import BeautifulSoup
from lxml import html

from core.const import URL_MELI, USER_AGENT
from repository.script import insert_product, delete_table, count_by_brand, max_pag

headers = {
    "user-agent": USER_AGENT
}

url_page = URL_MELI


def verify_reset(reset, pag, brand):
    if reset is True:
        return __find_page(pag, brand)
    else:
        return __find_data(brand)


def __find_page(pag, brand):
    delete_table()

    global products, url_page
    while True:

        response_page = requests.get(url_page, headers=headers)

        if response_page.status_code == 200:

            soup = BeautifulSoup(response_page.content, 'html.parser')
            dom_page = html.fromstring(response_page.content)
            products = soup.find_all('a', attrs={"class": "ui-search-item__group__element shops__items-group-details ui-search-link"})

            ini = soup.find('span', attrs={"class": "andes-pagination__link"}).text
            ini = int(ini)

            __insert_data(ini)
        else:
            break

        if pag == ini:
            break

        url_page = dom_page.xpath('//div[contains(@class, "ui-search-pagination")]/ul/li[contains(@class,"--next")]/a')[0].get(
            'href')

    return count_by_brand(brand), max_pag()


def __insert_data(ini):
    for product in products:
        marca, memoria_int, memoria_ram, modelo, precio, ref = __find_items(product)
        insert_product(str(marca), str(ref), str(modelo), str(memoria_int), str(memoria_ram), str(precio), str(ini))


def __find_items(product):
    url = product['href']
    item = requests.get(url, headers=headers)
    print(url)
    dom = html.fromstring(item.content)

    marca = dom.xpath('//tr[@class="andes-table__row ui-vpp-striped-specs__row"]/th[text()="Marca"]/following-sibling::td/span/text()')
    ref = dom.xpath('//tr[@class="andes-table__row ui-vpp-striped-specs__row"]/th[text()="Línea"]/following-sibling::td/span/text()')
    modelo = dom.xpath('//tr[@class="andes-table__row ui-vpp-striped-specs__row"]/th[text()="Modelo"]/following-sibling::td/span/text()')
    memoria_int = dom.xpath('//tr[@class="andes-table__row ui-vpp-striped-specs__row"]/th[text()="Memoria interna"]/following-sibling::td/span/text()')
    memoria_ram = dom.xpath('//tr[@class="andes-table__row ui-vpp-striped-specs__row"]/th[text()="Memoria RAM"]/following-sibling::td/span/text()')
    precio = dom.xpath('//div[@class="ui-pdp-price__second-line"]/span/span[@class="andes-money-amount__fraction"]/text()')

    ref = 'null' if len(ref) == 0 else ref[0]
    marca = 'null' if len(marca) == 0 else marca[0]
    modelo = 'null' if len(modelo) == 0 else modelo[0]
    memoria_int = 'null' if len(memoria_int) == 0 else memoria_int[0]
    memoria_ram = 'null' if len(memoria_ram) == 0 else memoria_ram[0]
    precio = 'null' if len(precio) == 0 else precio[0]

    event = threading.Event()
    event.wait(2)
    return marca, memoria_int, memoria_ram, modelo, precio, ref


def __find_data(marca):
    return count_by_brand(marca), max_pag()