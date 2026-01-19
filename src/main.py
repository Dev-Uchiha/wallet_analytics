import requests


def get_bitcoin_height():
    url = "https://blockchain.info/q/getblockcount"
    resp = requests.get(url)
    return resp.text


def main():
    print("Current Bitcoin block height:", get_bitcoin_height())


def test():
    print("hello")


if __name__ == "__main__":
    main()
