from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
import random
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc
import requests
from bs4 import BeautifulSoup

#Window.size=(320,600)
username_input="""
MDTextField:
    
    hint_text: "Enter city of locating "
    hint_text_size:30
    helper_text: "must be an integer"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.8}
    size_hint_x:.5
    size_hint_y:.1
    font_size:'15sp'
    width:400
"""
username_input1 = """
MDTextField:
    hint_text: "Enter Gender 1-Male 0-Female:    "
    hint_text_size:30
    helper_text: "must be an integer"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.7}
    size_hint_x:.5
    size_hint_y:.1
    font_size:'15sp'
    width:400
"""
username_input2 = """
MDTextField:
    hint_text: "Enter Actual PEFR value:    "
    hint_text_size:30
    helper_text: "must be an integer"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:.5
    size_hint_y:.1
    font_size:'15sp'
    width:400
"""
def predicter(city,g,actual_pefr):
    l=['Cuddalore','Tiruppur','Ooty','Krishnagiri','Kattivakkam','Dindigul','Chennai','Arcot','Ariyalur']
    data=pd.DataFrame.from_dict({'Age': [19, 26, 22, 25, 18, 18, 26, 33, 40, 25, 20, 27, 29, 26, 25, 20, 20, 23, 17, 18, 19, 20, 36, 49, 25, 29, 23, 24, 27, 15, 33, 65, 24, 26, 32, 16, 20, 25, 26, 29, 27, 23, 22, 33, 36, 36, 25, 39, 34, 29, 28, 25, 36, 22], 'Height': [155, 183, 153, 160, 162, 150, 176, 146, 178, 164, 195, 153, 149, 157, 140, 168, 174, 154, 176, 155, 150, 149, 160, 153, 164, 152, 169, 154, 180, 160, 145, 190, 160, 169, 142, 195, 146, 187, 182, 162, 146, 186, 144, 176, 155, 169, 166, 185, 166, 178, 145, 177, 146, 149], 'Gender': [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], 'Outdoor Temperature': [33, 32, 27, 26, 26, 32, 29, 24, 33, 36, 29, 27, 30, 31, 26, 24, 33, 28, 27, 34, 30, 25, 27, 20, 26, 24, 28, 29, 32, 21, 25, 24, 26, 36, 22, 33, 36, 34, 31, 22, 24, 27, 26, 32, 23, 36, 25, 34, 21, 25, 26, 35, 24, 33], 'Humidity': [60, 71, 85, 88, 85, 64, 82, 86, 65, 55, 78, 86, 62, 66, 89, 90, 64, 86, 89, 63, 68, 78, 73, 92, 88, 88, 78, 67, 62, 92, 90, 88, 84, 59, 79, 68, 64, 63, 60, 83, 89, 81, 76, 70, 89, 52, 82, 60, 95, 82, 84, 56, 81, 56], 'PM 2.5 ': [16, 12, 27, 18, 16, 38, 22, 34, 27, 28, 26, 18, 12, 16, 34, 20, 33, 21, 19, 14, 12, 18, 16, 20, 34, 20, 26, 38, 21, 36, 37, 25, 21, 26, 21, 25, 25, 12, 13, 18, 18, 14, 16, 22, 26, 29, 19, 18, 26, 24, 15, 16, 35, 24], 'PM 10': [23.62, 18.29, 38.29, 26.2, 23.62, 52.8, 31.62, 47.5, 38.3, 39.8, 36.0, 27.0, 18.0, 23.66, 47.5, 29.0, 46.1, 30.5, 27.7, 21.0, 18.0, 27.0, 23.66, 29.0, 48.0, 35.0, 40.0, 50.0, 36.0, 48.0, 49.0, 40.0, 36.0, 39.0, 35.0, 29.0, 33.0, 24.0, 26.0, 29.0, 32.0, 24.0, 28.0, 35.0, 36.0, 39.0, 29.0, 30.0, 32.0, 35.0, 30.0, 36.0, 51.0, 40.0], 'PEFR': [524, 640, 356, 402, 424, 465, 540, 326, 512, 399, 578, 401, 460, 453, 366, 571, 522, 432, 621, 531, 502, 456, 587, 516, 486, 460, 502, 412, 621, 322, 302, 600, 483, 513, 454, 586, 450, 651, 643, 586, 476, 608, 466, 578, 472, 565, 498, 600, 420, 598, 444, 599, 356, 416]})
    data.shape
    X=data.drop(columns=['Age','Height','PEFR'])
    y=data['PEFR']
    model=dtc()
    model.fit(X,y)
    url = f'https://www.iqair.com/in-en/india/tamil-nadu/{city}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    aqi_dict = []
    s = soup.find('table',class_ = "aqi-overview-detail__other-pollution-table")
    if(s==None):
        city = random.choice(l).lower()
        url = 'https://www.iqair.com/in-en/india/tamil-nadu/'+city
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        aqi_dict = []
        s = soup.find('table',class_ = "aqi-overview-detail__other-pollution-table")
    for x in s:
        aqi_dict.append(x.text)
    aqi = aqi_dict[1]
    a=aqi.split(" ")
    pm2_index = a.index("PM2.5")
    pm2 = a[pm2_index +1][0:2]
    if 'PM10' not in aqi_dict :
        pm10 = 1.38 * float(pm2)
    else:
        pm10_index = a.index("PM10")
        pm10 = a[pm10_index+ 1][0:2]
    t = soup.find('div', class_="weather__detail")
    y = t.text
    temp_index = y.find('Temperature')+11
    degree_index = y.find('°')
    temp = y[temp_index : degree_index]
    hum_index = y.find('Humidity')+8
    perc_index = y.find('%')
    hum = y[hum_index:perc_index]
    p=temp
    q=hum
    r=pm2
    s=pm10
    prediction = model.predict([[g,p,q,r,s]])
    predicted_pefr = prediction[0]
    perpefr = (actual_pefr/predicted_pefr)*100
    if perpefr >= 80:
        re='SAFE'
    elif perpefr >= 50:
        re='MODERATE'
    else:
        re='RISK'
    return (re,predicted_pefr,actual_pefr,(perpefr//100)*10)
class DemoApp(MDApp):
    
    def build(self):
        self.screen=Screen()
        self.theme_cls.primary_palette = "Green"
        self.label = MDLabel(text="ASTHMA RISK PREDICTION", halign="center",theme_text_color='Custom',
                        text_color=(0,1,0,1),font_style='H4',pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.username = Builder.load_string(username_input)
        self.username1 = Builder.load_string(username_input1)
        self.username2 = Builder.load_string(username_input2)
        
        self.btn = MDRectangleFlatButton(text='Calculate',font_size='20sp',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.1},size_hint=(.2, .1)
                                             ,on_release=self.mul)
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.username)
        self.screen.add_widget(self.username1)
        self.screen.add_widget(self.username2)
        self.screen.add_widget(self.btn)
        return self.screen
    def mul(self,obj):
        self.screen.remove_widget(self.label)
        self.screen.remove_widget(self.username)
        self.screen.remove_widget(self.username1)
        self.screen.remove_widget(self.username2)
        self.screen.remove_widget(self.btn)
        r=predicter(str(self.username.text),
                  int(self.username1.text),
                  int(self.username2.text),)
        self.label1 = MDLabel(text="PREDICTION RESULTS", halign="center",theme_text_color='Custom',
                        text_color=(0,1,0,1),font_style='H4',pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.label_1 = MDLabel(text="PREDICTED PEFR:   "+str(r[1]), halign="center",theme_text_color='Custom',
                        text_color=(0,0,1,1),font_style='H5',pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.label1_ = MDLabel(text="ACTUAL PEFR ENTERED:   "+str(r[2]), halign="center",theme_text_color='Custom',
                        text_color=(1,0,1,1),font_style='H5',pos_hint={'center_x': 0.5, 'center_y': 0.5}) 
        if(r[0]=='SAFE'):
            c=(0,1,0,1)
        if(r[0]=='MODERATE'):
            c=(1,1,0,1)
        if(r[0]=='RISK'):
            c=(1,0,0,1)
        self.label2 = MDLabel(text=str(r[0]), halign="center",theme_text_color='Custom',
                        text_color=c,font_style='H4',pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.button = MDRectangleFlatButton(text='Back',
                                       pos_hint={'center_x': 0.8, 'center_y': 0.1   },
                                            on_release=self.back)
        self.screen.add_widget(self.label1)
        self.screen.add_widget(self.label_1)
        self.screen.add_widget(self.label1_)
        self.screen.add_widget(self.label2)
        self.screen.add_widget(self.button)
    def back(self,obj):
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.username)
        self.screen.add_widget(self.username1)
        self.screen.add_widget(self.username2)
        self.screen.add_widget(self.btn)
        self.screen.remove_widget(self.button)
        self.screen.remove_widget(self.label1)
        self.screen.remove_widget(self.label2)
        self.screen.remove_widget(self.label_1)
        self.screen.remove_widget(self.label1_)
        self.screen.remove_widget(self.button)
DemoApp().run()
