#โปรแกรมแปลงศักราช
year = (input("ป้อนศักราชที่ต้องการแปลง (เช่น ค.ศ. 2020): "))
if year.startswith("พ.ศ.") :
    result = int(year[4:])-543
    start = " ค.ศ.="
elif year.startswith("ค.ศ.") :
    result = int(year[4:])+543
    start = " พ.ศ.="
else :
    result = "กรุณาป้อนศักราชนำหน้าด้วย"
    start = ""
print(year,start,result)