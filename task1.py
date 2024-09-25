def max_fives_count(n, digits):
    max_count = -1
    for i in range(n - 6):  # итерируемся до предпоследней позиции
        if 2 in digits[i:i+7] or 3 in digits[i:i+7]:  # проверяем наличие 2 или 3 в отрезке
            continue  # если есть 2 или 3, переходим к следующей итерации
        count = digits[i:i+7].count(5)  # считаем количество пятерок в отрезке
        if count > max_count:  # если текущее количество пятерок больше максимального
            max_count = count  # обновляем максимальное количество пятерок
    return max_count

# Считываем входные данные
n = int(input())
digits = list(map(int, input().split()))

# Вызываем функцию и выводим результат
result = max_fives_count(n, digits)
print(result)
