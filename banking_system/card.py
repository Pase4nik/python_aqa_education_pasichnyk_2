import random


def luhn_algorithm(card_number):
    card_number = list(map(int, card_number))  # Create a list of integers from the string
    for i, _ in enumerate(card_number, 1):
        # Multiply each odd digit by 2
        if i % 2 != 0:
            card_number[i - 1] *= 2
        # Subtract 9 from any digit bigger than 9
        if card_number[i - 1] > 9:
            card_number[i - 1] -= 9
    return sum(card_number)  # Return sum


def generate_card_number(acc_number):
    iin = "400000"  # IIN given by the assignment
    luhn_sum = luhn_algorithm(iin + acc_number)  # Calculate Luhn sum
    checksum = get_checksum(luhn_sum)  # Get checksum
    return iin + acc_number + str(checksum)  # Return 16-digit card number as a string


def get_checksum(luhn_sum):
    # Check sum added to the luhn sum must return round number
    return 10 - luhn_sum % 10 if luhn_sum % 10 != 0 else 0


# Generate 9-digit account number
def generate_account_number():
    acc_number = ""
    for _ in range(9):
        acc_number += str(random.randrange(10))
    return acc_number


def generate_pin():
    pin_code = ""
    for _ in range(4):
        pin_code += str(random.randrange(10))
    return pin_code
