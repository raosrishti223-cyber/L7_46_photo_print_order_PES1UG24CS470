
import math


def parse_order(text):
    try:
        if not isinstance(text, str):
            return None

        if text.count(':') != 1:
            return None

        size, copies = text.split(':')

        size = size.strip().upper()
        copies = int(copies.strip())

        if not size or copies < 0:
            return None

        return size, copies

    except (ValueError, TypeError, AttributeError):
        return None


def file_size_average(sizes_csv):
    try:
        if not isinstance(sizes_csv, str):
            return None

        if not sizes_csv.strip():
            return None

        parts = sizes_csv.split(',')

        if any(not value.strip() for value in parts):
            return None

        values = [int(value.strip()) for value in parts]

        if any(value < 0 for value in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError, AttributeError, ZeroDivisionError):
        return None


def payable_amount(text):
    try:
        if not isinstance(text, str):
            return None

        if text.count('|') != 1:
            return None

        amount, discount = text.split('|')

        amount = float(amount.strip())
        discount = float(discount.strip())

        if not math.isfinite(amount) or not math.isfinite(discount):
            return None

        if amount < 0 or discount < 0:
            return None

        total = amount * 1.18 - discount

        return max(total, 0)

    except (ValueError, TypeError, AttributeError, OverflowError):
        return None


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter print size:copies (e.g. 4x6:25): ")
    result = parse_order(user_input)
    print("Size and Copies:", result)

    print("\n==== Running file_size_average ====")
    user_input = input("Enter file sizes in MB as CSV (e.g. 4,8,12): ")
    result = file_size_average(user_input)
    print("Average File Size:", result)

    print("\n==== Running payable_amount ====")
    user_input = input("Enter amount|discount (e.g. 450|50): ")
    result = payable_amount(user_input)
    print("Payable Amount:", result)


if __name__ == "__main__":
    main()
