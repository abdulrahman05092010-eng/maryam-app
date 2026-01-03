from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from brain import respond
from voice import speak

CURRENT_PERSON = "user"

class Maryam(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.output = Label(
            text="Maryam is here.",
            font_size=22,
            size_hint_y=0.4
        )

        self.input = TextInput(
            hint_text="Say something…",
            multiline=False,
            size_hint_y=0.3
        )

        btn = Button(
            text="Speak",
            size_hint_y=0.3
        )
        btn.bind(on_press=self.talk)

        layout.add_widget(self.output)
        layout.add_widget(self.input)
        layout.add_widget(btn)

        return layout

    def talk(self, _):
        text = self.input.text
        if not text:
            return
        reply = respond(text, CURRENT_PERSON)
        self.output.text = reply
        speak(reply)
        self.input.text = ""

if __name__ == "__main__":
    Maryam().run()
