from tabulate import tabulate

max=0
row=[["Serial no.","NAME","PHONE NO","ADDRESS"]]
class phonebook:
  def __init__(self,name,phone,address):
    self.name=name
    self.phone=phone
    self.address=address
  def myfunc(p):
    i=1
    global row
    x=[]
    x.append(i)
    x.append(p.name)
    x.append(p.phone)
    x.append(p.address)
    row.append(x)
    i+=1

def custom(a,b):
  if(b==1):
    p[a-1].name=input("Enter new name\t")
    
  elif(b==2):
    p[a-1].phone=int(input("Enter new number\t"))
    
  elif(b==3):
    p[a-1].address=input("Enter new address\t")
    
  else:
    while(ser<100):
      name=input("Enter name\t")
      phone=int(input("Enter phone number\t"))
      address=input("Enter address\t")
      res=input("Do u want to add more numbers?[y/n]\t")
  
      p[ser]=phonebook(name,phone,address)
      
      if(res=="y"):
        ser+=1
    
      else:
        ser=100

p=[]
for ele in range(100):
  p.append("p"+str(ele))

ser=0
while(ser<100):
  name=input("Enter name\t")
  phone=int(input("Enter phone number\t"))
  address=input("Enter address\t")
  res=input("Do u want to add more numbers?[y/n]\t")
  max+=1
  p[ser]=phonebook(name,phone,address)
  
  if(res=="y"):
    ser+=1
    
  else:
    ser=100
  

flag=True
while(flag==True):
  row=[["Serial no.","NAME","PHONE NO","ADDRESS"]]
  print("\tPHONEBOOK\n\n")
  num=0
  for xe in range(max):
    p[num].myfunc()
  print(tabulate(row))
  res=input("Do u want to customize any data?")
  if(res=="y"):
    a=int(input("Which serial number contact do u want to change?(to add new number type 0)\t"))
    b=int(input("Press 1 to change name 2 to change phone number 3 to change address\t"))
    custom(a,b)
  if(res=="n"):
    flag=False
  

