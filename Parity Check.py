
def bindata(binlist,data) :
  for letter in data:
    asc=ord(letter)
    bindata=bin(asc)
    binlist.append(bindata[2:]) 
def Check_data(data,index):
    b ="01"
    for i in data:
        if(i not in b):
            print("Enter only binary number......")
            return 0
    if(len(data)!= len(sbinlist[index])):
        print("Enter Data of Correct length........")
        return 0
    return 1

def countbit(countlist,binlist,last):
    for item in range(len(binlist)):
        count=0
        for bit in range(0,len(binlist[item])-last):
            if(binlist[item][bit]=='1'):
                count=count + 1
        countlist.append(count)
def AddParity():
    for i in range(0,len(sbinlist)):
        if scountlist[i]%2 !=0:
            sbinlist[i]=sbinlist[i] + '1'
        else:
            sbinlist[i]=sbinlist[i] + '0'
def CheckParity():
    for i in range(len(rcountlist)):
        if((rbinlist[i][-1]=='1' and rcountlist[i]%2==0 ) or (rbinlist[i][-1]=='0' and rcountlist[i]%2!=0)):
            print("\nYour recieved data is corrupted")
            return
    print("\nYour recieved data is not corrupted")
def Recieve_data(length):
    i=0
    while(i< length):
       bits=input('Enter your Recieved Data Chunk  {} :   '.format(i+1)) 
       if (Check_data(bits,0)==0):
            continue
       rbinlist.append(bits)
       i+=1
      
def send():
    print("\n=============Sender=============")
    data=input ("\nEnter your data: ")
    bindata(sbinlist ,data) 
    print("The sender Encoded Dataword: ",sbinlist)
    countbit(scountlist,sbinlist,0)
    print("Total on bits: ",scountlist)
    AddParity()
    print("The sender Codeword: ",sbinlist,"\n")
    print("================================")
def recieve():
    print("\n=============Reciever=============\n")
    Recieve_data(len(sbinlist))
    countbit(rcountlist,rbinlist,1)
    print("Total on bits: ",rcountlist)
    CheckParity()
    print("================================")

sbinlist=[];rbinlist=[];scountlist=[];rcountlist=[]
send()

recieve()

