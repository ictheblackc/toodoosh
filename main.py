from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore

class CreateListItemForm(Widget):
    pass

class List(RecycleView):
    def __init__(self, **kwargs):
        super(List, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

    def load_items(self, *args):
        """Load list items from store.json"""
        store = JsonStore('store.json')
        list_items = []
        for item in store:
            list_items.append({'text': item})
        self.data = list_items

class Header(BoxLayout):
    pass

class Footer(BoxLayout):
    pass

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class TooDooshApp(App):
    def build(self):
        """"""

if __name__ == '__main__':
    app = TooDooshApp()
    app.run()
