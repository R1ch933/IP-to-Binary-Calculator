import kivy
from kivy.app import App
from kivy.uix.label import Label
import PIL
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import re


class Calc_Box(Widget):
    input = ObjectProperty(None)

    def Binary(self, ip):
        ip = ip
        bits = [128, 64, 32, 16, 8, 4, 2, 1]
        if ip <= 255 and ip >= 0:
            for bit_scan in bits:
                if ip >= bit_scan:
                    ip -= bit_scan
                    self.input.text += '1'
                elif ip < bit_scan:
                    self.input.text += '0'
        elif ip > 255 or ip < 0:
            self.input.text = "ERROR"
    def clear(self):
        input = ObjectProperty(None)
        self.input.text = ''

    def btn(self):
        input = ObjectProperty(None)
        # turns the input into a list
        while '.' in self.input.text:
            self.input.text = self.input.text.replace(".", "")
        ip_address = self.input.text
        if len(ip_address) == 12:
            ip_address = re.findall('...', ip_address)
            ip_2 = []
            for byte in ip_address:
                byte = int(byte)
                ip_2.append(byte)
            ip_address = ip_2
            print(ip_address)
            self.input.text = ''
            for ip in ip_address:
                self.Binary(ip)
                self.input.text += '.'
        elif len(ip_address) != 12:
            self.input.text = "Please input a 12 digit ip address"

class Calc(App):
    def build(self):
        return Calc_Box()


if __name__ == "__main__":
    Calc().run()
