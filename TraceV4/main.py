from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.behaviors import button
from kivy.uix.screenmanager import SwapTransition
from kivymd.uix import dialog
from kivymd.uix import picker
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDThemePicker,MDDatePicker
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingBottomButton
from kivy.core import text
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.garden.moretransitions import PixelTransition, RippleTransition, BlurTransition, RVBTransition
from kivy.storage.jsonstore import JsonStore
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker
from kivy.garden.mapview import MapSource
import os
import requests
from requests import *


KV = '''
#: import SwapTransition kivy.uix.screenmanager.SwapTransition
#: import RVBTransition kivy.garden.moretransitions.RVBTransition
#: import BlurTransition kivy.garden.moretransitions.BlurTransition

#: import MapView kivy.garden.mapview.MapView 

ScreenManager:
    id: scrn_manager
    # nav_drawer: nav_drawer
    transition: BlurTransition()
    Screen:
        name: 'well_scrn'
        FitImage:
            source: 'bg112.png'
        MDLabel:
            text: ' Welcome Buddy !!! '
            pos_hint: {'center_y':.7}
            halign: 'center'
            font_style: 'H3'
            font_name: 'COR' 
        MDFloatingActionButton:
            icon: 'arrow-down'
            pos_hint: {'center_x':.5 , 'center_y':.45}  
            user_font_size: '30sp'
            on_press:
                scrn_manager.current = "User_scrn" 
                scrn_manager.transition.direction = "up"
        MDProgressBar:
            value: 25
            pos_hint: {'center_y':.01}            

    Screen:
        name: 'User_scrn'
        dis_but: dis_but
        accountplus: accountplus
        username: username
        FitImage:
            source: 'bg112.png'
        MDLabel:
            text: 'Enter The Username'
            pos_hint: {'center_y':.76}
            halign: 'center'
            font_style: 'H3'
            font_name: 'COR'
        MDTextField:
            id: username
            hint_text: 'Enter the username'
            helper_text: 'Required'
            font_style: 'H5'
            font_name: 'COR'
            helper_text_mode: 'on_error'
            pos_hint: {'center_x':.5 , 'center_y':.56}
            size_hint_x: 0.7
            size_hint_y: 0.1
            icon_right: 'account'
            icon_right_color: self.theme_cls.primary_color
            required: True
        MDFloatingActionButton:
            id: accountplus
            icon: 'account-plus'
            pos_hint: {'center_x':.5 , 'center_y':.43}
            disabled: False 
            on_press: app.check_user()
        MDProgressBar:
            value: 50
            pos_hint: {'center_y':.01}
        MDFloatingActionButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':.1 , 'center_y':.1} 
            on_press:
                scrn_manager.current = "well_scrn"  
                scrn_manager.transition.direction = "right"
        MDFloatingActionButton:
            id: dis_but
            disabled: True
            icon: 'arrow-right'
            pos_hint: {'center_x':.9 , 'center_y':.1}
            on_press:
                scrn_manager.current = "Other_info" 
                scrn_manager.transition.direction = "left"

    Screen:
        name: 'Other_info'
        email: email
        accountplus2: accountplus2
        date_picker_text: date_picker_text
        password: password
        FitImage:
            source: 'bg112.png'
        MDLabel:
            text: 'Enter The Information'
            font_style: 'H4'
            halign: 'center'
            font_name: 'COR'
            pos_hint: {'center_x':.5 , 'center_y':.86}
        MDTextField:
            id: email
            hint_text: ' Email'
            helper_text: 'Required'
            font_style: 'H5'
            font_name: 'COR'
            helper_text_mode: 'on_error'
            pos_hint: {'center_x':.5 , 'center_y':.68}
            size_hint_x: 0.7
            size_hint_y: 0.1
            email: True
            icon_right: 'account'
            icon_right_color: self.theme_cls.primary_color
            required: True                
        MDTextField:
            id: password
            hint_text: 'Password'
            helper_text: 'Required'
            font_style: 'H5'
            font_name: 'COR'
            helper_text_mode: 'on_error'
            pos_hint: {'center_x':.5 , 'center_y':.58}
            size_hint_x: 0.7
            size_hint_y: 0.1
            email: True
            icon_right: 'key'
            password: True
            icon_right_color: self.theme_cls.primary_color
            required: True
        MDFillRoundFlatButton:
            id: date_picker_text
            text: 'Date Picker'
            pos_hint: {'center_x':.5 , 'center_y':.45}
            on_press: app.show_date_picker()

        MDFloatingActionButton:
            id: accountplus2
            icon: 'account-plus'
            pos_hint: {'center_x':.5 , 'center_y':.34}
            on_press: app.check_user2()
        MDProgressBar:
            value: 75
            pos_hint: {'center_y':.01}
        MDFloatingActionButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':.1 , 'center_y':.1} 
            on_press:
                scrn_manager.current = "User_scrn"  
                scrn_manager.transition.direction = "right"
        MDFloatingActionButton:
            id: dis_but2
            disabled: True
            icon: 'arrow-right'
            pos_hint: {'center_x':.9 , 'center_y':.1}
            on_press:
                app.save_data_using_json()
                scrn_manager.current = "main" 
                scrn_manager.transition.direction = "left"

    # Screen:
    #     name: 'OTP_scrn'
    #     dis_but3: dis_but3
    #     otp: otp
    #     FitImage:
    #         source: 'bg112.png'
    #     MDLabel:
    #         text: 'One Time Password'
    #         font_style: 'H4'
    #         halign: 'center'
    #         font_name: 'COR'
    #         pos_hint: {'center_x':.5 , 'center_y':.65}
    #     MDTextField:
    #         id: otp
    #         hint_text: ' Enter the OTP'
    #         helper_text: 'Sent to your email'
    #         font_style: 'H5'
    #         font_name: 'COR'
    #         helper_text_mode: 'on_focus'
    #         pos_hint: {'center_x':.5 , 'center_y':.5}
    #         size_hint_x: 0.6
    #         size_hint_y: 0.1
    #         icon_right: 'eye'
    #         icon_right_color: self.theme_cls.primary_color
    #         required: True                
    #     MDFloatingActionButton:
    #         icon: 'checkbox-marked-circle-outline'
    #         pos_hint: {'center_x':.5 , 'center_y':.34}
    #         on_press: app.check_otp()
    #     MDProgressBar:
    #         value: 100
    #         pos_hint: {'center_y':.01}
    #     MDFloatingActionButton:
    #         icon: 'arrow-left'
    #         pos_hint: {'center_x':.1 , 'center_y':.1} 
    #         on_press:
    #             scrn_manager.current = "Other_scrn"  
    #             scrn_manager.transition.direction = "right"
    #     MDFloatingActionButton:
    #         id: dis_but3
    #         disabled: True
    #         icon: 'arrow-right'
    #         pos_hint: {'center_x':.9 , 'center_y':.1}
    #         on_press:
    #             scrn_manager.current = "main" 
    #             scrn_manager.transition.direction = "left"        


    Screen:
        name: 'main'
        changing_text: changing_text
        FitImage:
            source: '—Pngtree—blue and purple gradient smoke_5494274.png'
        MDBoxLayout:
            padding: '8dp'
            orientation: 'vertical'
            spacing: '10dp'
            MDIconButton:   
                icon: 'menu'
                pos_hint: {'center_y':1}
                on_release:
                    nav_drawer.set_state("toggle")
            Widget:
        MDLabel:
            id: changing_text
            text: 'Welcome'
            halign: 'center'
            font_style: 'H4'
            font_name: 'COR'
            pos_hint: {'center_y':.62}
        MDLabel:
            text: 'Wanna to Trace IPs'
            halign: 'center'
            font_style: 'H5'
            font_name: 'COR'
            pos_hint: {'center_y':.52}
        MDRoundFlatButton:
            text: 'Get Started'
            pos_hint: {'center_x':.5 , 'center_y':.4}
            on_press: 
                scrn_manager.current = "main2"
                scrn_manager.transition = BlurTransition()
        MDNavigationDrawer: 
            id: nav_drawer
            MDBoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                padding: '8dp'
                MDIconButton:
                    icon: 'arrow-left'
                    pos_hint: {'center_x':.9}
                    size_hint_y: None
                    on_release: 
                        nav_drawer.set_state("close")
                Image: 
                    source: 'ip-img.png'
                MDLabel:
                    text: 'IP TRACER'
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1]
                    font_style: 'H5'
                    font_name: 'COR'
                    bold: True
                MDLabel:
                    text: ' By - Aditya Pawar '
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1]
                    font_style: 'H6'
                    font_name: 'COR'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            on_release:
                                scrn_manager.current = "profile"
                                nav_drawer.set_state("close")
                                scrn_manager.transition = RVBTransition()

                            IconLeftWidget:
                                icon: 'account'
                        OneLineIconListItem:
                            text: 'About'
                            on_release:
                                scrn_manager.current = "about"
                                nav_drawer.set_state("close")
                                scrn_manager.transition = SwapTransition()
                                scrn_manager.transition.direction = 'right'

                            IconLeftWidget:
                                icon: 'information'
                        OneLineIconListItem:
                            text: 'Settings'
                            on_release:
                                scrn_manager.current = "settings"
                                nav_drawer.set_state("close")
                                scrn_manager.transition = SwapTransition()
                                scrn_manager.transition.direction = 'right'
                            IconLeftWidget:
                                icon: 'cog'

                        OneLineIconListItem:
                            text: 'Exit'
                            on_release:
                                app.stop()
                            IconLeftWidget:
                                icon: 'location-exit'

    Screen:
        name: 'main2'
        ip: ip
        output: output
        dis_but4: dis_but4
        MDScreen:

            FitImage:
                source: 'hs.png'

            MDBoxLayout:
                orientation: 'vertical'
                spacing: '4dp'
                padding: '20dp'
                MDFillRoundFlatIconButton:
                    icon: 'arrow-left-thick'
                    text: 'Home'
                    on_press:
                        scrn_manager.current = "main"
                        scrn_manager.transition = BlurTransition()
                MDLabel:
                    id: output

            MDTextFieldRound:
                id: ip
                hint_text: 'Enter your ip'
                user_font_style: 'H3'
                size_hint_y: .067
                size_hint_x: .45
                pos_hint: {'center_x':.5 , 'center_y':.6}
                font_style: 'H4'
                font_name: 'COR'
                normal_color: app.theme_cls.primary_color

            MDFillRoundFlatIconButton:
                icon: 'cloud-search'
                text: "Trace"
                pos_hint: {'center_x':.5 , 'center_y':.5}
                on_release:
                    app.trace()
            
            MDFloatingActionButton:
                id: dis_but4
                disabled: True
                icon: 'google-maps'
                pos_hint: {'center_x':.5 , 'center_y':.1}
                on_press:
                    app.show_map()

            MDFloatingActionButtonSpeedDial:
                data: app.data_for_floating_action_btn
                root_button_anim: True
                pos_hint: {'center_x':.9 , 'center_y':.1}
                callback: app.callback



    Screen:
        id: profile
        name: 'profile'
        user_change: user_change
        email_change: email_change
        dob_change: dob_change
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '4dp'
            padding: '10dp'
            MDIconButton:
                icon: 'arrow-left'
                size_hint_y: None
                pos_hint: {'center_y':1}
                on_release: 
                    scrn_manager.current = "main"
                    scrn_manager.transition = RVBTransition()
            Widget:
        Image:
            source: 'adit.png'
            size_hint_x: .35
            size_hint_y: .35
            pos_hint: {'center_x':.5 , 'center_y':.76}
        MDLabel:
            id: user_change
            text: ' Username :  '
            font_style: 'H5'
            font_name: 'COR'
            pos_hint: {'center_x':.289 , 'center_y':.5}
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
        MDTextField:
            readonly: True
            id: user_change
            text: ''
            font_style: 'H4'
            font_name: 'COR'
            pos_hint: {'center_x':.7 , 'center_y':.5}
            size_hint_x: .4
        MDLabel:
            text: 'Email :  '
            font_style: 'H5'
            font_name: 'COR'
            pos_hint: {'center_x':.289 , 'center_y':.375}
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
        MDTextField:
            id: email_change
            text: ''
            readonly: True
            font_style: 'H4'
            font_name: 'COR'
            pos_hint: {'center_x':.7 , 'center_y':.375}
            size_hint_x: .4
        MDLabel:
            text: 'Date of Birth :  '
            font_style: 'H5'
            font_name: 'COR'
            pos_hint: {'center_x':.289 , 'center_y':.25}
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
        MDTextField:
            id: dob_change
            text: ''
            readonly: True
            font_style: 'H4'
            font_name: 'COR'
            pos_hint: {'center_x':.7 , 'center_y':.25}
            size_hint_x: .4        
        MDFloatingActionButton:
            icon: 'lead-pencil'
            pos_hint: {'center_x':.89 , 'center_y':.1}
            on_press: app.change_data()

    Screen:
        name: 'about'
        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '10dp'
            MDIconButton:
                icon: 'arrow-left'
                size_hint_y: None
                on_release:
                    scrn_manager.current = 'main'
                    scrn_manager.transition = SwapTransition()
                    scrn_manager.transition.direction = 'right' 
            MDLabel:
                text: 'Developer -> Aditya Pawar ( Cyber_adi ) '
                font_style: 'H4'
                font_name: 'COR'
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]              
            MDLabel:
                text: 'Designer -> Aditya pawar'
                font_style: 'H4'
                font_name: 'COR'
                halign: 'center' 
                size_hint_y: None
                height: self.texture_size[1]     
            MDLabel:
                text: 'Email id -> cybergeek563@gmail.com'
                font_style: 'H4'
                font_name: 'COR'
                halign: 'center' 
                size_hint_y: None
                height: self.texture_size[1]     
            MDLabel:
                text: 'Instagram username -> adityapawar4914'
                font_style: 'H4'
                font_name: 'COR'
                halign: 'center' 
                size_hint_y: None
                height: self.texture_size[1]     

            MDLabel:
                text: 'Github Profile -> github.com/aditya12-cyber'
                font_style: 'H4'
                font_name: 'COR'
                halign: 'center' 
                size_hint_y: None
                height: self.texture_size[1]                         
            MDLabel:
                text: 'This app is written in python language using the KIVYMD and KIVY module or library'
                font_style: 'H4'
                font_name: 'COR'
                halign: 'center' 
                size_hint_y: None
                height: self.texture_size[1]   
            Widget:

    Screen:
        name: 'settings'
        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '10dp'
            MDIconButton:
                icon: 'arrow-left'
                size_hint_y: None
                on_release:
                    scrn_manager.current = 'main'
                    scrn_manager.transition = SwapTransition()
                    scrn_manager.transition.direction = 'right'
            MDFloatLayout:

                MDLabel:
                    text: 'Theme Changer'
                    font_style: 'H3'
                    font_name: 'COR'
                    pos_hint: {'center_x':.5 , 'center_y':.7}
                    halign: 'center'

                MDFloatingActionButton:
                    icon: 'apple-icloud'
                    pos_hint: {'center_x':.5 , 'center_y':.5}
                    elevation_normal: 12
                    on_press:
                        app.theme()


'''


# OTP Info

# digits = "0123456789"
# OTP = ""

# for i in range(6):
#     OTP += digits[math.floor(random.random()*10)]

# otp = f" Hello User Its DEV \n Your OTP is {OTP}"
# msg = otp

# # Close the otp function

class Item(OneLineListItem):
    divider = None
    source = StringProperty()


class IpApp(MDApp):

    data_for_floating_action_btn = {
        "Save" : "content-save"
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def build(self):

        self.theme_cls.theme_style = "Light"
        self.kv = Builder.load_string(KV)

        return self.kv

    def username_changer(self):
        self.root.ids.changing_text.text = f"{self.store.get('UserInfo')['name']}"
        self.root.ids.user_change.text = f"{self.store.get('UserInfo')['name']}"
        self.root.ids.email_change.text = f"{self.store.get('UserInfo')['email']}"
        self.root.ids.dob_change.text = f"{self.store.get('UserInfo')['DOB']}"


    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.root.current = 'main'

        except KeyError:
            self.root.current = 'well_scrn'

    def save_data_using_json(self):
        self.store.put('UserInfo', name=self.user_text , email = self.email_text , password = self.pass_text , DOB = self.date_of_birth )
        self.username_changer()

    def theme(self):

        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def on_save(self , instance , value , date_range):
        print(instance , value , date_range)

        self.date_of_birth = str(value)

        self.root.ids.date_picker_text.text = str(value)

    def on_cancel(self , instance , value):
        print("cancel")

    def show_date_picker(self):

        self.picker = MDDatePicker(year = 2000 , month = 1 , day = 1)
        self.picker.bind(on_save = self.on_save , on_cancel = self.on_cancel)
        self.picker.open()
    

    def check_user(self):

        self.user_text = self.root.ids.username.text
        username_check_false = True
        self.dialog = None

        try:
            int(self.user_text)
        except:
            username_check_false = False
        if username_check_false or self.user_text.split() == []:

            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Invalid Username",
                    text="Please Enter a Valid Username",
                    buttons=[
                        MDFlatButton(
                            text="RETRY",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_press=self.close_dialog,
                        ),
                    ]
                )
            self.dialog.open()

        else:
            print("all ok")
            self.root.ids.dis_but.disabled = False
            self.root.ids.accountplus.icon = "account-check"

    def close_dialog(self, *kwargs):

        self.dialog.dismiss()

    def check_user2(self):

        self.email_text = self.root.ids.email.text
        self.pass_text = self.root.ids.password.text

        user_input_false = True

        try:
            int(self.email_text)
        except:
            user_input_false = False

        if user_input_false or self.email_text.split() == [] or self.pass_text.split() == []:

            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Invalid Data",
                    text="Enter Valid Email and password",
                    buttons=[
                        MDFlatButton(
                            text="RETRY",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_press=self.close_dialog2,
                        ),
                    ]
                )
            self.dialog.open()

        else:
            self.root.ids.dis_but2.disabled = False
            self.root.ids.accountplus2.icon = "account-check"
            
            

    def close_dialog2(self, *kwargs):

        self.dialog.dismiss()

    # def send_otp(self):

    #     self.s = smtplib.SMTP('smtp.gmail.com' , 567)
    #     self.s.starttls()

    #     self.s.login('cybergeek563@gmail.com' , 'qwert123Ad$&?')
    #     emailid = self.root.ids.email.text

    #     self.s.sendmail("One Time Password" , emailid , msg)

    # def check_otp(self):

    #     self.otp = self.root.ids.otp.text

    #     if (self.otp == OTP):

    #         self.root.ids.dis_but3.disabled = False

    #     else:
    #         print("error")

    def trace(self):

        self.dialog = None

        self.ip_adrr = self.root.ids.ip.text

        print(self.ip_adrr)

        self.response = requests.get(f"http://ip-api.com/json/{self.ip_adrr}").json()
        print(self.response)
        self.stat = self.response['status']
        self.country = self.response['country']
        self.countrycode = self.response['countryCode']
        self.region = self.response['region']
        self.regionname = self.response['regionName']
        self.city = self.response['city']
        self.zip = self.response['zip']
        self.latitude = self.response['lat']
        self.longitude = self.response['lon']
        self.timezone = self.response['timezone']
        self.isp = self.response['isp']
        self.org = self.response['org']
        self.ip = self.response['query']
        
        if self.ip_adrr.split() == []:

            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Error",
                    text="Enter the IpV4 address",
                    buttons=[
                        MDFlatButton(
                            text="RETRY",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_press=self.close_dialog2,
                        ),
                    ]
                )
            self.dialog.open()
        else:
            self.root.ids.dis_but4.disabled = False

            try:
                if not self.dialog: 
                    self.dialog = MDDialog(
                        title="IP Tracer",
                        type="simple",
                        text=f" IP Address -> {self.ip} \n Status -> {self.stat} \n City -> {self.city} \n Country -> {self.country} \n Region -> {self.region} \n Region Name -> {self.regionname} \n Country Code -> {self.countrycode} \n Latitude -> {self.latitude} \n Longitude -> {self.longitude} \n Zip Code -> {self.zip} \n Time Zone -> {self.timezone} \n Internet Service Provider -> {self.isp} \n Organisation -> {self.org} \n",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                                on_press= self.close_dialog3,
                            ),
                        ]
                    )
                self.dialog.open()
            except KeyError:
                print('error')

    def close_dialog3(self, *kwargs):

        self.dialog.dismiss()

    def show_map(self):
        self.map_scrn = MDScreen( name = "Map_scrn")
        self.map_view = MapView(
            lat = self.latitude,
            lon = self.longitude,
            zoom = 25,
            double_tap_zoom = True,
        )
        self.map_marker = MapMarker(
            lat = self.latitude,
            lon = self.longitude,
            source = "map_marker.png"
        )
        self.map_view.add_widget(self.map_marker)
        self.map_scrn.add_widget(self.map_view)
        self.root.add_widget(self.map_scrn)

        self.root.current = "Map_scrn"

        print(MapSource.providers.keys())

    def close_map(self):
        print("working")

    def callback(self, instance):
        print('callback')
        icon = instance.icon
        # if you want check button, use
        if isinstance(instance, MDFloatingBottomButton):
            
            checking_file = os.path.isfile("result_data.txt")

            if checking_file == True:

                with open('result_data.txt' , 'a') as f:
                
                    f.write(f"\n \n     IP_address you entered -> {self.response['query']} \n \n   Status - > { self.response['status'] } \n   Country - > { self.response['country'] } \n  CountryCode - > { self.response['countryCode'] } \n  City - > { self.response['city'] } \n  Region - > { self.response['region'] } \n  RegionName - > { self.response['regionName'] } \n  Zip - > { self.response['zip'] } \n  latitude - > { self.response['lat'] } \n  longitude - > { self.response['lon'] } \n  Timezone - > { self.response['timezone'] } \n  ISP - > { self.response['isp'] } \n  Organisation - > {self.response['org']} \n  IP_Address - > {self.response['query']} \n  \n")

            elif checking_file == False:

                with open('result_data.txt' , 'a') as f:

                    f.write(f"\n \n     IP_address you entered -> {self.response['query']} \n \n   Status - > { self.response['status'] } \n   Country - > { self.response['country'] } \n  CountryCode - > { self.response['countryCode'] } \n  City - > { self.response['city'] } \n  Region - > { self.response['region'] } \n  RegionName - > { self.response['regionName'] } \n  Zip - > { self.response['zip'] } \n  latitude - > { self.response['lat'] } \n  longitude - > { self.response['lon'] } \n  Timezone - > { self.response['timezone'] } \n  ISP - > { self.response['isp'] } \n  Organisation - > {self.response['org']} \n  IP_Address - > {self.response['query']} \n  \n")

    def change_data(self):

        self.snbar = Snackbar(
            text = "[color=#ddbb34]You Can Change your data !!!! [/color]"

        )
        self.snbar.open()
        
        self.root.ids.user_change.readonly = False
        self.root.ids.email_change.readonly = False

if __name__ == "__main__":
    LabelBase.register(name="COR", fn_regular="CarterOne-Regular.ttf")
    IpApp().run()