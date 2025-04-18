import pytest
import pandas as pd


@pytest.fixture
def transactions():
    transactions = [{
        "Дата операции": "2018-01-04 14:05:08",
        "Дата платежа": "06.01.2018",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -1065.9,
        "Валюта операции": "RUB",
        "Сумма платежа": -1065.9,
        "Валюта платежа": "RUB",
        "Кэшбэк": "nan",
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Пятёрочка",
        "Бонусы (включая кэшбэк)": 21,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 1065.9,
    },
    {
        "Дата операции": "2018-01-03 15:03:35",
        "Дата платежа": "04.01.2018",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -73.06,
        "Валюта операции": "RUB",
        "Сумма платежа": -73.06,
        "Валюта платежа": "RUB",
        "Кэшбэк": "nan",
        "Категория": "Супермаркеты",
        "MCC": 5499.0,
        "Описание": "Magazin 25",
        "Бонусы (включая кэшбэк)": 1,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 73.06,
    },
    {
        "Дата операции": "2018-01-03 14:55:21",
        "Дата платежа": "05.01.2018",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -21.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -21.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": "nan",
        "Категория": "Красота",
        "MCC": 5977.0,
        "Описание": "OOO Balid",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 21.0,
    },
    {
        "Дата операции": "2018-01-01 20:27:51",
        "Дата платежа": "04.01.2018",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -316.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -316.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": "nan",
        "Категория": "Красота",
        "MCC": 5977.0,
        "Описание": "OOO Balid",
        "Бонусы (включая кэшбэк)": 6,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 316.0,
    },
    {
        "Дата операции": "2018-01-01 12:49:53",
        "Дата платежа": "01.01.2018",
        "Номер карты": "nan",
        "Статус": "OK",
        "Сумма операции": -3000.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -3000.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": "nan",
        "Категория": "Переводы",
        "MCC": "nan",
        "Описание": "Линзомат ТЦ Юность",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 3000.0,
    }]
    transactions = pd.DataFrame(transactions)
    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    print(f"\n{transactions}")
    transactions.to_excel(path_or_buf="1.xlsx")
    return transactions
