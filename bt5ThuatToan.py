n = int(input("Nhập số nguyên n "))
s = 1
for i in range(1 , n + 1):
    s = s + 1 / (2 * i + 1)
print("Tổng là " , s)