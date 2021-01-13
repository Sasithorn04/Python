#โปรแกรมเรียงตัวเลขจำนวนเต็ม max-min sum
number = []
print("หากต้องการหยุดให้ใส่ 00")
while True:
    x = int(input("ป้อนตัวเลขที่คุณต้องการเรียง :"))
    if x == 00:
        break
    number.append(x)
print("ก่อนเรียง =",number)
number.sort()
print("มากไปน้อย =",number)
number.reverse()
print("น้อยไปมาก =",number)
print("ค่ามากสุด =",max(number))
print("ค่าน้อยสุด =",min(number))
print("ผลรวม =",sum(number))
