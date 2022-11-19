from tabulate import tabulate  #To use tables in python

max=0 #When producing new tables it will tell us how many times we have to append datas in a row
row=[["Serial no.","NAME","PHONE NO","ADDRESS"]]  #1ST ROW OF TABLE

#A class is created to store details of individual like name , phone ,address
class phonebook:
  def __init__(self,name,phone,address):
    self.name=name
    self.phone=phone
    self.address=address
  #A method that would add the datas of class in a row of table(ie. x)
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

 #A function to customise tables
def custom(a,b):
  #COMMITING CHANGES ACCORDING TO CHOICES
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
#GENERATING 100 INDIVIDUAL ENTRIES to store data in the phonebook class
p=[]
for ele in range(100):
  p.append("p"+str(ele))

#TAKING DATAS TO ADD IN PHONEBOOK
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
  
#PUTTING A FLAG WHICH TELLS SYSTEM WHEN TO MAKE TABLES AND WHEN TO STOP
flag=True
while(flag==True):
  row=[["Serial no.","NAME","PHONE NO","ADDRESS"]]#RENEWING THE  2D TABLE WITH ONLY FIRST ROW
  print("\tPHONEBOOK\n\n")#TABLE HEADING 
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
  

