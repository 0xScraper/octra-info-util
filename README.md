# Octra explorer info-utility

## Info
**Octra, chads.**

The script is written for entertainment purposes only and is just a regular web scraper for collecting public information from an [open source](https://octrascan.io/).

**Disclaimer:** This is an unofficial utility, and the Octra team bears no responsibility for your use of it.

## For Linux
Requires [Python](https://www.python.org/) v3.10+ and [Git](https://git-scm.com/downloads/linux).
Used third-party Python libs: [requests](https://requests.readthedocs.io/en/latest/), [BeautifulSoup4](https://tedboy.github.io/bs4_doc/), [lxml](https://pypi.org/project/lxml/), [tabulate](https://pypi.org/project/tabulate/).
## 1. Install and Run

Use Pip OR [UV](https://docs.astral.sh/uv/) package managers to install.
### 1.1. UV (Recommended)
1. Install UV package manager if not yet installed (one-time action).
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Clone GitHub repo, go to folder, install dependencies (one-time action).
```sh
git clone https://github.com/0xScraper/octra-info-util.git
cd octra-info-util
uv sync
```
3. Run script from project folder.
```sh
uv run main.py
```
### 1.2. PIP (Standart)
1. Clone GitHub repo, go to folder, create and activate virtual environment (VENV), install dependencies (one-time action).

```sh
git clone https://github.com/0xScraper/octra-info-util.git
cd octra-info-util
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```
2. Run script from project folder.
```sh
source .venv/bin/activate
python3 main.py
```
## 2. CLI usage
![Screen](https://github.com/0xScraper/octra-info-util/blob/main/interface.png)
### Menu items (from top to bottom):
1. Paste octra wallet address and press ENTER for getting address information, such as Type, Non-encrypted balance and amount of txns (nonce).
2. Type 'fau' (without quotation marks) and press ENTER for getting [official faucet](https://faucet.octra.network/) balance.
3. Type 'nfau' (without quotation marks) and press ENTER for getting [non-official](https://oct-faucet.xme.my.id/) faucet balance.
4. Press ENTER for getting current epoch number.
5. Type 'q' (without quotation marks) and press ENTER for Exit the script (or Ctrl-C).

