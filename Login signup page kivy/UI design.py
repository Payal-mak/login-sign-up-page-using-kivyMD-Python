from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Set window background color

KV = '''
ScreenManager:
    LoginScreen:
    SignupScreen:

<LoginScreen>:
    name: "login"

    FloatLayout:
        Image:
            source: "D:/SEM 3 Subjects/Python/LHC2/login background.jpg" 
            allow_stretch: True
            keep_ratio: False
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: 30
            spacing: 20
            size_hint: None, None
            size: 400, 400
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "Login"
                font_style: "H4"
                halign: "center"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: username
                hint_text: "Enter Username"
                icon_right: "account"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8

            MDTextField:
                id: password
                hint_text: "Enter Password"
                icon_right: "lock"
                password: True
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8

            MDRaisedButton:
                text: "Login"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                on_release: app.login(username.text, password.text)

            MDFlatButton:
                text: "Don't have an account? Sign Up"
                pos_hint: {"center_x": 0.5}
                on_release: app.switch_to_signup()

<SignupScreen>:
    name: "signup"

    FloatLayout:
        Image:
            source: "D:/SEM 3 Subjects/Python/LHC2/login background.jpg"
            allow_stretch: True
            keep_ratio: False

        MDBoxLayout:
            orientation: 'vertical'
            padding: 30
            spacing: 20
            size_hint: None, None
            size: 400, 400
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "Sign Up"
                font_style: "H4"
                halign: "center"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: signup_username
                hint_text: "Enter Username"
                icon_right: "account"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8

            MDTextField:
                id: signup_email
                hint_text: "Enter Email"
                icon_right: "email"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8

            MDTextField:
                id: signup_password
                hint_text: "Enter Password"
                icon_right: "lock"
                password: True
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8

            MDRaisedButton:
                text: "Sign Up"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                on_release: app.signup(signup_username.text, signup_email.text, signup_password.text)

            MDFlatButton:
                text: "Already have an account? Login"
                pos_hint: {"center_x": 0.5}
                on_release: app.switch_to_login()
'''
