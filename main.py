from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia


Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        # Get user query from text input
        user_query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and list of image urls
        page = wikipedia.page(user_query)
        image_links = page.images
        # Download the image
        link = image_links[0]
        req = requests.get(link)
        image_path = 'files/image.jpg'
        with open(image_path, 'wb') as file:
            file.write(req.content)
        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = image_path


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
