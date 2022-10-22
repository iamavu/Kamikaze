from colorama import init
init()
from colorama import Fore, Back, Style
from fake_useragent import UserAgent

from ..support.args import parser

import asyncio
import shutil
import aiohttp

CURSOR_UP = '\033[F'
ERASE_LINE = '\033[K'

class Directory:
    
    def __init__(self):
        args = parser()
        self.domain = args.domain
        self.redirects = args.redirects
        self.threads = args.threads
        self.sites = []
        
    #get terminal size for pretty printing
    def size():
        return shutil.get_terminal_size().columns
    
    #get random headers
    def client_headers(self):
        ua = UserAgent()
        header = {'User-Agent': str(ua.random)}
        return header
    
    async def check(self, session, domain, word):
        sites = []
        redirects = self.redirects
        try:
            async with session.get(domain + '/' + word, allow_redirects=redirects, headers=Directory.client_headers(self), ssl=False) as response:
                if response.status == 200:
                    self.sites.append(domain + '/' + word)
                    print(response.status)
                    print(Fore.GREEN + f'[{response.status}]' + Style.RESET_ALL + f' {domain}/{word}')
                else:
                    pass 
        except Exception as e:
            print(Fore.RED + '[!]' + Style.RESET_ALL + f' Exception occurred while checking {domain}/{word}: ' + str(e))   
    
    async def enumdir(self):
        wordlist = []
        domain = self.domain
        threads = self.threads
        size = Directory.size()
        with open('modules/support/dir-dict.txt', 'r') as file:
            for word in file:
                word = word.strip()
                wordlist.append(word)
        conn = aiohttp.TCPConnector(limit=threads)
        async with aiohttp.ClientSession(connector=conn) as session:
            tasks = []
            print(Fore.GREEN + Style.BRIGHT + '-' * size + '\n' + 'DIRECTORIES'.center(size) + '\n' + '-' * size + Style.RESET_ALL)
            for word in wordlist:
                tasks.append(asyncio.create_task(Directory.check(self, session, domain, word)))
                print(Fore.GREEN + '[+]' + Style.RESET_ALL + f' Request sent : {wordlist.index(word) + 1}/{len(wordlist)}')
                print(CURSOR_UP + ERASE_LINE, end='')
            await asyncio.gather(*tasks)
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + f' {len(self.sites)} sites found\n')

    