import random
import json
from colorama import Fore, Style

def card_luhn_checksum_is_valid(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven ):
            digit *= 2
        if digit > 9:
            digit -= 9
        sum += digit

    return (sum % 10) == 0

def generate_card_number(card_type):
    card_number = ""

    if card_type == "visa":
        card_number = "4"
    elif card_type == "mastercard":
        card_number = "5" + str(random.randint(1, 5))
    elif card_type == "amex":
        card_number = "3" + str(random.choice([4, 7]))
    elif card_type == "discover":
        card_number = "6" + "0" + "1" + "1"
    elif card_type == "diners":
        card_number = "3" + "0" + str(random.choice([0, 6, 8])) + str(random.randint(0, 9))

    while len(card_number) < 15:
        card_number += str(random.randint(0, 9))

    digits = [int(x) for x in card_number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    checksum = sum(digits) * 9 % 10
    card_number += str(checksum)

    if not card_luhn_checksum_is_valid(card_number):
        card_number = generate_card_number(card_type)

    return card_number

def generate_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(2024, 2029)
    return f"{month:02}/{year:02}"

def generate_cvv():
    return str(random.randint(100, 999))

card_type = input("Escolha o tipo de cartão (visa, mastercard, amex, discover o diners): ")
num_cards = int(input("Escolha a quantidade a ser gerada: "))

card_details = []
for i in range(num_cards):
    card_number = generate_card_number(card_type)
    expiry_date = generate_expiry_date()
    cvv = generate_cvv()

    card_info = {"numero_cartao": card_number, "data_de_expiracao": expiry_date, "cvv": cvv, "tipo_do_cartao": card_type.capitalize()}
    card_details.append(card_info)

result = {"cartao_gerados": card_details}
json_result = json.dumps(result, indent=4)

print(f"\nOs números de cartão de crédito gerados são:\n")

for card in card_details:
    cc_number = card["numero_do_cartao"]
    date = card["data_de_expiracao"]
    cvv = card["cvv"]
    card_type = card["tipo_do_cartao"]
    print(f"Cartão de crédito: {Fore.GREEN}{cc_number}{Fore.RESET}")
    print(f"Data de expiração: {Fore.GREEN}{date}{Fore.RESET}")
    print(f"Código de segurança CVV: {Fore.GREEN}{cvv}{Fore.RESET}")
    print(f"Tipo do cartão: {Fore.YELLOW}{card_type}{Fore.RESET}\n")
