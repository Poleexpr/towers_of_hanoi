# количество блинов принимается в int
# количество стержней принимается как список аргументов

def solve_towers_of_hanoi_problem(number_of_pancakes, *number_of_rods):
  # первый частный случай: 0 блинов не нужно перемещать  
  if(number_of_pancakes == 0):
    return 'кажется, кто-то уже съел все блины'
  
  # второй частный случай: один блин с 2 стержнями можно переместить единственным образом
  if(number_of_pancakes == 1 and len(number_of_rods) == 2):
    print(f"блин 1: стержень {number_of_rods[0]} -> стержень {number_of_rods[1]}")
    with open('решение.txt', 'a') as file:
      print(f"блин 1: стержень {number_of_rods[0]} -> стержень {number_of_rods[1]}", file=file)
  
  # для решения задачи с 3 и более стержнями используется рекурсия. вызывается ф-ция с количесвтом блинов на 1 меньше текущего кол-ва и местами меняются "вспомогательный" и "целевой" стержни, затем шаг выводится в консоль и в файл, затем вызывается ф-ция с количеством блинов на 1 меньше текущего кол-ва и местами меняются "вспомогательный" и "стартовый" стержни
  if(len(number_of_rods) >= 3):
    solve_towers_of_hanoi_problem(number_of_pancakes - 1, number_of_rods[0], 
    number_of_rods[2], number_of_rods[1])

    # вывод шагов в консоль
    print(f"блин {number_of_pancakes}: стержень {number_of_rods[0]} -> стержень {number_of_rods[1]}")

    # вывод шагов в файл решение.txt
    with open('решение.txt', 'a') as file:
      print(f"блин {number_of_pancakes}: стержень {number_of_rods[0]} -> стержень {number_of_rods[1]}", file=file)
    solve_towers_of_hanoi_problem(number_of_pancakes - 1, number_of_rods[2], number_of_rods[1], number_of_rods[0])

print(solve_towers_of_hanoi_problem(3, 'a', 'b', 'c'))

# TODO: формально ф-ция принимает неограниченное кол-во стержней, но решает задачу не самым оптимальным способом, используя максимум три стержня
# TODO: может быть, есть смысл разделять вывод разных вызовов ф-ции в файле решение.txt 






  