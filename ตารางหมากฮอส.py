#โปรแกรมจำลองตารางหมากฮอส
#ปรับจากสร้างภาพวาด4เหลี่ยมจตุรัส
number = int(input("ป้อนขนาด :"))
for row in range(1,number+1) :
    for column in range(1,number+1) :
        if (column%2 == 0) & (row%2 == 0) :
            print("o",end='')
        elif (column%2 != 0) & (row%2 != 0):
            print("o",end='')
        else :
            print("x",end='')
    print(" ")
    
'''
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
'''