contact_book = {
}

def load_contacts():
  try:
    with open("contacts.txt","r") as f:

      for line in f:
        name, number = line.strip().split(",")

        contact_book[name] = number
    
  except FileNotFoundError:
        pass
  
def save_contacts():
  with open("contacts.txt","w") as f:
    for name,number in contact_book.items():
     f.write(f"{name},{number}\n")

def add():
    a=input("enter contact name\n")
    b=input("enter contact number")
    
    contact_book[a]=b
    save_contacts()

def show():
  for key,values in contact_book.items():
    print(key,values)

# show()

def search():
   
   a=input("enter contact name ")
   print(f"{a}  {contact_book.get(a)}")

# search()

def update():
   a=input("enter contact name ")
   b=(input("enter new number "))
   contact_book[a]=b
   save_contacts()

# update()

def delete():
   a=input("enter contact name to delete")
   if a in contact_book:
    contact_book.pop(a)
    save_contacts()

   else:
    print("contact not found")



# delete()
# show()
load_contacts()
def menu():
 
 while True:
  print('''
   Choose from following options
    1.Add contact
    2.View contacts
    3.Search contacts
    4.Delete contact
    5.Update contact
    6.exit
       
 ''')
  
  try:
        a = int(input("Enter choice: "))
  except ValueError:
        print("Please enter a valid number")
        continue
  
 
  if(a==1):
   add()
  elif(a==2):
   show()
  elif(a==3):
   search()
  elif(a==4):
   delete()
  elif(a==5):
   update()
  elif(a==6):
   print("Thank you")
   break
  else:
   print("invalid option")
a = menu()
