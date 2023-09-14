from flask import Flask
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import math

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def fetch_immo_data():
    page = requests.get("https://www.immowelt.de/suche/muenchen/wohnungen/mieten?d=true&sd=DESC&sf=TIMESTAMP&sp=1").content

    Data = {}
    DOMdocument = BeautifulSoup(page, 'lxml')

    for item in DOMdocument.find_all('div', class_="EstateItem-4409d"):
        # print(item.prettify())
        # TODO: add image url
        elems = item.find_all('div', class_="KeyFacts-073db")
        elem = [elem.text for elem in elems][0] # .split('€').split('m')
        price = elem.split('€')[0]
        size = elem[elem.find('€')+1:elem.find('m²')]
        rooms = elem.split('m²')[1]
        price_per_m2 = math.ceil(int(price)/int(size))
        # tenant = [tenant.split('|') for tenant in elem]
        # info = [info for info in tenant] #ok
        # # info2 = " ".join(info[1].split()) #no
        # title = " ".join(info[0][0].split())
        # # city = info[0][1] #no
        # city = 'city'

        # info: {info}
        # title : {title}
        # city : {city}
        print(f'''
        price : {price} €
        size : {size} m²
        rooms : {rooms}
        price per m² : {price_per_m2} €/m²

        ''')

        # title = tenant[0].split(' ').replace(' ', '') #no?

        # title = tenant[0].split(',', 0) #no
        # city = tenant[0].split(',', 1)
        # street = tenant[0].split(',', 3)

        # {tenant[0].split(' ', 0)[0]},
        # price?: {tenant[1]},
        # city:  {tenant[2].split('|')[].replace(' ', '')},
        # attr3: {tenant[2].split(' ', 0)[0]},

        # tenant: {tenant} #.strip()
        # street : {street}
        # title?:
        # [
        #     '(Verfügbar 1-24 Monate) - 1 bedroom flat across from ...Nordbad...2-Zimmer-Wohnung...|...München...Schwabing-West |...Zentnerstr...1680 €...02.01.2024... - 31.07.2024...45 m²...Verifiziertes Unternehmen...Online: 02.08.2023(Verfügbar 1-24 Monate) - 1 bedroom flat across from Nordbad1680 € |45 m² ...2-Zimmer-Wohnung...|...München...Schwabing-West |...Zentnerstr...Verfügbar:...02.01.2024...Diese Anzeige ist erreichbar unter: https://www.wg-gesucht.de/10339155.html',
        #  '(Verfügbar 1-24 Monate) - 1 bedroom flat across from Nordbad...2-Zimmer-Wohnung...|...München...Schwabing-West |...Zentnerstr', '1680 €...02.01.2024...- 31.07.2024...45 m²',
        #    'Verifiziertes...Online: 02.08.2023', 'Verifiziertes Unternehmen', 'Online: 02.08.2023']

        # attr1: attr1: Schickes Apartment mit Balkon zur Miete ...Wohnen im Szeneviertelab ...1560 € ...sofort frei - auch monatsweise oder für kurze Zeit ...Beispielanzeige von Spacest*Anzeige,
        # attr2: (Verfügbar 1-24 Monate) - Charmante & stilvolle  2 Zimmer Wohnung - Gehobene Ausstattung (München) 3-Zimmer-Wohnung | München Berg am Laim | Kreillerstraße,
        # attr3: 1350 € 01.08.2023 - 30.06.2024 35 m²,

    # for item in DOMdocument.find_all('div', class_="col-sm-12 flex_space_between"):
    #     h3s = item.find_all('h3', class_="truncate_title")
    #     name = [name.text.strip() for name in h3s]
    #     print(f'''
    #     Wohnung: {name},
    #     ''')

    # for item in DOMdocument.find_all('div', class_="col-xs-11"):
    #     address = item.find('span').text.split('|')[2].replace('\n', '')
    #     print(f'''
    #     Stadt:  {address}
    #     ''')

    # for item in DOMdocument.find_all('div', class_="row noprint middle"):
    #     rent = item.find('b').text
    #     m2 = item.find('div', class_="col-xs-3 text-right").b.text
    #     per_sqr_mtr = math.ceil(int(rent.replace('€', ''))/int(m2.replace('m²', '')))
    #     print(f'''
    #     Miete: {rent}, {m2}, {per_sqr_mtr}/m²
    #     ''')


    # print(Data['title'])

    # city_tags = DOMdocument.find_all('div', id="liste-details-ad-10477566")
    # # cities_links = [url + tag["href"] for tag in city_tags]
    # # cities_links = [tag["href"] for tag in city_tags]
    # print(DOMdocument.prettify)

    return Data

if __name__ == '__main__':
    fetch_immo_data()
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5001)
