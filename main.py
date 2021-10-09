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
        st.write('■'+ today)
        st.image(icon_today)
        st.write('最高気温:'+ max_today +'　最低気温:'+ min_today)
        st.write('～6時：'+ today_p6 +'　～12時：'+ today_p12 +'　～18時：'+ today_p18 +'　～24時：'+ today_p24)

        st.write('■明日の天気')
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
        st.write(’■’+ today)
        st.image(icon_today)
        st.write('最高気温:'+ max_today +'　最低気温:'+ min_today)
        st.write('～6時：'+ today_p6 +'　～12時：'+ today_p12 +'　～18時：'+ today_p18 +'　～24時：'+ today_p24)

        st.write('■明日の天気')
        st.image(icon_tomorrow)
        st.write('最高気温:'+ max_tomorrow +'　最低気温:'+ min_tomorrow)
        st.write('～6時：'+ tomorrow_p6 +'　～12時：'+ tomorrow_p12 +'　～18時：'+ tomorrow_p18 +'　～24時：'+ tomorrow_p24)

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
    vcm = st.checkbox('VCM血中濃度シミュレーション')
    if vcm == True:
        import streamlit as st
        import math
        import pandas as pd
        import matplotlib.pyplot as plt

        global age
        global gen
        global height
        global weight
        global SCr
        global dose
        global tau

        st.title('VCMパラメータ計算')
        """
        #### 1-コンパートメントモデルを用いてトラフ値およびAUCを計算します。
        #### 当サイトのご利用は自己責任でお願いします。
        ####
        """
        st.sidebar.title('基本情報')
        age = st.sidebar.slider('■年齢', 0, 100, 60)
        gen = st.sidebar.radio('■性別', ('M', 'F'), index=0)
        height = st.sidebar.slider('■身長（cm）', 120, 200, 160)
        weight = st.sidebar.slider('■体重（kg）', 20, 150, 50)
        SCr = st.sidebar.slider('■SCr', 0.00, 2.50, 0.70)

        st.sidebar.title('設定値')
        dose_select = st.sidebar.radio('投与量の入力方法', ('選択', '任意'), index=0)
        if dose_select ==  '選択':
            dose = st.sidebar.slider('■投与量（mg）', 250, 4000, 2000, step=250)
        elif dose_select == '任意':
            dose = st.sidebar.number_input('■投与量（mg）')
        tau = st.sidebar.radio('■投与間隔（hr）', (6, 8, 12, 24, 48), index=3)

        """
        ## ―体格―
        """
        def cal_BMI(height, weight):
            BMI = weight/(height/100)**2
            return BMI
        BMI = cal_BMI(height, weight)

        if BMI >25:
            adj_BW = 25 * (height/100)**2
            comment = f'  ※補正体重 {round(adj_BW, 1)} (kg)を使用してください'
        else:
            comment = ''
        'BMI = ', round(BMI, 2), comment

        def cal_BSA(height, weight):
            BSA = weight**0.425 * height**0.725 * 0.007184
            return BSA
        BSA = cal_BSA(height, weight)
        'BSA (m2) = ', round(BSA, 3)


        """
        ## ―腎機能―
        """
        def cal_CLcr(age, weight, SCr):
            CLcr = (140-age)*weight / (72*SCr)
            return CLcr
        if gen == 'M':
            CLcr = cal_CLcr(age, weight, SCr)
        else:
            CLcr = cal_CLcr(age, weight, SCr)*0.85
        'CLcr (mL/min) = ', round(CLcr, 1)

        def cal_eGFR(SCr, age):
            eGFR = 194*(SCr**(-1.094))*(age**(-0.287))
            return eGFR
        if gen == 'M':
            eGFR = cal_eGFR(SCr, age)
        else:
            eGFR = cal_eGFR(SCr, age) *0.739
        'eGFR (mL/min/1.73) = ', round(eGFR, 1)

        adj_eGFR = eGFR * BSA /1.73
        'BSA未補正eGFR (mL/min) = ', round(adj_eGFR, 1)

        """
        ## 
        ## ―VCM初期パラメータ―
        """
        CLvcm = CLcr * 0.797*60/1000
        'CLvcm (L/hr) = ', round(CLvcm, 2)
        Vd = weight * 0.7
        'Vd (L) = ', round(Vd, 1)
        kel = CLvcm / Vd
        'kel (/hr) = ', round(kel, 3)
        t_half = math.log(2)/kel
        't1/2 (hr) = ', round(t_half, 1)
        Ctrough = ((dose/Vd)/(1-math.exp(-kel*tau)))*math.exp(-kel*tau)
        'Ctrough (mg/L) = ', round(Ctrough, 2)
        AUC = dose/CLvcm *24/tau
        'AUC (mg・hr/L) = ', round(AUC, 1)


        st.title('VCMパラメータ Fitting')

        kel_select = st.radio('kel検討レンジ', ('kel < 0.1', 'kel > 0.1'), index=0)
        """
        ### 
        ## ―Simulation #1―
        """
        if kel_select == 'kel < 0.1':
            kel_max = 110
        else:
            kel_max =1000

        f_Vd = st.slider('Vd', 0.0, 100.0, round(Vd, 1), step=0.1)
        f_kel = st.slider('kel（x 0.001）', 0, kel_max, int(kel*1000))

        f_CLvcm = f_Vd * (f_kel/1000)
        'CLvcm (L/hr) = ', round(f_CLvcm, 2)
        f_t_half = math.log(2) / (f_kel/1000)
        't1/2 (/hr) = ', round(f_t_half, 1)
        f_Ctrough = ((dose/f_Vd)/(1-math.exp(-(f_kel/1000)*tau)))*math.exp(-(f_kel/1000)*tau)
        'Ctrough (mg/L) = ', round(f_Ctrough, 2)
        f_AUC = dose/f_CLvcm *24/tau
        'AUC (mg・hr/L) = ', round(f_AUC, 1)

        #----------------------------------------------------------------グラフ化↓
        time = list(range(0, 120, 1))
        C1 = []
        for t in time:
            conc = (dose/f_Vd)*math.exp(-(f_kel/1000)*t)
            C1.append(conc)

        df = pd.DataFrame({'time':time, 'C1':C1})
        df = df.set_index('time')
        df['C2'] = df['C1'].shift(tau)
        df['C3'] = df['C1'].shift(tau*2)
        df['C4'] = df['C1'].shift(tau*3)
        df['C5'] = df['C1'].shift(tau*4)
        df['C6'] = df['C1'].shift(tau*5)
        df['C7'] = df['C1'].shift(tau*6)
        df['C8'] = df['C1'].shift(tau*7)
        df['C9'] = df['C1'].shift(tau*8)
        df['C10'] = df['C1'].shift(tau*9)
        df['C11'] = df['C1'].shift(tau*10)
        df['C12'] = df['C1'].shift(tau*11)
        df['C13'] = df['C1'].shift(tau*12)
        df['C14'] = df['C1'].shift(tau*13)
        df['C15'] = df['C1'].shift(tau*14)
        df = df.fillna(0)
        C = df.sum(axis='columns')

        fig = plt.figure(figsize=(9, 6))
        ax = fig.add_subplot(1,1,1)

        ax.set_ylim([0, 80])
        ax.set_xlim([0, 120])

        start, end = ax.get_xlim()
        stepsize=24
        ax.xaxis.set_ticks(pd.np.arange(start, end, stepsize))

        ax.plot(time, C, linewidth=2, color='darkturquoise')
        plt.xlabel('Time (hr)', fontsize=18)
        plt.ylabel('Concentration (mg/L)', fontsize=18)

        graph_display = st.checkbox('グラフ1を表示')
        if graph_display == True:
            #st.write(df)
            st.pyplot(fig)
        #----------------------------------------------------------------グラフ化↑

        """
        # 
        """
        S2_display = st.checkbox('別の一手')
        if S2_display == True:
            """
            ## ―Simulation #2―
            """
            f2_Vd = st.slider('Vd', 0.0, 100.0, 30.0, step=0.1)
            f2_kel = st.slider('kel（x 0.001）', 0, kel_max, 100)

            f2_CLvcm = f2_Vd * (f2_kel/1000)
            'CLvcm (L/hr) = ', round(f2_CLvcm, 2)
            f2_t_half = math.log(2) / (f2_kel/1000)
            't1/2 (/hr) = ', round(f2_t_half, 1)
            f2_Ctrough = ((dose/f2_Vd)/(1-math.exp(-(f2_kel/1000)*tau)))*math.exp(-(f2_kel/1000)*tau)
            'Ctrough (mg/L) = ', round(f2_Ctrough, 2)
            f2_AUC = dose/f2_CLvcm *24/tau
            'AUC (mg・hr/L) = ', round(f2_AUC, 1)

            #----------------------------------------------------------------グラフ化↓
            Co1 = []
            for t in time:
                conc = (dose/f2_Vd)*math.exp(-(f2_kel/1000)*t)
                Co1.append(conc)

            df2 = pd.DataFrame({'time':time, 'Co1':Co1})
            df2 = df2.set_index('time')
            df2['Co2'] = df2['Co1'].shift(tau)
            df2['Co3'] = df2['Co1'].shift(tau*2)
            df2['Co4'] = df2['Co1'].shift(tau*3)
            df2['Co5'] = df2['Co1'].shift(tau*4)
            df2['Co6'] = df2['Co1'].shift(tau*5)
            df2['Co7'] = df2['Co1'].shift(tau*6)
            df2['Co8'] = df2['Co1'].shift(tau*7)
            df2['Co9'] = df2['Co1'].shift(tau*8)
            df2['Co10'] = df2['Co1'].shift(tau*9)
            df2['Co11'] = df2['Co1'].shift(tau*10)
            df2['Co12'] = df2['Co1'].shift(tau*11)
            df2['Co13'] = df2['Co1'].shift(tau*12)
            df2['Co14'] = df2['Co1'].shift(tau*13)
            df2['Co15'] = df2['Co1'].shift(tau*14)
            df2 = df2.fillna(0)
            Con = df2.sum(axis='columns')

            fig2 = plt.figure(figsize=(9, 6))
            ax2 = fig2.add_subplot(1,1,1)

            ax2.set_ylim([0, 80])
            ax2.set_xlim([0, 120])

            start, end = ax2.get_xlim()
            stepsize=24
            ax2.xaxis.set_ticks(pd.np.arange(start, end, stepsize))

            ax2.plot(time, Con, linewidth=2, color='hotpink')
            plt.xlabel('Time (hr)', fontsize=18)
            plt.ylabel('Concentration (mg/L)', fontsize=18)

            graph2_display = st.checkbox('グラフ2を表示')
            if graph2_display == True:
                #st.write(df)
                st.pyplot(fig2)
            #----------------------------------------------------------------グラフ化↑

            grapg_merge = st.checkbox('グラフ1・2を重ねて表示')
            if grapg_merge == True:
                fig = plt.figure(figsize=(9, 6))
                ax = fig.add_subplot(1,1,1)

                ax.set_ylim([0, 80])
                ax.set_xlim([0, 120])

                start, end = ax.get_xlim()
                stepsize=24
                ax.xaxis.set_ticks(pd.np.arange(start, end, stepsize))

                ax.plot(time, C, linewidth=2, color='darkturquoise')
                ax.plot(time, Con, linewidth=2, color='hotpink')

                plt.xlabel('Time (hr)', fontsize=18)
                plt.ylabel('Concentration (mg/L)', fontsize=18)
                st.pyplot(fig)


    workanal = st.checkbox('業務分析アプリ')
    if workanal == True:
        '''
        #### 業務分析アプリ
        '''
        st.markdown('https://share.streamlit.io/h10kb-1ki/workanalysis/WorkAnalysis.py', unsafe_allow_html=True)

    ichiro = st.checkbox('一郎の部屋')
    if ichiro == True:
        '''
        #### 一郎の部屋
        '''
        st.markdown('https://sites.google.com/view/tdmichiro/%E3%83%9B%E3%83%BC%E3%83%A0', unsafe_allow_html=True)
