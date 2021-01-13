#โปรแกรมแสดงตัวเลขเป็นขั้นบันได
stop = int(input("ป้อนตัวเลขสุดท้ายที่ต้องการ :"))
for row in range(1,stop+1) :
    for column in range(1,row+1):
        print(column,end='')
    print(" ")