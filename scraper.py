from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import Request, urlopen

def scrape():
    req = Request('https://www.klmoneychanger.com/forex.php?n=USD&d=US+Dollar&q=', headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req)
    soup = BeautifulSoup(url, 'lxml')
    soup = soup.find('div', id='webuy')

    data = soup.find_all('tr', class_='accordion-toggle')
    rates = soup.find_all('span', style="font-size: 4vh;color:red")

    exchange_rates = []
    for index, d in enumerate(data):
        name = d.text.strip()
        rate = rates[index].text.strip()
        data = {
            "name" : name,
            "rate" : rate
        }
        exchange_rates.append(data)

    sorted_rates = sorted(exchange_rates, key=lambda x : x['rate'], reverse=True)
    return sorted_rates

