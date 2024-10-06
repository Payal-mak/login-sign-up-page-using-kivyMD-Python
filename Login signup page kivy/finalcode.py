import sqlite3
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = (0.95, 0.95, 0.95, 1)

DB_NAME = 'users.db'

# Create a database for storing user credentials
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

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

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class LoginApp(MDApp):
    dialog = None

    def build(self):
        create_database()  # Create the user database
        self.theme_cls.primary_palette = "Blue"  
        self.theme_cls.theme_style = "Light"  
        return Builder.load_string(KV)

    def switch_to_signup(self):
        self.root.current = 'signup'

    def switch_to_login(self):
        self.root.current = 'login'

    def login(self, username, password):
        # Ensure that fields are not empty
        if not username or not password:
            self.show_dialog("Error", "Please fill in all fields.")
            return

        # Connect to the database to verify credentials
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        # Check if user exists and password matches
        if user is None:
            self.show_dialog("Error", "Username not found.")
        elif user[3] == password:  # Password stored as plain text, so simple comparison
            self.show_dialog("Login", "Login successful")
        else:
            self.show_dialog("Error", "Incorrect password.")

    def signup(self, username, email, password):
        # Ensure that all fields are filled in
        if not username or not email or not password:
            self.show_dialog("Error", "Please fill in all fields.")
            return

        # Insert user data into the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                           (username, email, password))  # Store password as plain text
            conn.commit()
            self.show_dialog("Sign Up", "Sign up successful")
        except sqlite3.IntegrityError:
            self.show_dialog("Error", "Username already exists.")
        finally:
            conn.close()

    def show_dialog(self, title, message):
        # Display dialog messages
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=message,
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.title = title
        self.dialog.text = message
        self.dialog.open()

if __name__ == "__main__":
    LoginApp().run()
