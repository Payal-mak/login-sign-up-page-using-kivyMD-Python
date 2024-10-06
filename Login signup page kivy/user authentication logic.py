from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

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
