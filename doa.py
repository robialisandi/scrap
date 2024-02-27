import sys
import os
import requests
import json
from bs4 import BeautifulSoup

def scrape_website(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        nui = soup.find('div', class_='nui-PageDoaDetail')
        screen = nui.find('div', class_='max-w-screen-lg mx-auto mt-5')
        html_content = screen

        list_header = html_content.find_all('div', class_='text-center mt-10 mb-6')

        data = []

        for i, header in enumerate(list_header):
            title_text = header.find('h1').text.strip()
            formatted_html = html_content.prettify()
            current_header_index = formatted_html.index(str(title_text))

            if i < len(list_header) - 1:
                next_header_index = formatted_html.index(str(list_header[i + 1].find('h1').text.strip()))
            else:
                next_header_index = len(formatted_html)

            current_content = formatted_html[current_header_index:next_header_index]
            arabics = BeautifulSoup(current_content, 'html.parser').find_all('span', class_='__className_6952f9')
            arabic_text = [arabic.text.strip() for arabic in arabics]

            scripts = BeautifulSoup(current_content, 'html.parser').find_all('span', class_='text-primary-500')
            script_text = [script.text.strip() for script in scripts]

            translates = BeautifulSoup(current_content, 'html.parser').find_all('span', class_='text-neutral-700')
            translate_text = [translate.text.strip() for translate in translates]

            data.append({
                'title': title_text,
                'text_arabic': arabic_text,
                'text_script': script_text,
                'translate': translate_text
            })

        output_file_path = os.path.join('data-doa', output_file)
        os.makedirs('data-doa', exist_ok=True)

        with open(output_file_path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            print(output_file + ' Successful scrape')
    else:
        print('Gagal mengunduh halaman', response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python doa.py <config_file>')
        sys.exit(1)

    config_file = sys.argv[1]

    with open(config_file) as f:
        config = json.load(f)

    for item in config:
        url = item['url']
        output_file = item['output_file']
        scrape_website(url, output_file)
