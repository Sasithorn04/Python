#โปรแกรมคำนวณค่า BMI
hight = float(input("กรุณากรอกส่วนสูงของท่าน หน่วยเซนติเมตร :"))
weight = float(input("กรุณากรอกน้ำหนักของท่าน หน่วยกิโลกรัม :"))

BMI = weight/((hight/100)**2)

if BMI>=30 :
    result = "โรคอ้วนระดับ3"
elif BMI>=25 and BMI<=29.90 :
    result = "โรคอ้วนระดับ2"
elif BMI>=23 and BMI<=24.90 :
    result = "โรคอ้วนระดับ1"
elif BMI>=18.50 and BMI<=22.90 :
    result = "สุขภาพดี"
elif BMI<= 18 and BMI>0 :
    result = "ผอม"
else :
    result = "ไม่ทราบค่าที่ชัดเจน"

print("BMI = ",BMI, result)