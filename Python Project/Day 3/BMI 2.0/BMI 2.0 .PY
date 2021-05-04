height = float(input("What is your height ? m: "))
weight = float(input("What is your weight ? kg: "))

bmi = round(weight/(height*height))

if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you are normal weight")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese")
else :
  print(f"Your bmi is {bmi}, you are clinically obese")