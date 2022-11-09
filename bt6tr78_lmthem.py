n = int(input("Nhập số nguyên n = "))
s = 1
T = 1
for i in range(2, n + 1):        
    s = s * i
    T=T + s
print("Tổng số là " , T)