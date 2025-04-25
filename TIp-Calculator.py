print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15% "))
people = int(input("How many people to split the bill? "))
if tip == 15:
    total = (bill / people) * 1.15
elif tip >= 12:
    total = (bill / people) * 1.12
elif tip >= 10:
    total = (bill / people) * 1.10
else:
   total = (bill / people)
print("Each person should pay: $ ", round(total, 2))






