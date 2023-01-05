from bs4 import BeautifulSoup
import requests
from flask import Flask

app = Flask(__name__)


def get_data():
    response = requests.get("https://www.sharesansar.com/today-share-price")
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    price_data = []
    del rows[0]
    for row in rows:
        data = row.find_all("td")
        company_name = data[1].text.strip()
        company_close = data[6].text
        price_data.append({"companyName": company_name, "closingPrice": company_close})

    return price_data


def get_all_data():
    response = requests.get("https://www.sharesansar.com/today-share-price")
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    price_data = []
    del rows[0]
    for row in rows:
        data = row.find_all("td")
        price_data.append({"companyName": data[1].text.strip(),
                           "stockConfidence": data[2].text.strip(),
                           "openingPrice": data[3].text.strip(),
                           "highestPrice": data[4].text.strip(),
                           "lowestPrice": data[5].text.strip(),
                           "closingPrice": data[6].text.strip(),
                           "volumeWeightedAveragePrice": data[7].text.strip(),
                           "volume": data[8].text.strip(),
                           "previousClose": data[9].text.strip(),
                           "turnover": data[10].text.strip(),
                           "transactions": data[11].text.strip(),
                           "difference": data[12].text.strip()
                           })
    return price_data


@app.route("/")
def index():
    return get_data()


@app.route("/all")
def all():
    return get_all_data()


if __name__ == "__main__":
    app.run(debug=False, port=8080)

