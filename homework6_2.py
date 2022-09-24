# Найти сумму чисел списка стоящих на нечетной позиции

lst = []
lst = input('input numbers: ').split()
sum_odd = sum(int(lst[i]) for i in range(1, len(lst), 2))
odd_el = str([lst[i] for i in range(1, len(lst), 2)]).strip('[]')
print(f'Для списка {lst} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')