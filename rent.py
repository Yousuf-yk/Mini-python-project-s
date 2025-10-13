#in this project the rent is calculated and divide by n number of person living in house

rent = int(input("enter the rent of flat = "))
food = (int(input("enter the amount spend on food/grocries = ")))
electricity_bill = int(input("enter the electrictiy bill = "))
per_unit_charge_of_electricity = int(input("enter the current electricty charge per unit = "))
person = int(input("enter the total member's in flat = "))

total = (electricity_bill * per_unit_charge_of_electricity )
output = (rent + food + total) // person
print("total amount is:",rent + food + total)
print("each person has to pay:",output)
