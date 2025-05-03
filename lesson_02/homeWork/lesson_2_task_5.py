def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    if month in [3, 4, 5]:
        return "Весна"
    if month in [6, 7, 8]:
        return "Лето"
    if month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
