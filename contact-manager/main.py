print("Welcome to contact manager\n1.To Add a contact (enter add)\n2.To view the stored contact (enter view)\n3.To delete the contact (enter delete)\n4.To close  (enter close)")

import pandas as pd
game=True
while game:
  condition=input("\nwhat you wanna do==>").lower()
#-------------------addition of data ------------------------#
  if condition=="add":
    name=input("Enter name:")
    contact=input("Enter contact number:")
    email=input("Enter mail:")
    with open("file.txt","a") as file:
      file.write(f"{name} || {contact} || {email} \n")
    print("Successfully added")
#-------------------to view the data ------------------------#
  elif condition=="view":  
    with open("file.txt","r") as file : 
      lines=[line.strip().split("||") for line in file]
      tab=pd.DataFrame(lines,columns=["Name","Contact","Email"])
    print(tab)
    print("\n")
#-------------------to delete the data ------------------------#
  elif condition=="delete":
    with open("file.txt","r") as file : 
      lines=[line.strip().split("||") for line in file]
    dname=input("Enter the name of the contact to be deleted :")
    lines=[line for line in lines if line[0].strip() !=dname]
    with open("file.txt","w") as file:
      for line in lines:
        file.write(" || ".join(line)+"\n")
    print(f"Data from {dname} is deleted\n")
#-------------------to edit the data ------------------------#
  elif condition=="edit": 
    edit=input("Enter the name of the contact to edit:")
    with open("file.txt","r") as file : 
      lines=[line.strip().split("||") for line in file]
      for line in lines:
        if line[0].strip()==edit:
          line[0]=input("enter new name:")
          line[1]=input("enter the contact number:")
          line[2]=input("enter new email :")
      else:
        print("Enter again \nWe recevied a invalid input")
    with open("file.txt","w") as file:
      for line in lines:
        file.write(" || ".join(line)+"\n")
    print(f"Data from {edit} is successfully edited ")
#-------------------to close the prompt ------------------------#
  elif condition=="close":
    print("Good Bye\nHave a wonderfull day")
    game=False
  else:
    print("Enter again \nWe recevied a invalid input")
    
    
    
    
    
    
      
        
    
    

  
        
    
    
    
  