import json
from bs4 import BeautifulSoup

html_content = """
<div class='max-w-screen'>
    # list ke-1
    <div class="text-center mt-10 mb-6">
        <span class="font-normal block text-sm lg:text-base text-neutral-500 dark:text-neutral-300">1/9</span>
        <h1 class="text-lg md:text-xl lg:text-1xl font-semibold">Doa Berangkat Kerja</h1>
    </div>
    <div class="last:border-none border-b border-neutral-100 dark:border-neutral-800 py-5 px-3 md:px-5 ">
        <div class="flex">
            <div class="flex-grow flex flex-col ms-2 text-lg rounded-xl sm:ms-3 sm:text-base dark:border-neutral-700">
                <div class="flex flex-col space-y-3">
                    <span class="__className_6952f9 text-4xl lg:text-5xl leading-relaxed lg:leading-relaxed text-right">بِسْمِ اللهِ عَلَى نَفْسِيْ وَمَالِي وَدِيْنِيْ، اَللّٰهُمَّ رَضِّنِيْ بِقَضَائِكَ وَبَارِكْ لِي فِيْمَا قُدِّرَ لِيْ حَتَّى لَا أُحِبَّ تَعْجِيْلَ مَا أَخَّرْتَ وَلَا تَأْخِيْرَ مَا عَجَّلْتَ</span>
                    <span class="block text-md lg:text-lg text-neutral-700 dark:text-neutral-300">Dengan menyebut nama Allah, atas diriku, hartaku, dan agamaku. Ya Allah, jadikanlah aku orang yang ridha (menerima) atas ketetapan-Mu serta berkahilah aku atas rezeki yang Engkau tentukan sehingga aku tak tergesa-gesa meminta sesuatu yang Engkau tunda, atau menunda-nunda sesuatu yang Engkau hendak segerakan. (HR Ibnu as-Sunni).</span>
                </div>
            </div>
        </div>
    </div>

    # list ke-2
    <div class="text-center mt-10 mb-6">
        <span class="font-normal block text-sm lg:text-base text-neutral-500 dark:text-neutral-300">2/9</span>
        <h1 class="text-lg md:text-xl lg:text-1xl font-semibold">Doa Mudah Raih Rezeki</h1>
    </div>
    <div class="last:border-none border-b border-neutral-100 dark:border-neutral-800 py-5 px-3 md:px-5 ">
        <div class="flex">
            <div class="flex-grow flex flex-col ms-2 text-lg rounded-xl sm:ms-3 sm:text-base dark:border-neutral-700">
                <div class="flex flex-col space-y-3">
                    <span class="__className_6952f9 text-4xl lg:text-5xl leading-relaxed lg:leading-relaxed text-right">اَللّٰهُ لَطِيْفٌۢ بِعِبَادِهٖ يَرْزُقُ مَنْ يَّشَاۤءُۚ وَهُوَ الْقَوِيُّ الْعَزِيْزُ</span>
                    <span class="block text-md lg:text-lg text-neutral-700 dark:text-neutral-300">Allah Mahalembut terhadap hamba-hamba-Nya; Dia memberi rezeki kepada siapa yang Dia kehendaki dan Dia Mahakuat, Mahaperkasa.</span>
                </div>
            </div>
        </div>
    </div>
    <div class="last:border-none border-b border-neutral-100 dark:border-neutral-800 py-5 px-3 md:px-5 ">
        <div class="flex">
            <div class="flex-grow flex flex-col ms-2 text-lg rounded-xl sm:ms-3 sm:text-base dark:border-neutral-700">
                <div class="flex flex-col space-y-3">
                    <span class="__className_6952f9 text-4xl lg:text-5xl leading-relaxed lg:leading-relaxed text-right">اَللّٰهُمَّ إِنِّي أَسْأَلُكَ أَنْ تَرْزُقَنِيْ رِزْقًا حَلَالًا وَاسِعًا طَيِّبًا مِنْ غَيْرِ تَعَبٍ وَلَا مَشَقَّةٍ وَلَا ضَيْرٍ وَلَانَصَبٍ إِنَّكَ عَلَى كُلِّ شَيْءٍ قَدِيْرٌ</span>
                    <span class="block text-md lg:text-lg text-neutral-700 dark:text-neutral-300">Ya Allah aku mohon kepadamu limpahan rezeki yang halal, luas, dan baik, yang didapat tanpa letih, memberatkan, membahayakan, dan banting tulang. Sungguh Engkau Mahakuasa atas segala sesuatu.</span>
                </div>
            </div>
        </div>
    </div>

    # list ke-3
    <div class="text-center mt-10 mb-6">
        <span class="font-normal block text-sm lg:text-base text-neutral-500 dark:text-neutral-300">1/9</span>
        <h1 class="text-lg md:text-xl lg:text-1xl font-semibold">Doa Bercermin</h1>
    </div>
    <div class="last:border-none border-b border-neutral-100 dark:border-neutral-800 py-5 px-3 md:px-5 ">
        <div class="flex">
            <div class="flex-grow flex flex-col ms-2 text-lg rounded-xl sm:ms-3 sm:text-base dark:border-neutral-700">
                <div class="flex flex-col space-y-3">
                    <span class="__className_6952f9 text-4xl lg:text-5xl leading-relaxed lg:leading-relaxed text-right">بِسْمِ اللهِ عَلَى نَفْسِيْ وَمَالِي وَدِيْنِيْ، اَللّٰهُمَّ رَضِّنِيْ بِقَضَائِكَ وَبَارِكْ لِي فِيْمَا قُدِّرَ لِيْ حَتَّى لَا أُحِبَّ تَعْجِيْلَ مَا أَخَّرْتَ وَلَا تَأْخِيْرَ مَا عَجَّلْتَ</span>
                    <span class="block text-md lg:text-lg text-neutral-700 dark:text-neutral-300">Dengan menyebut nama Allah, atas diriku, hartaku, dan agamaku. Ya Allah, jadikanlah aku orang yang ridha (menerima) atas ketetapan-Mu serta berkahilah aku atas rezeki yang Engkau tentukan sehingga aku tak tergesa-gesa meminta sesuatu yang Engkau tunda, atau menunda-nunda sesuatu yang Engkau hendak segerakan. (HR Ibnu as-Sunni).</span>
                </div>
            </div>
        </div>
    </div>

    # list ke-4
    <div class="text-center mt-10 mb-6">
        <span class="font-normal block text-sm lg:text-base text-neutral-500 dark:text-neutral-300">2/9</span>
        <h1 class="text-lg md:text-xl lg:text-1xl font-semibold">Doa Makan</h1>
    </div>
    <div class="last:border-none border-b border-neutral-100 dark:border-neutral-800 py-5 px-3 md:px-5 ">
        <div class="flex">
            <div class="flex-grow flex flex-col ms-2 text-lg rounded-xl sm:ms-3 sm:text-base dark:border-neutral-700">
                <div class="flex flex-col space-y-3">
                    <span class="__className_6952f9 text-4xl lg:text-5xl leading-relaxed lg:leading-relaxed text-right">اَللّٰهُ لَطِيْفٌۢ بِعِبَادِهٖ يَرْزُقُ مَنْ يَّشَاۤءُۚ وَهُوَ الْقَوِيُّ الْعَزِيْزُ</span>
                    <span class="block text-md lg:text-lg text-neutral-700 dark:text-neutral-300">Allah Mahalembut terhadap hamba-hamba-Nya; Dia memberi rezeki kepada siapa yang Dia kehendaki dan Dia Mahakuat, Mahaperkasa.</span>
                </div>
            </div>
        </div>
    </div>
    <div class="last:border-none border-b border-neutral-100 dark:border-neutral-800 py-5 px-3 md:px-5 ">
        <div class="flex">
            <div class="flex-grow flex flex-col ms-2 text-lg rounded-xl sm:ms-3 sm:text-base dark:border-neutral-700">
                <div class="flex flex-col space-y-3">
                    <span class="__className_6952f9 text-4xl lg:text-5xl leading-relaxed lg:leading-relaxed text-right">اَللّٰهُمَّ إِنِّي أَسْأَلُكَ أَنْ تَرْزُقَنِيْ رِزْقًا حَلَالًا وَاسِعًا طَيِّبًا مِنْ غَيْرِ تَعَبٍ وَلَا مَشَقَّةٍ وَلَا ضَيْرٍ وَلَانَصَبٍ إِنَّكَ عَلَى كُلِّ شَيْءٍ قَدِيْرٌ</span>
                    <span class="block text-md lg:text-lg text-neutral-700 dark:text-neutral-300">Ya Allah aku mohon kepadamu limpahan rezeki yang halal, luas, dan baik, yang didapat tanpa letih, memberatkan, membahayakan, dan banting tulang. Sungguh Engkau Mahakuasa atas segala sesuatu.</span>
                </div>
            </div>
        </div>
    </div>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')
list_header = soup.find_all('h1', class_='font-semibold')

data = []

for i, header in enumerate(list_header):
    title_text = header.text.strip()

    current_header_index = html_content.index(str(header))

    if i < len(list_header) - 1:
        next_header_index = html_content.index(str(list_header[i + 1]))
    else:
        next_header_index = len(html_content)


    current_content = html_content[current_header_index:next_header_index]
    arabics = BeautifulSoup(current_content, 'html.parser').find_all('span', class_='__className_6952f9')
    arabic_text = [arabic.text.strip() for arabic in arabics]

    translates = BeautifulSoup(current_content, 'html.parser').find_all('span', class_='text-md')
    translate_text = [translate.text.strip() for translate in translates]

    data.append({
        'title': title_text,
        'arabics': arabic_text,
        'translates': translate_text
    })

print(json.dumps(data, indent=4, ensure_ascii=False))
