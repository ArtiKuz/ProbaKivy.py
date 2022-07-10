import math
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.clearcolor = [.4,.4,.4]

class TangensApp(App):
    def build(self):

        self.tiD = TextInput(background_color=[.9, .9, .9], font_size=30, halign="center")
        self.tid = TextInput(background_color=[.9, .9, .9], font_size=30, halign="center")
        self.til = TextInput(background_color=[.9, .9, .9], font_size=30, halign="center")
        self.tiv = TextInput(background_color=[.8, .8, .8], readonly=True, font_size=35, halign="center")

        gl = GridLayout(rows=5, cols=2, padding=3, spacing=1)

        gl.add_widget(TextInput(text="D - больший диаметр", background_color=[.7, .7, .7], readonly=True, font_size=25, halign="center", foreground_color = [.1,.1,.1]))
        gl.add_widget(self.tiD)
        gl.add_widget(TextInput(text="d - меньший диаметр", background_color=[.7, .7, .7], readonly=True, font_size=25, halign="center", foreground_color = [.1,.1,.1]))
        gl.add_widget(self.tid)
        gl.add_widget(TextInput(text="l - длина", background_color=[.7, .7, .7], readonly=True, font_size=25, halign="center", foreground_color = [.1,.1,.1]))
        gl.add_widget(self.til)
        gl.add_widget(TextInput(text="Ответ:", background_color=[.7, .7, .7], readonly=True, font_size=30, halign="center", foreground_color = [.1,.1,.1]))
        gl.add_widget(self.tiv)
        gl.add_widget(Button(text="Сброс", on_press=self.sbros, font_size=30, color=[.9,.9,.9]))
        gl.add_widget(Button(text="Вывод", on_press=self.result, font_size=30, color=[.9,.9,.9]))

        return gl

    def result(self, instance):
        try:
            tgA = (float(self.tiD.text) - float(self.tid.text)) / (2 * float(self.til.text))
            x = math.atan(tgA)
            y = math.degrees(x)
            i = str(round(y, 2))
            self.tiv.text = i
        except ValueError:
            pass

    def sbros(self, instance):
        self.tiD.text = ""
        self.tid.text = ""
        self.til.text = ""
        self.tiv.text = ""

if __name__ == "__main__":
    TangensApp().run()

















