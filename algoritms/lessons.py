# пузырковая сортировка (Buble Sort)

# def buble_sort(chisla):
#     n = len(chisla)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if chisla[j] > chisla[j+1]:
#                 chisla[j], chisla[j+1] = chisla[j+1], chisla[j]
#     return chisla

# chisla = [101, 22, 31, 55, 1, 90, 203]
# otsortirovanny_chisla = buble_sort(chisla)
# print("Отсортированные массив: ", otsortirovanny_chisla)

# ____________________________________________________________________

# # Линейный поиск (Linear Search) 

def linera_search(nomera, nomer):
    """
    Функция линейного поиска элемента в массиве
    nomera - список элементов
    nomer - искомый элемент
    """
    for index, element in enumerate(nomera):
        if element == nomer:
            return index
    return -1 # Если элемент не найден, возвращаем -1

nomera = [101, 22, 31, 55, 1, 90, 203]
nomer = 31

index = linera_search(nomera, nomer)
print(index)

if index != -1:
    print(f"Элемент {nomer} найден на индексе {index}")
else:
    print(f"Элемент {nomer} не найден в массиве")

# ___________________________________________________________________


def sql_request():
    sql = [
        SELECT * FROM raby;
    ]

sql_request()
print(sql_request)

SELEC first_name,last_name from RABY 
ORDER BY fisrt_name == 'A' and last_name == 'A'
