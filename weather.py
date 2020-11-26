import requests
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


if __name__ == "__main__":
    print(Temperature("Brasilia \n"))
    print(Temperature("Sao_paulo \n"))
    print(Temperature("Rio_de_janeiro \n"))
