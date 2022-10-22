from colorama import init
init()
from colorama import Fore, Back, Style
from fake_useragent import UserAgent

from ..support.args import parser

import asyncio
import socket
import aiohttp
import shutil

class Crawl:
    def __init__(self):
        args = parser()
        self.domain = args.domain
        
    #get terminal size for pretty printing
    def size():
        return shutil.get_terminal_size().columns
    
    #get random headers
    def client_headers(self):
        ua = UserAgent()
        header = {'User-Agent': str(ua.random)}
        return header
    
    #get headers from domain
    async def target_headers(self):
        size = Crawl.size()
        domain = self.domain
        if domain.startswith('https://') == False and domain.startswith('http://') == False:
            print(Fore.RED + '[-] Error: Protocol not specified (http or https)' + Style.RESET_ALL)
            exit()
        try:    
            async with aiohttp.ClientSession(headers=Crawl.client_headers(self)) as session:
                async with session.get(domain) as response:
                    headers = response.headers
        except:
            print(Fore.RED + '[-] Error: Domain not found' + Style.RESET_ALL)
            exit()
        print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'HEADERS'.center(size) + '\n' + '-' * size + Style.RESET_ALL)     
        for key, value in headers.items():
            print(Fore.GREEN + f'[+]' + Fore.MAGENTA + f' {key}: ' + Style.RESET_ALL + f'{value}')
    
    async def sitemap(self):
        size = Crawl.size()
        domain = self.domain
        async with aiohttp.ClientSession(headers=Crawl.client_headers(self)) as session:
            async with session.get(domain + '/sitemap.xml') as response:
                if response.status == 200:
                    sitemap = await response.text()
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'SITEMAP.XML'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(sitemap)
                else:
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'ROBOTS.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(Fore.RED + '\n[-] Error: Sitemap.xml not found\n' + Style.RESET_ALL)
                    
    
    #get txts from domain
    async def txts(self):
        domain = self.domain
        size = Crawl.size()
        async with aiohttp.ClientSession(headers=Crawl.client_headers(self)) as session:
            
            #get robots.txt
            async with session.get(domain + '/robots.txt') as response:
                if response.status == 200:
                    robots = await response.text()
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'ROBOTS.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(robots)
                else:
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'ROBOTS.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(Fore.RED + '\n[-] Error: Robots.txt not found\n' + Style.RESET_ALL)
            
            #get security.txt
            async with session.get(domain + '/security.txt') as response:
                if response.status == 200:
                    security = response.text()
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'SECURITY.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(response)
                else:
                    async with session.get(domain + '/.well-known/security.txt') as response:
                        if response.status == 200:
                            security = await response.text()
                            print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'SECURITY.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                            print(security)
                        else:
                            print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'SECURITY.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                            print(Fore.RED + '\n[-] Error: Security.txt not found\n' + Style.RESET_ALL)
            
            #get humans.txt
            async with session.get(domain + '/humans.txt') as response:
                if response.status == 200:
                    humans = await response.text()
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'HUMANS.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(humans)
                else:
                    print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'HUMANS.TXT'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
                    print(Fore.RED + '\n[-] Error: Humans.txt not found\n' + Style.RESET_ALL)
            
if __name__ == '__main__':
    Crawl()