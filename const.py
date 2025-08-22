USER_INTERFACE: list[tuple[str]] = [
    ('oct...', 'wallet info'),
    ('fau', 'official faucet balance'),
    ('nfau', 'non-official faucet balance'),
    ('<ENTER>', 'Epoch #'),
    ('q', 'Exit'),
]
CMD: tuple[str, str] = ('clear', 'cls')
STATUS_OK: int = 200
FAIR_LENGTH_ADDR: int = 47
URLS: dict[str, str] = {
    'addr': 'https://octrascan.io/addr/',
    'epoch': 'https://octrascan.io/validators',
    'faucet': 'oct3SSKjCGK8pVxPHH1Y6LZEVqm94rZn3StXHt31AD1UUVN',
    'nfaucet': 'octAuNz35Tc3BfGurox4c82aZMLN3RvXDJ1T9HVTwqK7et1',
}
HEADERS: dict[str, str] = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0',
}
