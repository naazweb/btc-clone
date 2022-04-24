import requests

from app.constants import API_KEY


def get_home_page_content():
    inr_url = 'https://rest.coinapi.io/v1/exchangerate/BTC/INR'
    headers = {'X-CoinAPI-Key': API_KEY}
    exchange_rate = {}
    exchange_rate_inr = requests.get(inr_url, headers=headers).json()['rate']
    exchange_rate['inr'] = exchange_rate_inr
    usd_url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    exchange_rate_usd = requests.get(usd_url, headers=headers).json()['rate']
    exchange_rate['usd'] = exchange_rate_usd
    return {'exchange_rate': exchange_rate}


def get_transaction_info(txn_hash):
    # headers = {'X-CoinAPI-Key': API_KEY}

    block = requests.get(
        'https://blockchain.info/rawtx/{}'.format(txn_hash))
    return block.json()


def get_latest_blocks():
    url = "https://blockchain.info/blocks/1650727893387?format=json"
    blocks = requests.get(url).json()
    return blocks
