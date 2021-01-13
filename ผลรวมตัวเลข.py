#โปรแกรมหาผลบวก n พจน์แรก

#แบบ while loop
n = int(input("กรอกเลขที่ต้องการบวกจนถึง : "))
i = 1
summation = 0
while i<=n :
    summation+=i
    i+=1
print(summation)

#แบบ ใช้สูตรทางคณิตศาสตร์
x = int(input("กรอกเลขที่ต้องการบวกถึง : "))
print((x/2)*(2+(x-1)))