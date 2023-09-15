from flask import Flask
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import math
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/data", methods=['GET'])
def fetch_immo_data():
    page = requests.get("https://www.immowelt.de/suche/muenchen/wohnungen/mieten?d=true&sd=DESC&sf=TIMESTAMP&sp=1").content

    Data = []
    DOMdocument = BeautifulSoup(page, 'lxml')

    for item in DOMdocument.find_all('div', class_="EstateItem-4409d"):
        title = [title.text.strip() for title in item.find_all('h2')][0]
        location = [location.text.strip() for location in item.find_all('span')[1]][0]

        elems = item.find_all('div', class_="KeyFacts-073db")
        elem = [elem.text for elem in elems][0]
        price = elem.split('€')[0].replace(' ', '')
        without_dot = price.replace('.', '')
        int_price = math.floor(int(float(without_dot.replace(',', ''))))
        size = elem[elem.find('€')+1:elem.find('m²')].replace(' ', '')
        int_size = math.floor(int(float(size)))
        rooms = elem.split('m²')[1]
        price_per_m2 = math.floor(int_price/int_size)

        # TODO: get image_src(href)
        # print('img_src: ' + [img_src.text for img_src in item.find_all('img', class_="cover-bc87c loadedClass-6b527")])

        Data.append({
            'title': title,
            'location': location,
            'price': price,
            'size': size,
            'rooms': rooms,
            'price_per_m2': price_per_m2
        })

        json_string = json.dumps(Data, default=list)

    return json_string

if __name__ == '__main__':
    fetch_immo_data()
    app.run(debug=True, host="127.0.0.1", port=5000)
