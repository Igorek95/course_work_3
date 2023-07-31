import json


def read_operations_file(file_name):
    with open(file_name) as file:
        return json.load(file)


def format_date(date_str):
    date_parts = date_str.split("T")[0].split("-")
    return ".".join(reversed(date_parts))


def format_from_number(card_number):
    data_card = card_number.split(' ')
    if len(data_card) == 3:
        return f"{data_card[0]} {data_card[1]}  {data_card[2][0:4]} {data_card[2][5:7]}** **** {data_card[2][12:]}"
    elif len(data_card) == 1:
        return f'{data_card[0:]}'
    elif len(data_card[1]) > 16:
        return f"{data_card[0]} ** {data_card[1][-1:-5:-1]}"
    else:
        return f"{data_card[0]} {data_card[1][0:4]} {data_card[1][5:7]}** **** {data_card[1][12:]}"


def format_account_number(account_number):
    return f"**{account_number[-4:]}"


def display_last_operations():
    data = read_operations_file('operations.json')

    executed_operations = [op for op in data if op.get('state', 'UNKNOWN') == 'EXECUTED']
    last_operations = sorted(executed_operations, key=lambda op: op['date'], reverse=True)[:5]

    for operation in last_operations:
        date = format_date(operation['date'])
        description = operation['description']
        to_account = operation['to']
        amount = operation['operationAmount'].get('amount', '0.00')
        currency_name = operation['operationAmount']['currency'].get('name', 'USD')

        print(f"{date} {description}")
        if 'from' in operation:
            from_account = operation.get('from', '')
            print(f"{format_from_number(from_account)} -> Счет {format_account_number(to_account)}")
        else:
            print(f"-> Счет {format_account_number(to_account)}")
        print(f"{amount} {currency_name}\n")


if __name__ == "__main__":
    display_last_operations()
