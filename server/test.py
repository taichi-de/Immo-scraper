url = "https://www.immobilienscout24.de/Suche/de/wohnung-mieten?sorting=2#"

jsonData = requests.get(url).json()
return jsonData

# url = "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?enteredFrom=one_step_search"

# soup = BeautifulSoup(requests.get(url).content, 'html.parser')

# data = []
# for h5 in soup.select('h5'):
#     print(h5.get_text(strip=True, separator=' '))
#     data.append(h5.get_text(strip=True, separator=' '))
return jsonData

headers= {
'content-type': 'application/json',
'x-requested-with': 'XMLHttpRequest'
}

print(f'''
        'title': {title},
        'address': {address},
        'cost': {cost},
        'size': {size}

        ''')

# results.append({
        #     'title': title,
        #     'address': address,
        #     'cost': cost,
        #     'size': size
        # })

    # Data['title'] = DOMdocument.title.string



        # <h3 class="truncate_title noprint" title="BEFRISTET bis 30.09-13.10 ;  LIMITED 30.09.-13.10. 2 weeks! 1,5 Zimmer Wohnung Schwabing 30 qm">
        # <a href="/wohnungen-in-Muenchen-Schwabing-Freimann.7718282.html">
        #                             BEFRISTET bis 30.09-13.10 ;  LIMITED 30.09.-13.10. 2 weeks! 1,5 Zimmer Wohnung Schwabing 30 qm
        #                         </a>
        # </h3>
        # <div class="asset_favourite cursor-pointer" data-ad_id="7718282" data-ad_type="0" data-favourite_status="0">
        # <span aria-hidden="true" class="fav-button-7718282 mdi mdi-heart-outline icon-fav-empty" id="to-fav-7718282"></span>
        # </div>
        # </div>, <div class="col-sm-12 flex_space_between">
        # </div>, <div class="col-sm-12 flex_space_between">
        # <span class="ml5">Marcel H.</span>

                # print(card.prettify())
                   # print(card.div.span.split()[-1])


    # for h3 in DOMdocument.select('h3'):
    #     print('h3: ' + h3.get_text(strip=True, separator=' '))
    # for link in DOMdocument.find('div').find_all('a'):
    #     print('link: ' + link["href"])
    #     # Data['links'] = link["href"]
    # print(DOMdocument.find_all('div').select('a').text)
    # print(DOMdocument.find('div', class_="col-sm-4 card_image").select_one('a')["href"])
    # print("Adress: " + DOMdocument.find('div', id_="liste-details-ad-10485859").select('div', class_="col-xs-11").select('span').split('|')[2])
    # print("Adress: " + DOMdocument.find('div', id="liste-details-ad-10485859"))

        Title: {title},
        Image_link: {link},
        Area: {area},
        Miete: {rent}

string = '-'.join(list_string)

  for item in DOMdocument.find_all('div', class_="wgg_card"): #col-sm-4 card_image
        txt = item.find_all('div', class_="row")

# print(elem.prettify().replace('\n', ',')[0] for elem in txt)
        # elem = [elem.prettify() for elem in txt]
        # title = elem[0]
        # area = elem[1]
        # # address = elem[1]
        # rent = elem[2]
        # m2 = elem[3]
        # per_sqr_mtr = math.ceil(int(rent.replace('€', ''))/int(m2.replace('m²', '')))

        # link = [link.text.strip().replace('\n', '').split(' ')[0] for link in txt]