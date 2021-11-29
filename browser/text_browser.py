# from sys import argv
from os import mkdir
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Style, Fore


class TextBasedBrowser:
    def __init__(self, directory):
        self.tabs = {}
        self.directory = directory
        self.cache = deque()
        try:
            mkdir(self.directory)
        except FileExistsError:
            pass

    def cache_tab(self, name, content):
        if not self.tabs.get(name[:-4]):
            with open(f'{self.directory}/{name[:-4]}.txt', 'w') as tab:
                tab.write(content)
            self.tabs[name[:-4]] = f'{self.directory}/{name[:-4]}.txt'
            self.cache.appendleft(self.tabs[name[:-4]])

    def open_tab(self, url):
        with open(self.tabs[url], 'r') as tab:
            return tab.read()

    @staticmethod
    def get_tags(content):
        tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        soup = BeautifulSoup(content, 'html.parser').body.descendants
        page = ""
        for descendant in soup:
            if descendant.name in tags:
                if descendant.name == 'a':
                    page += Fore.BLUE + descendant.get_text().strip()
                else:
                    page += Style.RESET_ALL + descendant.get_text().strip()
        return page

    def check_url(self, url):
        try:
            if url.startswith('http'):
                return self.request(url)
            return self.request('https://' + url)
        except requests.exceptions.RequestException:
            return 'Something went wrong with connection'

    def request(self, url):
        request = requests.get(url)
        clean_page = self.get_tags(request.content)
        self.cache_tab(url[8:], clean_page)
        return clean_page

    def back(self):
        if len(self.cache) == 1:
            return 'History is Empty'
        try:
            with open(self.cache.pop(), 'r') as cached:
                return cached.read()
        except FileNotFoundError:
            return 'Error.'
        except IndexError:
            return 'History is already empty'


def main(folder='sites'):
    browser = TextBasedBrowser(folder)
    while True:
        print(Fore.LIGHTYELLOW_EX + '')
        url = input('Please, input site here:\n> ')
        if '.' in url:
            print(browser.check_url(url))
        elif url in browser.tabs:
            print(browser.open_tab(url))
        elif url == 'back':
            print(browser.back())
        elif url == 'exit':
            break
        else:
            print('Error')


if __name__ == '__main__':
    main()
