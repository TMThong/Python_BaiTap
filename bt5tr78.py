n = int(input("Nhập số nguyên n "))
s = 1
for i in range(n):
    x = int(input("Nhập giá trị n" + str(i) + " = "))
    if x % 2 == 0:
        s = s - x ** 2
    else:
        s = s + x ** 2
print("Tổng số = " , s)