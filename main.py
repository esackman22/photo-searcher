from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia


Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):
        # Get user query from text input
        user_query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and list of image urls
        page = wikipedia.page(user_query, auto_suggest=False)
        image_links = page.images
        link = image_links[0]
        return link

    def download_image(self):
        link = self.get_image_link()
        headers = {'User-Agent' : 'photo_searcher_bot/1.0 (eks3333@gmail.com)'}
        req = requests.get(link, headers=headers)
        image_path = 'files/image.jpg'
        with open(image_path, 'wb') as file:
            file.write(req.content)

        return image_path

    def set_image(self):

        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
