import sys
import pytest

sys.path.insert(0, "../src")
from utils import format_date, format_from_number, format_to_number, read_operations_file


def test_format_date():
    date_str = "2019-07-12T20:41:47.882230"
    formatted_date = format_date(date_str)
    assert formatted_date == "12.07.2019"


def test_format_from_number():
    card_number1 = "Visa 1234567890123456"
    formatted_number1 = format_from_number(card_number1)
    assert formatted_number1 == 'Visa 1234 56** **** 3456'

    card_number2 = "Visa Classik 9876543210987654"
    formatted_number2 = format_from_number(card_number2)
    assert formatted_number2 == 'Visa Classik  9876 54** **** 7654'

    card_number3 = "12345678901234567890"
    formatted_number3 = format_from_number(card_number3)
    assert formatted_number3 == '1234 56** **** 7890'

    card_number4 = "Счет 12345678901234567890"
    formatted_number4 = format_from_number(card_number4)
    assert formatted_number4 == 'Счет **7890'


def test_format_to_number():
    account_number = "Visa 1234567890123456"
    formatted_number1 = format_to_number(account_number)
    assert formatted_number1 == 'Visa 1234 56** **** 3456'

    account_number = "Visa Classik 9876543210987654"
    formatted_number2 = format_to_number(account_number)
    assert formatted_number2 == 'Visa Classik  9876 54** **** 7654'

    account_number = "12345678901234567890"
    formatted_number3 = format_to_number(account_number)
    assert formatted_number3 == '1234 56** **** 7890'

    account_number = "Счет 12345678901234567890"
    formatted_number4 = format_to_number(account_number)
    assert formatted_number4 == 'Счет **7890'


def test_format_number_other_cases():
    card_number = "123456"
    formatted_number = format_from_number(card_number)
    assert formatted_number == "['123456']"

    account_number = "9876543210"
    formatted_number = format_to_number(account_number)
    assert formatted_number == "['9876543210']"


def test_read_operations_file(temp_operations_file):
    file_path = temp_operations_file

    data = read_operations_file(file_path)

    assert len(data) == 3
    assert isinstance(data, list)
    assert all(isinstance(op, dict) for op in data)
    assert data[0]["state"] == "EXECUTED"
    assert data[0]["description"] == "Operation 1"
    assert data[1]["state"] == "PENDING"
    assert data[1]["description"] == "Operation 2"
    assert data[2]["state"] == "EXECUTED"
    assert data[2]["description"] == "Operation 3"


if __name__ == "__main__":
    pytest.main()
