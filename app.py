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


@app.route("/")
def index():
    return get_data()


app.run()

