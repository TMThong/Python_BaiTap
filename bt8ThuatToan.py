n = int(input("Nhập số nguyên n "))
s = 1/2
for i in range(1 , n):
    s = s + (2 * i + 1) / (2 * i + 2)
print("Tổng là " , s)