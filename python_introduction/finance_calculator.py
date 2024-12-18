# Prompt the user for their monthly income
monthly_income = input("Enter your monthly income:")

# Ask for their total monthly expenses
monthly_expenses = input("Enter your total monthly expenses:")

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print results
print(f"Your monthly savings are ${monthly_savings} .")
print(f"Projected savings after one year, with interest, is: ${annual_savings} .")
