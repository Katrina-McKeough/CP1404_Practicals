from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM_CONVERSION = 1.60934  # Conversion factor is 1.60934 km/ 1 mile


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles to kilometres from user input """

    output_text = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation from button press, output result to label widget"""
        result = value * MILES_TO_KM_CONVERSION
        self.output_text = str(result)


ConvertMilesApp().run()
