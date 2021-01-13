#โปรแกรมสร้างภาพวาด 4 เหลี่ยมจตุรัส
number = int(input("ป้อนขนาด :"))
for row in range(1,number+1) :
    for column in range(1,number+1) :
        print("*",end='')
    print(" ")
    
'''
*****
*****
*****
*****
*****
'''