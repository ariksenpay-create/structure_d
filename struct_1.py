import  time


A = int(input("Введите значение А в диапазоне от 2 до 2000000000 "))
B = int(input("Введите значение B в диапазоне от 2 до 2000000000 "))

start_time = time.time()

n = 1
for n in range(1, 100):
    if B**n % A == 0:
        print(n)
        break
else:
    print(-1)

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")

