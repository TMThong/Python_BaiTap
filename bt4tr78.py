n = int(input("Nhập số nguyên n = "))
s = 0
for i in range(n):
    print("Nhập giá trị n " , i)
    x = int(input());
    s = s + (x ** 2)
print("Tổng là = " , s)