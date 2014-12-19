import requests
import _thread
from urllib.request import urlopen
from bs4 import BeautifulSoup
from dataBase import addPage


class Konoshtip:
    biten = []

    def __init__(self, URL):
        self.URL = URL

    def bite(self):
        allTheRubish = requests.get(self.URL, verify=False)
        soup = BeautifulSoup(allTheRubish.content)

        for link in soup.find_all('a'):
            try:
                if "http" in link.get('href') and not link.get('href') in Konoshtip.biten:
                    soup = BeautifulSoup(urlopen(link.get('href')))
                    html = soup.contents[0]
                    if "html" == html:
                        html = "HTML5"
                    elif "html4" in html:
                        html = "HTML4"
                    elif "xhtml1" in html:
                        html = "XHTML1"
                    description = soup.find(attrs={"property": "og:description"}).get("content")
                    Konoshtip.biten.append(link.get('href'))
                    addPage(link.get('href'), soup.title.string, html, description)
                    print(link.get('href') + "||" + soup.title.string + "||" + html + "||" + description)
                    _thread.start_new_thread(biteAgain, (link.get('href'),))
            except:
                pass


def biteAgain(URL):
    allTheRubish = requests.get(URL, verify=False)
    soup = BeautifulSoup(allTheRubish.content)
    print("AAA")
    for link in soup.find_all('a'):
            try:
                if "http" in link.get('href') and not link.get('href') in Konoshtip.biten:
                    soup = BeautifulSoup(urlopen(link.get('href')))
                    html = soup.contents[0]
                    if "html" == html:
                        html = "HTML5"
                    elif "html4" in html:
                        html = "HTML4"
                    elif "xhtml1" in html:
                        html = "XHTML1"
                    description = soup.find(attrs={"property": "og:description"}).get("content")
                    Konoshtip.biten.append(link.get('href'))
                    addPage(link.get('href'), soup.title.string, html, description)
                    print(link.get('href') + "||" + soup.title.string + "||" + html + "||" + description)
                    _thread.start_new_thread(biteAgain, (link.get('href'),))

            except:
                pass
    quit()


def main():
    strahil = Konoshtip("http://www.computerhope.com/os.htm")
    strahil.bite()


if __name__ == "__main__":
    main()
