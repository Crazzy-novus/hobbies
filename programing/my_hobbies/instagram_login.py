from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp


class InstagramLoginApp(MDApp):
    def build(self):
        Window.size = (300, 400)
        return Builder.load_file("instagram_login.kv")


if __name__ == "__main__":
    InstagramLoginApp().run()


