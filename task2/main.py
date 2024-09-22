from math import sqrt
""" Лаба 1. Git, Python. Реализовать алгоритм Эратосфена.
Алгоритм нахождения простых чисел до заданного натурального числа путем постепенного отсеивания составных чисел """


def eratosthenes_algorithm(num):
    prime_nums = [i for i in range(num)]
    for i in range(2, int(sqrt(num)) + 1):
        if prime_nums[i]:
            for j in range(i*i, num, i):
                prime_nums[j] = 0
    prime_nums[1] = 0                      # на этом индексе стоит единица, она не является простым числом
    return prime_nums


def main():
    while True:
        num = input("введите натуральное число, до которого будут искаться простые числа\n")
        try:
            bomba = int(num)
            if bomba > 0:
                prime_nums = [i for i in eratosthenes_algorithm(bomba) if eratosthenes_algorithm(bomba)[i] != 0]
                print(f"простые числа до заданного числа:\n{' '.join(str(item) for item in prime_nums)}"
                      f"\nкол-во простых чисел - {len(prime_nums)}")
                break
            else:
                print("можно вводить только натуральные числа")
        except ValueError:
            print('буквы нельзя и дробные числа тоже, только натуральное число')


if __name__ == "__main__":
    main()
