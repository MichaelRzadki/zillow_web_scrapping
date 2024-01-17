import requests
from bs4 import BeautifulSoup
import json
import time
import csv

class CondoScraper():
    results = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding':'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control':'no-cache',
        #'cookie': 'zguid=24|%249aafe715-aa0e-4aea-a414-424f699a1052; zgsession=1|37f7e003-d613-4ca0-870c-94ddb2dec1fa; zjs_anonymous_id=%229aafe715-aa0e-4aea-a414-424f699a1052%22; zjs_user_id=null; zg_anonymous_id=%2235502394-af6f-416a-b157-8e9b9485c1cd%22; _ga=GA1.2.537440393.1705011702; _gid=GA1.2.977148507.1705011702; pxcts=cc678db7-b0cf-11ee-85d3-237eaaf332a8; _pxvid=cc6779ba-b0cf-11ee-85d2-7d179b25f72c; _gcl_au=1.1.1857370131.1705011704; DoubleClickSession=true; __pdst=83260003b8774c6fb93e351ec7c5d12b; _pin_unauth=dWlkPU16azJPVGRoWmpJdFl6RTVOaTAwWVdJeUxUaGpOREl0TlRJeFlqYzJORFl3TlRGaA; g_state={"i_p":1705165501349,"i_l":2}; FSsampler=1449519208; _clck=1vol6lt%7C2%7Cfid%7C0%7C1471; JSESSIONID=D57D907C1E9C27D260EC2295A09B9AAE; AWSALB=Q9IVnKNshglem2YybdqWSfE4KfpDD1SpQhlMg+XNoTueP8xkZUbRKtHYjSdVSSOAn3kegZgOnBgrMeuIs5It2Ahwn3KGA4+V+ecD1ejUAOA2O4V5bQZluBvJvU1V; AWSALBCORS=Q9IVnKNshglem2YybdqWSfE4KfpDD1SpQhlMg+XNoTueP8xkZUbRKtHYjSdVSSOAn3kegZgOnBgrMeuIs5It2Ahwn3KGA4+V+ecD1ejUAOA2O4V5bQZluBvJvU1V; _px3=e73cc53967b0d00c62c89092ed9ce08887f9e46744b6b555e82fa990939d67d4:kvu4Lw+/tPAo5alcMA/UJbR02A+gRN5WLFKn2mN7FBRNl94jhav9fXKDNlA0EaipoC/nnLtGkR/r2RZK94UNTw==:1000:++79l4+9yl0fn1pBnEnEV/naTMd98rucvxKTNazepLBEu0VOWOXY24g0f+kpvZW65AjOOxCAnBJMV3zQ6tD3gX7AjOHMesEgfm0qh6MC4WeqpckLSxqloHjZyVvljPnwMkZVljvEQys4Yg+ebjmUuReWW5vh25DuC4Zl6l2hEHrInKfe33z4JTPi8u5BK30Hn9mh5t6dvyMI8DzkianqYXduV5nLmoULCf1Ee5eOdAU=; _uetsid=cd870600b0cf11eeb2d1dfa6dbb8bcd0; _uetvid=cd874450b0cf11eebfed891b06f78875; _derived_epik=dj0yJnU9ZGV4QkVEc3JhcHRaTG92encwMHJIR2VHRVZnQjJ0ZFUmbj1zY2hHM21lZmt4dm1zSVF5ZkZvWDFRJm09ZiZ0PUFBQUFBR1dpRG1VJnJtPWYmcnQ9QUFBQUFHV2lEbVUmc3A9Mg; _gat=1; search=6|1707711405086%7Crect%3D33.140489278154114%2C-96.23772813085938%2C32.49418982375236%2C-97.31713486914063%26rid%3D38128%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D0%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0938128%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _clsk=ogqu32%7C1705119405126%7C29%7C0%7Cq.clarity.ms%2Fcollect',
        'pragma':'no-cache',
        'referer':'https://www.google.com/',
        'sec-ch-ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'same-origin',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    def get_data(self, url, params):
        page = requests.get(url, headers = self.headers, params= params)
        return page
    
    def parse_data(self, page):
        #content = BeautifulSoup(page.content, "html.parser")
        content = BeautifulSoup(page, 'lxml')
        listings = content.find('ul', {'class': 'List-c11n-8-84-3__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 doa-doM fgiidE photo-cards photo-cards_extra-attribution'})
        if listings is None:
            listings = content.find('ul', {'class': 'List-c11n-8-84-3__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 doa-doM fgiidE photo-cards'})
        
        #Obtain all child elemements
        for listing in listings.contents:
            script = listing.find('script', {'type': 'application/ld+json'})
            if script:
                script_json = json.loads(script.contents[0])

                #Collect Main Page Data
                if 'name' in script_json:
                    name = None
                    name = script_json['name']
                else:
                    name = None
                
                if 'addressLocality' in script_json['address']:
                    city = None
                    city  = script_json['address']['addressLocality']
                else:
                    city = None
                
                if 'addressRegion' in script_json['address']:
                    state = script_json['address']['addressRegion']
                else: 
                    state = None
                
                if 'postalCode' in script_json['address']:
                    postalcode = script_json['address']['postalCode']
                else:
                    postalcode = None
                
                if 'latitude' in script_json['geo']:
                    latitude = script_json['geo']['latitude']
                else:
                    latitude = None

                if 'longitude' in script_json['geo']:
                    longitude = script_json['geo']['longitude']
                else:
                    longitude = None
                
                if 'value' in script_json['floorSize']:
                    floorsize = script_json['floorSize']['value']
                else:
                    floorsize = None
                
                if listing.find('div', {'class': 'PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 kSsByo'}).text is not None:
                    price = listing.find('div', {'class': 'PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 kSsByo'}).text
                else:
                    price = None
                
                if listing.find('ul', {'class': 'StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 eYPFID'}).text is not None:
                    rooms = listing.find('ul', {'class': 'StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 eYPFID'}).text
                else:
                    rooms = None
                
                if listing.find('div', {'class': 'StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 dbDWjx'}).text is not None:
                    home_type = listing.find('div', {'class': 'StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 dbDWjx'}).text.split('-', 1)[1].strip(','), 
                else:
                    home_type = None

                if 'url' in script_json:
                    url_details = script_json['url']
                    
                    #Additional home details on second page
                    additional_info = requests.get(url_details, headers= self.headers).text
                    content_2 = BeautifulSoup(additional_info, 'lxml')

                    if content_2.find('div', {'class': 'Spacer-c11n-8-84-3__sc-17suqs2-0 dqTzbQ'}) is not None:

                        perks = content_2.find('div', {'class': 'Spacer-c11n-8-84-3__sc-17suqs2-0 dqTzbQ'}).text
                    else:
                        perks = None

                    if content_2.find('div', {'class': 'Spacer-c11n-8-84-3__sc-17suqs2-0 jzqFVI'}) is not None:

                        listing_overview = content_2.find('div', {'class': 'Spacer-c11n-8-84-3__sc-17suqs2-0 jzqFVI'}).text
                    else:
                        listing_overview = None
                    
                    if content_2.find('dl', {'class': 'OverviewStatsComponentsstyles__StyledOverviewStats-sc-1bg6b6d-0 nnBbc'}) is not None:
                        traffic = content_2.find('dl', {'class': 'OverviewStatsComponentsstyles__StyledOverviewStats-sc-1bg6b6d-0 nnBbc'}).text
                    else:
                        traffic = None
                    
                    building_info = content_2.find_all('ul', {'class': 'List-c11n-8-84-3__sc-1smrmqp-0 styles__StyledFactCategoryFactsList-sc-1i5yjpk-1 dQcvzF gpBiYn'})
                    building_stats = []
                    
                    for item in building_info:
                        
                        building_stats.append(item.text)
                        
                else:
                    url_details = None                 
                    
                        
                #Place data in results
                self.results.append({
                    'Name': name,
                    'City': city,
                    'State': state,
                    'Postal Code': postalcode,
                    'Latitude': latitude, 
                    'Longitude': longitude,
                    'Floorsize': floorsize,
                    'Url': url_details, 
                    'Price': price,
                    'Rooms' : rooms,
                    'Home Type': home_type,
                    'Perks' : perks,
                    'Listing Overview' : listing_overview,
                    'Website Traffic' : traffic,
                    'Building Stats' : building_stats,
                })
                
    def to_csv(self):
        with open('for_sale_data.csv', 'w', newline='', encoding = 'utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = self.results[0].keys())
            writer.writeheader()

            for row in self.results:
                if row:
                    writer.writerow(row)

    def run_scraper(self):
        url = "https://www.zillow.com/dallas-tx/fsbo/"
        

        for page in range(1,21):
            print('PAGE:', page)
            params = {
            'searchQueryState': '{"pagination":{"currentPage": %s},"isMapVisible":false,"mapBounds":{"west":-97.31713486914063,"east":-96.23772813085938,"south":32.49418982375236,"north":33.140489278154114},"regionSelection":[{"regionId":38128,"regionType":6}],"filterState":{"sort":{"value":"globalrelevanceex"}},"isListVisible":true}' %page    
            }
            data = self.get_data(url, params)
            self.parse_data(data.text)
            time.sleep(2)



if __name__ == '__main__':
    scraper = CondoScraper()
    scraper.run_scraper()
    scraper.to_csv()

