import ping3, time, os 
from requests import get
from pyportscanner import pyscanner

def ping():
    print("[1] Ping Padrão \n[2] Ping Infinito \n[99] Voltar \n")
    es = input(f'> ')
    if '1' == es:
       url1 = input("URL: ")
       os.system("clear")
       ping3.verbose_ping(url1)
    elif '2' == es:
        url2 = input("URL: ")
        os.system("clear")
        while True:
          ping3.verbose_ping(url2)
          time.sleep(2)
    elif '99' == es:
        os.system("clear")
        init()

def scan():
    scanner = pyscanner.PortScanner(target_ports=100, timeout=10, verbose=True)
    host = input("Host ou IP: ")
    scanner.scan(host)

        
def ip():
    ip = get('http://meuip.com/api/meuip.php').text
    os.system("clear")
    print(f'Seu ip é: {ip} ')

def init():
    print("[1] Ping \n[2] Get your IP \n[3] Scan Ports \n[0] EXIT \n")
    a = input(f'> ')
    os.system("clear")
    if '1' == a:
      ping()
    elif '2' == a:
      ip()
    elif '3' == a:
      scan()
    elif '0' == a:
      os.system("clear")
      exit()

init()




    
    
    
    






       
       

      
      
        
      






