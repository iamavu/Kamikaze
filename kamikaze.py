#kamikaze
version = '0.0.1'

from colorama import init
init()
from colorama import Fore, Back, Style

from modules.recon.crawl import Crawl
from modules.recon.directory import Directory
from modules.support.args import parser
import asyncio
import uvloop

def banner():
    print(Fore.MAGENTA + Style.BRIGHT + f'''
                                                                                                                  
                                                                                                        
  G:                                             G:                                                   ,;
  E#,    :                                   t   E#,    :                                           f#i 
  E#t  .GE           ..           ..       : Ej  E#t  .GE           ..                            .E#t  
  E#t j#K;          ;W,          ,W,     .Et E#, E#t j#K;          ;W,      ,##############Wf.   i#W,   
  E#GK#f           j##,         t##,    ,W#t E#t E#GK#f           j##,       ........jW##Wt     L#D.    
  E##D.           G###,        L###,   j###t E#t E##D.           G###,             tW##Kt     :K#Wfff;  
  E##Wi         :E####,      .E#j##,  G#fE#t E#t E##Wi         :E####,           tW##E;       i##WLLLLt 
  E#jL#D:      ;W#DG##,     ;WW; ##,:K#i E#t E#t E#jL#D:      ;W#DG##,         tW##E;          .E#L     
  E#t ,K#j    j###DW##,    j#E.  ##f#W,  E#t E#t E#t ,K#j    j###DW##,      .fW##D,              f#E:   
  E#t   jD   G##i,,G##,  .D#L    ###K:   E#t E#t E#t   jD   G##i,,G##,    .f###D,                 ,WW;  
  j#t      :K#K:   L##, :K#t     ##D.    E#t E#t j#t      :K#K:   L##,  .f####Gfffffffffff;        .D#; 
   ,;     ;##D.    L##, ...      #G      ..  E#t  ,;     ;##D.    L##, .fLLLLLLLLLLLLLLLLLi          tt 
          ,,,      .,,           j           ,;.         ,,,      .,,                                   
                                                                                                        
                                                                                                        ''' + Style.RESET_ALL + Fore.MAGENTA + f'''
                                                                                                        > Kamikaze v{version}
                                                                                                        > Created by @iamavu''' 
                                                                                                        )
    print(Style.RESET_ALL)

async def kamikaze():
    banner()
    args = parser()
    
    if args.full == True:
        crawl = Crawl()
        directory = Directory()
        
        await crawl.target_headers()
        await crawl.sitemap()
        await crawl.txts()
        
        await directory.enumdir()
    
    if args.crawl == True:
        crawl = Crawl()
        await crawl.target_headers()
        await crawl.sitemap()
        await crawl.txts()
    
    if args.dir == True:
        directory = Directory()
        await directory.enumdir()  
    

async def main():
    await kamikaze()
if __name__ == '__main__':
    uvloop.install()
    asyncio.run(main())
    
    
