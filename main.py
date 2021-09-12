
print("Welcome to the tip calculator.")
Total = input("What was the total bill? ")
Tip = input("What percentage tip would you like to give? ")
People = input("How many people to split the bill? ")

Total_Int = float(Total)
Tip_Int = int(Tip)
People_Int = int(People)

Tip_cal = (Tip_Int / 100) + 1

Total_bill = int(Total_Int * Tip_cal)
Split = (round((Total_bill / People_Int),2))

print(f"Everyone needs to pay £{Split}")
