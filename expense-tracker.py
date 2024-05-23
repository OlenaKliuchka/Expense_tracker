expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def delete_expense(category):
    if category in expenses:
        del expenses[category]
        print("Витрата видалена!")
    else:
        print("Цієї категорії не існує.")

def view_expenses():
    if not expenses:
        print("Витрат немає.")
    else:
        for category, amount in expenses.items():
            print(f"{category}: {amount}")

while True:
    print("\n1. Додати витрату")
    print("2. Переглянути витрати")
    if expenses:
        print("3. Видалити витрату")
    print("4. Вийти")
    choice = input("Виберіть опцію: ")

    if choice == '1':
        category = input("Введіть категорію витрати: ")
        amount = float(input("Введіть суму витрати: "))
        add_expense(category, amount)
        print("Витрата додана!")

    elif choice == '2':
        view_expenses()

    elif choice == '3' and expenses:
        category = input("Введіть категорію витрати для видалення: ")
        delete_expense(category)

    elif choice == '4':
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")
