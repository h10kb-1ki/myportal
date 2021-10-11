import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime

from PIL import Image
import io

import re

'''
## MyPortal
'''

traffic = st.checkbox('Traffic')
if traffic == True:
    '''
    #### 東海道本線[豊橋～米原]
    '''
    url = 'https://transit.yahoo.co.jp/traininfo/detail/192/193/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    nameJ = soup.select_one('h1').text
    kosinJ = soup.find(class_='subText').text
    infoJ = soup.select_one("#mdServiceStatus > dl > dt").text
    st.write(kosinJ)
    st.write(infoJ)
    '''
    ###### ▶JR運行情報
    '''
    st.markdown('https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja', unsafe_allow_html=True)
    st.write('')
    '''
    #### 名鉄名古屋本線
    '''
    url = 'https://transit.yahoo.co.jp/traininfo/detail/208/0/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    nameM = soup.select_one('h1').text
    kosinM = soup.find(class_='subText').text
    infoM = soup.select_one("#mdServiceStatus > dl > dt").text
    st.write(kosinM)
    st.write(infoM)
    st.write('')

    '''
    ###### ▶名鉄バス
    '''
    st.markdown('https://navi.meitetsu-bus.co.jp/mb/DepQR.aspx?p=320103000', unsafe_allow_html=True)

    '''
    ###### ▶乗り換え案内
    '''
    st.markdown('https://www.jorudan.co.jp/norikae/', unsafe_allow_html=True)


weather = st.checkbox('Weather')
if weather == True:
    nagoya = st.checkbox('名古屋市の天気')
    if nagoya == True:
        url = 'https://weathernews.jp/onebox/35.140631/136.856940/q=%E5%90%8D%E5%8F%A4%E5%B1%8B%E5%B8%82%E4%B8%AD%E5%B7%9D%E5%8C%BA&v=6e0846f392462de33f98b88b4ccdc67e48efadd56255e3c54a8f2bf8341c7f00&temp=c&lang=ja'
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        #日付の取得（webページ上から）
        day_ = soup.find_all(class_='wTable__item')
        today = day_[6].text

        #最高・最低気温の取得
        kion = soup.find_all(class_='text wTable__item')
        max_today = kion[0].text
        min_today = kion[1].text
        max_tomorrow = kion[2].text
        min_tomorrow = kion[3].text

        #時間ごとの降水確率の取得
        kakuritu = soup.find_all(class_='text')
        today_p6 = kakuritu[2].text
        today_p12 = kakuritu[3].text
        today_p18 = kakuritu[4].text
        today_p24 = kakuritu[5].text
        tomorrow_p6 = kakuritu[8].text
        tomorrow_p12 = kakuritu[9].text
        tomorrow_p18 = kakuritu[10].text
        tomorrow_p24 = kakuritu[11].text

        #イメージアイコンの取得
        icon = soup.find_all(class_='day2Table__item weather')
        icon_today = 'https:' + icon[0].find('img').get('src')
        icon_tomorrow = 'https:' + icon[1].find('img').get('src')

        #解説コメントの取得
        title = soup.find(class_='tit-02').text
        info = soup.find(class_='comment no-ja')
        comment = info.text
        comment = comment.split('\n')[2]

        st.write(title)
        st.write(comment)
        st.write('■ '+ today)
        st.image(icon_today)
        st.write('最高気温:'+ max_today +'　最低気温:'+ min_today)
        st.write('～6時：'+ today_p6 +'　～12時：'+ today_p12 +'　～18時：'+ today_p18 +'　～24時：'+ today_p24)

        st.write('■ 明日の天気')
        st.image(icon_tomorrow)
        st.write('最高気温:'+ max_tomorrow +'　最低気温:'+ min_tomorrow)
        st.write('～6時：'+ tomorrow_p6 +'　～12時：'+ tomorrow_p12 +'　～18時：'+ tomorrow_p18 +'　～24時：'+ tomorrow_p24)

    anjo = st.checkbox('安城市の天気')
    if anjo == True:
        url = 'https://weathernews.jp/onebox/34.948663/137.079025/q=%E6%84%9B%E7%9F%A5%E7%9C%8C%E5%AE%89%E5%9F%8E%E5%B8%82&v=3fa1edac9382759435af39576ac457ebaf29245456fafb5ff44b458182f4cbbc&temp=c&lang=ja'
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        #日付の取得（webページ上から）
        day_ = soup.find_all(class_='wTable__item')
        today = day_[6].text

        #最高・最低気温の取得
        kion = soup.find_all(class_='text wTable__item')
        max_today = kion[0].text
        min_today = kion[1].text
        max_tomorrow = kion[2].text
        min_tomorrow = kion[3].text

        #時間ごとの降水確率の取得
        kakuritu = soup.find_all(class_='text')
        today_p6 = kakuritu[2].text
        today_p12 = kakuritu[3].text
        today_p18 = kakuritu[4].text
        today_p24 = kakuritu[5].text
        tomorrow_p6 = kakuritu[8].text
        tomorrow_p12 = kakuritu[9].text
        tomorrow_p18 = kakuritu[10].text
        tomorrow_p24 = kakuritu[11].text

        #イメージアイコンの取得
        icon = soup.find_all(class_='day2Table__item weather')
        icon_today = 'https:' + icon[0].find('img').get('src')
        icon_tomorrow = 'https:' + icon[1].find('img').get('src')

        #解説コメントの取得
        title = soup.find(class_='tit-02').text
        info = soup.find(class_='comment no-ja')
        comment = info.text
        comment = comment.split('\n')[2]

        st.write(title)
        st.write(comment)
        st.write('■ '+ today)
        st.image(icon_today)
        st.write('最高気温:'+ max_today +'　最低気温:'+ min_today)
        st.write('～6時：'+ today_p6 +'　～12時：'+ today_p12 +'　～18時：'+ today_p18 +'　～24時：'+ today_p24)

        st.write('■ 明日の天気')
        st.image(icon_tomorrow)
        st.write('最高気温:'+ max_tomorrow +'　最低気温:'+ min_tomorrow)
        st.write('～6時：'+ tomorrow_p6 +'　～12時：'+ tomorrow_p12 +'　～18時：'+ tomorrow_p18 +'　～24時：'+ tomorrow_p24)

    '''
    ###### ▶雨雲レーダー
    '''
    st.markdown('https://tenki.jp/radar/map/', unsafe_allow_html=True)
news = st.checkbox('NEWS')
if news == True:
    yahoo = st.checkbox('Yahoo! ニュース トピックス')
    if yahoo == True:
        url = 'https://www.yahoo.co.jp/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        elems = soup.find_all(href = re.compile('news.yahoo.co.jp/pickup'))
        for i in range(0, len(elems)):
            # titleを取得
            title = elems[i].text
            st.write(f'・{title}')
            # linkを取得
            link = elems[i].attrs['href']
            st.write(f'>>>{link}')
            st.write('')
    seiyaku = st.checkbox('製薬業界ニュース')
    if seiyaku ==True:
        url = 'https://answers.ten-navi.com/pharmanews/pharma_category/1/'
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        titles = soup.find_all('h2')
        tag = soup.find_all(class_='tag')
        ref = soup.find_all('a', class_='clearfix')

        for i in range(0, len(titles)):
            if tag[i].text == 'ニュース解説':
                title = titles[i].text
                link = ref[i].attrs['href']
                st.write(f'・{title}')
                st.write(f'>>>{link}')
                st.write('')

MyLib = st.checkbox('Library')
if MyLib == True:
    '''
    ###### ▶VCM血中濃度シミュレーション
    '''
    st.markdown('https://share.streamlit.io/h10kb-1ki/vcm/vcm_para.py', unsafe_allow_html=True)
    '''
    ###### ▶業務分析アプリ
    '''
    st.markdown('https://share.streamlit.io/h10kb-1ki/workanalysis/WorkAnalysis.py', unsafe_allow_html=True)
    '''
    ###### ▶ToDoリスト（閉鎖中）
    '''
    st.markdown('https://share.streamlit.io/h10kb-1ki/todolist/ToDoList.py', unsafe_allow_html=True)

    '''
    ###### ▶一郎の部屋
    '''
    st.markdown('https://sites.google.com/view/tdmichiro/%E3%83%9B%E3%83%BC%E3%83%A0', unsafe_allow_html=True)
