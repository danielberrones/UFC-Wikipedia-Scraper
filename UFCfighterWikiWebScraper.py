## A tool to extract data from Wikipedia for UFC Fighters
## Created by Daniel Berrones [email: Daniel.A.Berrones@gmail.com]


import requests
from bs4 import BeautifulSoup


# example url = 'https://en.wikipedia.org/wiki/Jorge_Masvidal'


class Fighter:
    def __init__(self, url):
        self.url = url

    def searchWeb(self):
        #returns soup object
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, 'lxml')

        #searches HTML tree for table
        self.parsedText = self.soup.find_all("table", class_="wikitable")

        #finds index where fighter name is in URL
        self.truncatedTitle = self.url.split('/')[4]

        #saves text in file with fighter name
        with open("ENTER\YOUR\FILE\PATH\HERE\{}.txt".format(self.truncatedTitle), "w") as f:
            for self.parsed in self.parsedText[1].text:
                f.write(self.parsed)

        #success statement
        return "It was a success!"

def main():
    gamebred = Fighter(input("Type URL: "))
    print(gamebred.searchWeb())


if __name__ == "__main__":
    main()
