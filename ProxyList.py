import requests
from termcolor import colored
import time

def get_free_proxies(url, limit=5):
    url_with_limit = f'{url}&limit={limit}'
    response = requests.get(url_with_limit)
    proxy_data = response.json()

    proxies = [f"{entry['ip']}:{entry['port']}" for entry in proxy_data.get('data', [])]
    return proxies

def display_proxy_list(proxies):
    if not proxies:
        print(colored("Nessun proxy disponibile.", 'red'))
    else:
        print(colored("Proxy List:", 'green'))
        for i, proxy in enumerate(proxies, start=1):
            print(colored(f"{i}. {proxy}", 'cyan'))

def print_with_typing_effect(message, color):
    for char in message:
        print(colored(char, color), end='', flush=True)
        time.sleep(0.05)

if __name__ == "__main__":
    proxy_url = 'https://proxylist.geonode.com/api/proxy-list?page=1&sort_by=lastChecked&sort_type=desc'

    print_with_typing_effect("Inserisci il limite della lista (minimo 5, massimo 30): ", 'yellow')

    while True:
        try:
            limit = int(input())
            if 5 <= limit <= 30:
                break
            else:
                print_with_typing_effect("Il limite deve essere compreso tra 5 e 30. Riprova : ", 'red')
        except ValueError:
            print_with_typing_effect("Inserisci un numero valido : ", 'red')

    proxies = get_free_proxies(proxy_url, limit=limit)
    display_proxy_list(proxies)

    print_with_typing_effect("Vuoi salvare la lista dei proxy in un documento txt? (yes/no): ", 'green')

    save_option = input().lower()

    if save_option == 'yes':
        with open('proxy_list.txt', 'w') as file:
            for proxy in proxies:
                file.write(proxy + '\n')
        print_with_typing_effect("Risultato salvato in proxy_list.txt. Grazie per aver provato questo tool. Visita t.me/VikingTerminal per altre utility.", 'yellow')
    elif save_option == 'no':
        print_with_typing_effect("Grazie per aver provato questo tool. Visita t.me/VikingTerminal per altre utility.", 'yellow')
    else:
        print_with_typing_effect("Opzione non valida. Il risultato non sarà salvato. Grazie per aver provato questo tool. Visita t.me/VikingTerminal per altre utility.", 'red')
