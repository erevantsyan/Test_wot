from buffer import FixedSizeFIFO
from buffer2 import DynamicFIFO

#1 задание
def isEven(value):
    return value // 2 == value / 2

num = int(input())
print(isEven(num))

# плюсы: болле эффективный
# минусы: менее понятен


#2 задание
sizeBuffer1 = int(input("Введите размер "))
buffer1 = FixedSizeFIFO(sizeBuffer1)

print("Введите элементы в буффер")
for i in range(sizeBuffer1):
    count = float(input())
    buffer1.push(count)

if buffer1.is_empty():
    print("Буфер пуст")
elif buffer1.is_full():
    print("Буфер заполнен")
else:
    print("В буфере есть данные")

print("Вывод значений буфера:")
for i in range(sizeBuffer1):
    value = buffer1.pop()
    print(value)

if buffer1.is_empty():
    print("Буфер пуст")
elif buffer1.is_full():
    print("Буфер заполнен")
else:
    print("В буфере есть данные")

# плюсы: простая реализация, эффективное использование памяти
# минусы: заранее известен размер

buffer2 = DynamicFIFO()
sizeBuffer2 = int(input("Введите размер "))

print("Введите элементы в буффер")
for i in range(sizeBuffer2):
    count = float(input())
    buffer2.push(count)

print("Вывод значений буфера:")
for i in range(sizeBuffer2):
    print(buffer2.pop())

# плюсы: размер может быть любым, быстрая операция добавления и удаления элементов
# минусы: может потребовать больше памяти

#3 задание

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less = [x for x in nums[1:] if x <= pivot]
        greater = [x for x in nums[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

#Посмотрел в интернете, так как не знал какая сортировка лучше.