n = int(input("Nhập n số nguyên "))
m = n
s = 0
for i in range(n):
    m = m -1
    x = int(input("Nhập n" + str(m) + " = "))
    s = s + x
print("Tổng số " , s)
