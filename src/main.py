from utils import format_date, format_from_number, format_to_number, read_operations_file


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
            print(f"{format_from_number(from_account)} -> {format_to_number(to_account)}")
        else:
            print(f"-> {format_to_number(to_account)}")
        print(f"{amount} {currency_name}\n")


if __name__ == "__main__":
    display_last_operations()
