import sqlite3
from sqlite3 import Error
import asyncio
from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class AppClass(Widget):
    def __init__(self, **kwargs):
        super(AppClass, self).__init__(**kwargs)


class List(RecycleView):
    def __init__(self, **kwargs):
        super(List, self).__init__(**kwargs)
        self.load_data()

    def load_data(self):
        self.data = []
        print('load_data')
        cursor.execute("SELECT * FROM tasks")
        for task in cursor.fetchall():
            print(task[0])
            self.data.append({'text': task[0]})

    def load_items(self, *args):
        """Load list items from store.json"""
        store = JsonStore('store.json')
        list_items = []
        for item in store:
            list_items.append({'text': item})
        self.data = list_items


class AddTaskPopup(Popup):
    def __init__(self, **kwargs):
        super(AddTaskPopup, self).__init__(**kwargs)

    def add_task(self):
        cursor.execute("INSERT INTO tasks VALUES (:title)", {'title': self.ids.text_input_add_task.text})
        connect.commit()

        # app.list.load_data()

        self.dismiss()


class Header(BoxLayout):
    pass


class Footer(BoxLayout):
    pass


class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class NewScreen(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


class TooDooshApp(App):
    def build(self):
        self.list = List()


if __name__ == '__main__':
    try:
        connect = sqlite3.connect('toodoosh.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE if not exists tasks( title TEXT )""")
        connect.commit()

        app = TooDooshApp()
        app.run()

    except Error:
        print(Error)
    finally:
        connect.close()