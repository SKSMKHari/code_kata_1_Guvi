UI = 0
while True:
  try:
     UI = int(input("Enter something: "))       
  except ValueError:
     print("No!")
     continue
  else:
     print("Yes!")
     break 
