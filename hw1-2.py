# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = int(input())

if S % 6 != 0:
    S = int(input('Введите число кратное 6: '))

n = S // 6

print(f'Петя сделал {n}')
print(f'Сережа сделал {n}')
print(f'Катя сделала {4 * n}')