from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


class NameListApp(App):
    """ NameListApp is a Kivy App for displaying names from a list as separate Labels """

    def __init__(self, **kwargs):
        """ construct main app """
        super().__init__(**kwargs)
        self.names = ["Big Ben", "Large Larry", "Huge Hugh (Jackman)", "Massive Monty", "Bigger Ben"]

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Name List App"
        self.root = Builder.load_file('name_list_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """ create Labels from names list and add them to Kivy GUI """
        for name in self.names:
            new_label = Label(text=name, id=name, font_size=50)
            self.root.ids.name_entries.add_widget(new_label)


NameListApp().run()
