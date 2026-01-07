sales = [
    {"продукт": "Ноутбук", "кількість": 5, "ціна": 15000},
    {"продукт": "Мишка", "кількість": 30, "ціна": 400},
    {"продукт": "Клавіатура", "кількість": 20, "ціна": 800},
    {"продукт": "Монітор", "кількість": 3, "ціна": 7000},
    {"продукт": "Мишка", "кількість": 10, "ціна": 400}
]

def calculate_income(sales_list):
    income = {}

    for sale in sales_list:
        product = sale["продукт"]
        quantity = sale["кількість"]
        price = sale["ціна"]

        total = quantity * price

        if product in income:
            income[product] += total
        else:
            income[product] = total

    return income


total_income = calculate_income(sales)

products_over_1000 = []

for product, money in total_income.items():
    if money > 1000:
        products_over_1000.append(product)

print("Загальний дохід по кожному продукту:")
for product, money in total_income.items():
    print(f"{product}: {money} грн")

print("\nПродукти, що принесли дохід більше ніж 1000 грн:")
print(products_over_1000)