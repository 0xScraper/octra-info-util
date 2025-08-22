#!/usr/bin/env python3
# ruff: noqa: I001
import sys

from tabulate import tabulate

from stats import status
from const import USER_INTERFACE, FAIR_LENGTH_ADDR, URLS

def main() -> None:

    print(tabulate(USER_INTERFACE, tablefmt='fancy_grid', colalign=('center', 'center')))
    try:
        user_input: str | None = input('>>> ').strip()

        if user_input:
            if user_input.startswith('oct') and len(user_input) == FAIR_LENGTH_ADDR:
                url1: str = URLS.get('addr') + user_input
                status(url1, flag=True)
            elif user_input.lower() == 'q':
                sys.exit()
            elif user_input.lower() == 'fau':
                url2: str = URLS.get('addr') + URLS.get('faucet')
                status(url2, flag=True)
            elif user_input.lower() == 'nfau':
                url3: str = URLS.get('addr') + URLS.get('nfaucet')
                status(url3, flag=True)
        else:
            url4: str = URLS.get('epoch')
            status(url4, flag=False)
    except KeyboardInterrupt:
        print('\tExit script')
        sys.exit()

    main()


if __name__=='__main__':
    main()
