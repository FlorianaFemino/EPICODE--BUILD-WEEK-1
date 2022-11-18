import http.client

host = input ("\nInserire l'Host/IP del server da attaccare: ")
path = input ("\nInserire il percorso della pagina da analizzare: ")
port = input ("\nInserire la porta target (default: 80): ")

if (port == ""):
    port = 80

try:
        connection = http.client.HTTPConnection(host, port)
        connection.request('OPTION','/' + path +".html")
        response = connection.getresponse()
        methods = response.getheader("allow").split(",")
        print ("\n\nI metodi abilitati sono:\n\n")
        for i in range (len(methods)):
                print ("[+] {}".format(methods[i]))
        connection.close()
except ConnectionRefusedError:
        print("\n\nConnection Refused")