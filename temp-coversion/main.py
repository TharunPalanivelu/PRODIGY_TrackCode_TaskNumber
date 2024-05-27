def cel_to_far (input):
  return (input*9/5)+32
def far_to_cel (input):
  return (input-32)*5/9
def cel_to_kel (input):
  return input+273.15
def kel_to_cel (input):
  return input-273.15

con=int(input("which covertion you wanna perform :\nenter\n1 for (celsius to farheit)\n\n2 for (farnheit to celsius)\n\n3 for (celsius t kelvin)\n\n4 for (kelvin to celsius)\n=>"))
temp=float(input("enter the temperature :"))

if con == 1:
  print(f"The converted value is {cel_to_far(temp)}")
elif con == 2:
  print(f"The converted value is {far_to_cel(temp)}")
elif con == 3:
  print(f"The converted value is {cel_to_kel(temp)}")
elif con == 4:
  print(f"The converted value is {kel_to_cel(temp)}")
else:
  print("invalid input")