import requests
import lista
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

class Temperature(object):
    def __init__(self, place):
        self.place = place

    def __repr__(self):
        temperature = self.weather()
        return str(f"Temperatura no seu estado {temperature} in {self.place}")

    def weather(self):
        url = f"https://www.google.com/search?&q=weather in {self.place}"
        req = requests.get(url)
        scrap = BeautifulSoup(req.text, "html.parser")
        temperature = scrap.find("div", class_="BNeawe").text
        return temperature

linha ='-'*57

x = datetime.now()
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
print(linha)
print("Hoje é", dias[x.weekday()])
print("Data",x.day,"/", x.month,"/", x.year)
print("Horas",x.hour ,":",x.minute,":",x.second)

if __name__ == "__main__":
    print(linha)
    print(Temperature("Am \n"))
    print(Temperature("Sp \n"))
    print(Temperature("Rj \n"))
    print(Temperature("Rn \n"))
    print(linha)
