import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)
bin_number = input('Digite o número da BIN: ')
url = f'https://lookup.binlist.net/{bin_number}'

response = requests.get(url)

if response.status_code == 200:
    bin_info = response.json()
    print("")
    print(Fore.RED +"INFORMAÇÃO DO NÚMERO BIN" + Fore.RESET) 
    print("")
    print(f'Número do cartão: {Fore.PURPLE}{bin_number}{Fore.RESET}')
    print(f'Marca do cartão : {Fore.PURPLE}{bin_info.get("marca", "Não disponível")}{Fore.RESET}')
    print(f'Tipo ddo cartão: {Fore.PURPLE}{bin_info.get("tipo", "Não disponível")}{Fore.RESET}')
    print(f'Scheme/Network: {Fore.PURPLE}{bin_info.get("scheme", "Não disponível")}{Fore.RESET}')
    print(f'Comprimento do cartão: {Fore.PURPLE}{bin_info.get("number_length", "16")}{Fore.RESET}')
    print(f'Algoritmo de Luhn: {Fore.PURPLE}{bin_info.get("luhn", "Yes")}{Fore.RESET}')
    print(f'País emisor: {Fore.PURPLE}{bin_info["country"].get("name", "Não disponível")}{Fore.RESET}')
    print(f'Código de país emisor: {Fore.PURPLE}{bin_info["country"].get("alpha2", "Não disponível")}{Fore.RESET}')
    print(f'Nome do banco emissor: {Fore.PURPLE}{bin_info["bank"].get("name", "Não disponível")}{Fore.RESET}')
    print(f'Site do banco emissor: {Fore.PURPLE}{bin_info["bank"].get("url", "Não disponível")}{Fore.RESET}')
    print(f'Telefone do banco emisor: {Fore.PURPLE}{bin_info["bank"].get("phone","Não disponível")}{Fore.RESET}')
    print("")
else:
    print(f'O BIN {bin_number} inválido ou nenhum resultado encontrado.') 
