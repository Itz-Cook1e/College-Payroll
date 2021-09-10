# Assignment:
# Use an input prompt to ask the user to enter the name, hours worked, and hourly wage for two employees.
# Calculate the gross pay for each employee.
# Calculate the total amount of money you need to have.
# Print out the names, gross pay, and the total.
# Make sure you include comments with your name, date, and assignment name, as well as brief comments telling me what you're doing.
    
# Get data on employee one
name = input('Please enter an employee name: ')
hour = input('Hours worked: ')
wage = input('Hourly wage: ')
print(" ")

# Change str to int
hourint = int(hour)
wageint = int(wage)


# Calculates gross wage one
wage1 = hourint*wageint

# Get data on employee two
names = input('Please enter a second emplyee name: ')
hours = input('Hours worked: ')
wages = input('Hourly wage: ')
print(" ")

# Change str to int
hoursint = int(hours)
wagesint = int(wages)

# Calculates gross wage two
wage2 = hoursint*wagesint

# Reply with data
print(f"{name}'s gross pay is ${str(wage1)}")
print(f"{names}'s gross pay is ${str(wage2)}")
inbank = wage1+wage2
print(f"Make sure you have ${str(inbank)} in the bank!")

# Comment with name, date, and assignment name redacted
