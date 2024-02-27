import requests
import json
from bs4 import BeautifulSoup
import re

def scrape_website(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        all_links = soup.find_all('a', class_='line-clamp-1')

        data_list = []

        for link in all_links:
            category = link.find('h2').get_text(strip=True)
            total_element = link.find('span', class_='text-neutral-500')

            if total_element:
                number = re.search(r'\d+', total_element.get_text(strip=True))
                if number:
                    total = number.group()
                else:
                    total = 'Angka tidak ditemukan'

            else:
                total = 'data tidak ditemukan'

            url = link.get('href')

            data_list.append({
                'category': category,
                'total': total,
                'url': url
            })

            with open(output_file, 'w') as f:
                json.dump(data_list, f, indent=4)

            print('Data telah disimpan dalam file:', output_file)
    else:
        print('Gagal mengunduh halaman', response.status_code)

url_to_scrape = 'https://quran.nu.or.id/doa'
output_json_file = 'doa-categories.json'
scrape_website(url_to_scrape, output_json_file)
