def Check_data(data):
    b ="01"
    for i in data:
        if(i not in b):
            print("Enter only binary number......")
            return 0
    return 1
def Division(value,data):
    # y = int(dividend, 2)^int(divisor,2)
    #print bin(y)[2:].zfill(len(a))
    l=len(value)  #divisor
    r=len(data) 
    divisor=value
    dividend=data[0:l]
    for i in range(l,r+1):
        print ("Dividend: ",dividend)
        print ("Divisor : ",divisor)
        XOR=int(dividend, 2)^int(divisor,2)
        XOR=bin(XOR)[2:].zfill(len(divisor))
        print ("XOR     : ",XOR)
        XOR=XOR[1:] 
        if(i==r):
            break
        dividend=XOR + data[i]
        if(dividend[0]=='0'):
           divisor="0"*4
        else:
            divisor=value
    return XOR

def send_Recieve(d,mode,divisor):
    Remainder=Division(divisor,d)
    print("\nRemainder: ",Remainder)
    if(mode=='0'):
       return d[0:-len(divisor)+1] + Remainder[0:]
       
      
    elif(mode=='1'):
        if (Remainder=="0"*(len(Remainder))) :
            print("Your data is not corrupted")
            return
    print("Your data is Corrupted")

Div=input("\nEnter a Divisor: ")   
while(Check_data(Div)==0):
    Div=input("\nEnter  Correct Data: ")  
print("\n=============Sender=============\n")    
send_data=input("Enter  your Data: ")
while(Check_data(send_data)==0):
    send_data=input("\nEnter  Correct Data: ")
send_data= send_data + ("0" *(len(Div)-1))
print("The Appended Data is: ",send_data)
codeword =send_Recieve(send_data,'0',Div)
print("The codeword: ",codeword)
print("================================")
print("\n=============Reciever=============\n")
recieved_data=input("\nEnter  your Recieved Data: ")
while(Check_data(recieved_data)=='0'):
    recieved_data=input("........Enter  Correct Data: ")
recieved_data=send_Recieve(recieved_data,'1',Div)
print("================================")