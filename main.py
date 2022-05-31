from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("screen.kv")

class MyApp(App):
    def build(self):
        return GUI

    def on_start(self):        
        self.root.ids['moeda1'].text = f"Dólar R${self.get_quote('USD')}"
        self.root.ids['moeda2'].text = f"Euro R${self.get_quote('EUR')}"
        self.root.ids['moeda3'].text = f"Bitcoin R${self.get_quote('BTC')}"
        self.root.ids['moeda4'].text = f"Ethereum R${self.get_quote('ETH')}"

    def get_quote(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        request = requests.get(link)
        res_json = request.json()
        bid = res_json[f"{moeda}BRL"]["bid"]
        # print(request.json())
        return bid

MyApp().run()