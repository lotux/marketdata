from polygon import RESTClient


def main():
    key = "AuTxXLAoTV3haQekGxEnnDNkpy1I5b1j"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_snapshot_all_tickers()
        print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()
