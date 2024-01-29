import sys
import requests

if len(sys.argv) == 2:
    try:
        coin = float(sys.argv[1])
    except ValueError:
        print("Missing command-line argument")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()

    data = response.json()
    current_bitcoin = float(data["bpi"]["USD"]["rate"].replace(",", ""))

    value = current_bitcoin * coin
    formatted_value = "${:,.4f}".format(value)

    print(formatted_value)

except requests.RequestException:
    sys.exit(1)
