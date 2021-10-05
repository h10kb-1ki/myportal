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
    #### JR
    '''
    st.markdown('https://traininfo.jr-central.co.jp/zairaisen/status_detail.html?line=10001&lang=ja', unsafe_allow_html=True)

    '''
    #### 名鉄バス
    '''
    st.markdown('https://navi.meitetsu-bus.co.jp/mb/DepQR.aspx?p=320103000', unsafe_allow_html=True)

    '''
    #### 乗り換え案内
    '''
    st.markdown('https://www.jorudan.co.jp/norikae/', unsafe_allow_html=True)

    '''
    ###### 【予定】webスクレイピング →遅延情報取得 時刻表
    ######
    '''

weather = st.checkbox('Weather')
if weather == True:
    url = 'https://weathernews.jp/onebox/34.948663/137.079025/q=%E6%84%9B%E7%9F%A5%E7%9C%8C%E5%AE%89%E5%9F%8E%E5%B8%82&v=3fa1edac9382759435af39576ac457ebaf29245456fafb5ff44b458182f4cbbc&temp=c&lang=ja'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    rainy_prob = soup.find_all('td')
    # 時間ごとの降水確率を取得
    tmr = format((datetime.datetime.now() + datetime.timedelta(days = 1)).day)
    tmr_6 = rainy_prob[4].text
    tmr_12 = rainy_prob[5].text
    tmr_18 = rainy_prob[6].text
    tmr_24 = rainy_prob[7].text
    tomorrow = str(tmr+'日の天気（安城市）')
    yohou = str('～6時：'+tmr_6+'、～12時：'+tmr_12+'、～18時：'+tmr_18+'、～24時：'+tmr_24)
    # 解説コメントを取得
    cmt = soup.find(class_='comment no-ja')
    comment = cmt.text

    # 画像を取得
    #imgs = soup.find_all(class_='weather-2day__icon')
    #img_src = imgs[1].get("src")

    #img_url = 'https:'+img_src   #ソース（src）にhttpsをつけてurlへ
    #img = Image.open(io.BytesIO(requests.get(img_url).content))

    '''
    #### 明日の降水確率（安城市）
    '''
    st.write(yohou)
    st.write(comment)
    #st.image(img)

    '''
    #### 雨雲レーダー
    '''
    st.markdown('https://tenki.jp/radar/map/', unsafe_allow_html=True)
news = st.checkbox('NEWS')
if news == True:
    '''
    #### Yahoo! ニュース トピックス
    #####
    '''
    url = 'https://www.yahoo.co.jp/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    elems = soup.find_all(href = re.compile('news.yahoo.co.jp/pickup'))
    col1, col2 = st.columns(2)
    for i in range(0, len(elems)):
        # titleを取得
        title = elems[i].text
        with col1:
            st.write(title)
        # linkを取得
        link = elems[i].attrs['href']
        with col2:
            st.write(link)

ToDo = st.checkbox('ToDo List')
if ToDo == True:
    st.markdown('https://share.streamlit.io/h10kb-1ki/todolist/ToDoList.py', unsafe_allow_html=True)

finance = st.checkbox('Finance')
if finance == True:
    '''
    ##### 作成中
    #####
    '''
    #st.markdown('', unsafe_allow_html=True)

MyLib = st.checkbox('Library')
if MyLib == True:
    '''
    #### VCM血中濃度シミュレーション
    '''
    st.markdown('https://share.streamlit.io/h10kb-1ki/vcm/vcm_para.py', unsafe_allow_html=True)
    
    '''
    #### 業務分析アプリ
    '''
    st.markdown('https://share.streamlit.io/h10kb-1ki/workanalysis/WorkAnalysis.py', unsafe_allow_html=True)
    
    '''
    #### 一郎の部屋
    '''
    st.markdown('https://sites.google.com/view/tdmichiro/%E3%83%9B%E3%83%BC%E3%83%A0', unsafe_allow_html=True)