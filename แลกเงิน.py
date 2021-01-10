#โปรแกรมแลกเงิน
money = int(input("ป้อนจำนวนเงินที่คุณต้องการ : "))
if money>= 1000 :
    print("แบงค์ 1000 บาท ",money//1000," ใบ")
    money%=1000
if money>=500 :
    print("แบงค์ 500 บาท ",money//500," ใบ")
    money%=500
if money>=100 :
    print("แบงค์ 100 บาท ",money//100," ใบ")
    money%=100
if money>=50 :
    print("แบงค์ 50 บาท ",money//50," ใบ")
    money%=50
if money>=20 :
    print("แบงค์ 20 บาท ",money//20," ใบ")
    money%=20
if money>=10 :
    print("เหรียญ 10 บาท ",money//10," เหรียญ")
    money%=10
if money>=5 :
    print("เหรียญ 5 บาท ",money//5," เหรียญ")
    money%=5
if money>=2 :
    print("เหรียญ 2 บาท ",money//2," เหรียญ")
    money%=2
if money>=1 :
    print("เหรียญ 1 บาท ",money//1," เหรียญ")


