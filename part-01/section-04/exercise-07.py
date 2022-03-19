weekly_meals_at_cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
student_lunch_price = float(input("The price of a typical student lunch? "))
weekly_groceries_cost = float(input("How much money do you spend on groceries in a week? "))

weekly_cost = weekly_meals_at_cafeteria * student_lunch_price + weekly_groceries_cost

print("Average food expenditure:")
print(f"Daily: {weekly_cost / 7} euros")
print(f"Weekly: {weekly_cost} euros")