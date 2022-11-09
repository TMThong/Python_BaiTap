n=int(input("Nhập số nguyên n ="))
i=0
s=0
c=1
for i in range(1,n):
    s = s + i * c
    print("Đổi dấu tại i = " , i , " thành " , i * c)
    c = c * -1
print("Tổng số là = " , s)
