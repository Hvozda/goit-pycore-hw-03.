import re
def normalize_phone(phone_number):
    cleaned = re.sub(r'[^0-9+]', '', phone_number)
    if cleaned.startswith('+'):
        return cleaned
    if cleaned.startswith('380'):
        return '+' + cleaned
    return '+38' + cleaned
raw_numbers = [
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)