UI = 0
while True:
  try:
     UI = int(input("Enter something: "))       
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break 
