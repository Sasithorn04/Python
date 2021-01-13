#โปรแกรมผลรวมตัวเลข
start = 1
stop = int(input("ต้องการบวกเลขกี่จำนวน : "))
summation,avg = 0,0
while start<=stop :
    num = float(input("ป้อนตัวเลขที่ต้องการบวก : "))
    start+=1
    summation+=num
print("ผลรวม =",summation)
print("ค่าเฉลี่ย =",summation/stop)