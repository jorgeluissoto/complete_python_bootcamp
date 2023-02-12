print("Welcome to the tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to the bill?"))

tip_as_percent = int(tip)/ 100

total_tip_amount = bill* tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/ people

final_amount = round(bill_per_person, 2)
# adds a zero at the end when one isnt
final_amount2 = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount2}")