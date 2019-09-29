from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles to kilometres from user input """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root


ConvertMilesApp().run()
