to_do = ["call a client", "do the laundry", "study at noon", "Go to the gym"]

for index, value in enumerate(to_do):
   print(f"{index + 1}. {value}")

user = input("Pick your task today: ")
to_do.append(user)

print("Task added successfully!")

for index, value in enumerate(to_do):
   print(f"{index + 1}. {value}")

choice = int(input("Enter the number you want to update: "))

index = choice - 1
if index >= 0 and index < len(to_do):
   user2 = input("Enter a new task: ")
to_do[index] = user2

for index, value in enumerate(to_do):
   print(f"{index + 1}. {value}")

user3 = int(input("Enter the number you want to delete: "))
index = choice - 1
if index >= 0 and index < len(to_do):
   to_do.pop(index)
 
for index, value in enumerate(to_do):
   print(f"{index + 1}. {value}")

print("Task delete successully!")
  
   







   


      
    
      

    
