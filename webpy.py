from bs4 import BeautifulSoup
import requests
import json
import secrets # file that contains your API key

#response = requests.get('http://visadoor.com/h1b/index?company=HITHINK&job=Business+Intelligence+Analyst&state=&year=2020&submit=Search')   
response = requests.get('http://visadoor.com/h1b/index?company=DELOITTE+CONSULTING+LLP&job=Specialist+Senior&state=&year=2020&submit=Search')   
soup = BeautifulSoup(response.text)
s = {}
a = soup.find('table',class_ = 'table table-bordered table-striped table-hover')
l = a.find_all('tr')
r = l[1].find_all('td')
s["time"] = r[1].text
s["status"] = r[3].text
s["salary"] = r[-1].text
li = []
li.append(s)
li.append(s)


with open('demo1.json', mode='w', encoding='utf-8') as f:
    json.dump(li, f)

def load_cache():
    with open('demo1.json', mode='r', encoding='utf-8') as f:
        dicts = json.load(f)
        rr = []
        for i in dicts:
            rr.append(i)
    return rr
    
    
def save_cache(li):
    with open('demo1.json', mode='w', encoding='utf-8') as f:
        json.dump(li, f)
    
def record(soup):
    try:
        s = {}
        a = soup.find('table',class_ = 'table table-bordered table-striped table-hover')
        l = a.find_all('tr')
        r = l[1].find_all('td')
        s['time'] = r[1].text
        s['status'] = r[3].text
        s['salary'] = r[-1].text
        cache_file = load_cache()
        if s in cache_file:
            print('caching')
            return s
        else:
            print('feching')
            cache_file.append(s)
            save_cache(cache_file)
            return s
    except:
        return 'false'












'''
    def __init__(self, national_site = ''):
        #state_url = national_site
        #response = requests.get(state_url)
        #soup = BeautifulSoup(response.text, 'html.parser')
        
        
        state_page_url = national_site
        url_text = make_url_request_using_cache(state_page_url, CACHE_DICT)
        soup = BeautifulSoup(url_text, 'html.parser') 
        
        #category
        searching_span = soup.find('span',class_='Hero-designation')
        self.category = searching_span.text
            
        #name
        searching_name = soup.find('a',class_ = 'Hero-title')
        self.name = searching_name.text

            

            
        #zipcode 
        #response = requests.get(state_url)
       # soup = BeautifulSoup(response.text, 'html.parser')
        searching_zipcode = soup.find('span',itemprop='postalCode')
        self.zipcode = searching_zipcode.text.replace(' ','')

            
        #phone
        searching_phone = soup.find('span',itemprop='telephone')
        self.phone = searching_phone.text.replace('\n','')

        #address
        searching_address = soup.find('p',class_='adr')
        unwanted1 = searching_address.find('span')
        unwanted2 = searching_address.find('span',itemprop='postalCode')
        unwanted1.extract()
        unwanted2.extract()
        self.address = searching_address.text.replace("\n", "")
'''