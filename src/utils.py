from datetime import datetime
import json


def read_operations_file(file_name):
    """
    Читает данные операций из JSON-файла и возвращает их в виде списка словарей.
"""
    with open(file_name) as file:
        return json.load(file)


def format_date(date_str):
    """
    Преобразует строку даты в формате ISO 8601 в формат "ДД.ММ.ГГГГ".
"""
    date_object = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


def format_from_number(card_number):
    """
    Форматирует номер карты или счета, скрывая часть чисел для безопасного отображения.
"""
    data_card = card_number.split(' ')
    if len(data_card[-1]) > 16 and len(data_card) == 1:
        return f"{data_card[0][:4]} {data_card[0][4:6]}** **** {data_card[0][-4::1]}"
    if len(data_card) == 3:
        return f"{data_card[0]} {data_card[1]}  {data_card[2][:4]} {data_card[2][4:6]}** **** {data_card[2][-4::1]}"
    elif len(data_card) == 1:
        return f'{data_card[0:]}'
    elif len(data_card) >= 2 and len(data_card[1]) > 16:
        return f"{data_card[0]} **{data_card[1][-4::1]}"
    else:
        return f"{data_card[0]} {data_card[1][0:4]} {data_card[1][4:6]}** **** {data_card[1][-4::1]}"


def format_to_number(account_number):
    """
    Форматирует номер счета, скрывая часть чисел для безопасного отображения.
"""
    data_card = account_number.split(' ')
    if len(data_card[-1]) > 16 and len(data_card) == 1:
        return f"{data_card[0][:4]} {data_card[0][4:6]}** **** {data_card[0][-4::1]}"
    if len(data_card) == 3:
        return f"{data_card[0]} {data_card[1]}  {data_card[2][:4]} {data_card[2][4:6]}** **** {data_card[2][-4::1]}"
    elif len(data_card) == 1:
        return f'{data_card[0:]}'
    elif len(data_card) >= 2 and len(data_card[1]) > 16:
        return f"{data_card[0]} **{data_card[1][-4::1]}"
    else:
        return f"{data_card[0]} {data_card[1][0:4]} {data_card[1][4:6]}** **** {data_card[1][-4::1]}"
