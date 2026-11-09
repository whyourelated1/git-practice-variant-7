from pricing import divide

TITLE = "Payment training"


def main():
    amount = 1200
    people = 3
    print(TITLE)
    print(divide(amount, people))


# Settings for the first developer
REGION = "RU"
LANGUAGE = "ru"


# Settings for the third developer
CURRENCY = "RUB"


if __name__ == "__main__":
    main()
