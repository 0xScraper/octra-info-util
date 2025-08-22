# ruff: noqa: I001
import os

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

from timing import get_time
from const import CMD, STATUS_OK, HEADERS

def clear_screen() -> None:
    os.system(CMD[0]) if os.name == 'posix' else os.system(CMD[1]) # noqa: S605


@get_time
def status(url: str, *, flag: bool) -> None:
    clear_screen()
    resp: requests.Response = requests.get(url=url, headers=HEADERS, timeout=25)

    if resp.status_code == STATUS_OK:
        content: str = resp.text
        soup: BeautifulSoup = BeautifulSoup(content, 'lxml')
        try:
            mono = soup.find_all('div', class_='mono')
            param1 = mono[0]
            if flag:
                param2, param3 = mono[1], mono[2]
                data: list[tuple[str]] = [
                    ('WALLET', param1.text),
                    ('BALANCE', param2.text),
                    ('NONCE', param3.text),
                ]
                table: str = tabulate(data, tablefmt='fancy_grid', colalign=('right', 'left'), missingval = 'N/A')
                print(table)
            else:
                print(tabulate([['EPOCH', param1.text], ], tablefmt='fancy_grid', colalign=('center', 'center'))) #noqa: COM819
        except IndexError as e:
            print(f'!!!!! Failed: {e}. \n!!!!! ERROR on the web-page !!!!!')
    else:
        print(f'!!!!!! FAILED! Status {resp.status_code} !!!!!!')
