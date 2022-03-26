def Check_data(data):
    if(len(data)<=8):
        print("Data must be greater than 8 bits....")
        return 0
    if(len(data)%8 !=0):
        print("For 8 bit checksum length of data must be divisible by 8")
        return 0
    b ="01"
    for i in data:
        if(i not in b):
            print("Enter only binary number......")
            return 0
    return 1

def segments(data,length):
    datalist=[]
    for i in range(0,len(data),length):
         datalist.append(data[i:i+length])
    return datalist
def Addition(datalist):
    sum=0
    for i in range(len (datalist)):
         sum=sum + int (datalist[i],2)
    sum=bin(sum)
    return sum[2:]
def AddCarry(sum,data):
    
    n=len(sum)-8
    sum=bin (int(sum[0+n:] ,2) + int('0' + sum[0:0 + n],2))
    sum=sum[2:]
    if(len(sum)<8):
        n=8-len(sum)  # How it is giving positive number
        z="0"
        sum= (z * n) + sum
    return sum
def cal_Checksum(sum):
    checksum = sum.replace('1','x') 
    checksum = checksum.replace('0','1') 
    checksum = checksum.replace('x','0')
    return checksum
def sending(d):
    length=8
    segment=segments(d,length)
    print("\nYour data is divided into segments: ",segment)
    sum=Addition(segment)
    print("\nYour Sum: ",sum)
    while(len(sum)>8):
       sum= AddCarry(sum,d)
    print("\nYour final Sum: ",sum)
    checksum=cal_Checksum(sum)
    print("CheckSum",checksum)
    return d+checksum

def recieving(d):
    length=8
    segment=segments(d,length)
    print("Your data is divided into segments: ",segment)
    sum=Addition(segment)
    print("\nYour Sum: ",sum)
    while(len(sum)>8):
       sum= AddCarry(sum,d)
    print("\nYour final Sum: ",sum)
    checksum=cal_Checksum(sum)
    print("CheckSum: ",checksum)
    if(checksum==("00000000")):
        print("Your Data is not Corrupted........")
        return
    print("Your Data is  Corrupted........")
    
print("\n=============SENDER=============\n")
send_data=input("Enter  your Data: ")

while(Check_data(send_data)==0):
    send_data=input("\nEnter  Correct Data: ")
send_data =sending(send_data)
print("The codeword: ",send_data)
print("================================")
print("\n=============Reciever=============\n")
recieved_data=input("\nEnter  your Recieved Data: ")
while(Check_data(recieved_data)==0):
    recieved_data=input("........Enter  Correct Data: ")
recieved_data=recieving(recieved_data)
print("================================")







