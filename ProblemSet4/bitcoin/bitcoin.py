import requests, sys, json

def main():
    quantity = float(sys.argv[1])
    try:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoinResponse = bitcoin.json()
        finalPrice = bitcoinResponse['bpi']['USD']['rate_float'] * quantity
        print(f"${finalPrice:,.4f}")
    except requests.RequestException:
        sys.exit("Error")

if __name__ == "__main__":
    main()