n = int(input("Nhập số nguyên n "))
s = 0
for i in range(1 , n + 1):
    s = s + 1 / (2 * i)
print("Tổng là " , s)
print(list(range(1 , n + 1)))