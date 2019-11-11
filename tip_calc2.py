# SPLIT THE BILL


service_good = 0.2
service_fair = 0.15
service_bad = 0.1
service_whatevs = 0.05

total_bill = float(input("Total bill amount? $"))

level_of_service = input("Level of service? ")

split_by = int(input("Split by how many ways? "))



if level_of_service == "good":
    service_amount= service_good
elif level_of_service == "fair":
    service_amount = service_fair
elif level_of_service == "bad":
    service_amount = service_bad
else: 
    service_amount = service_whatevs

# print("total amount: %2f" % (total_amount, ))
# Placeholder for a float, showing only two decimals.
# ", " is a tuple. a tuple with only one item must have a comma.
# If you leave it off, python will forgive you but only for string interpilation.

tip_amount = (total_bill * service_amount)
total_amount = total_bill + tip_amount

print(f"Tip amount: ${tip_amount}")
print(f"Total amount: ${total_amount}")
rounded_amount_per_person = round(total_amount /split_by, 2)
print(f"Amount per person: ${rounded_amount_per_person}")