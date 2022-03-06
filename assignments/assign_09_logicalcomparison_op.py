# A bank offers loan to customer if following criteria is met:
# Age of the customer is in between 21 to 35 years.
# Salary of customer is greater than 25000 per month.
# Write a program to perform below operations:
# Read the inputs, age and salary from the user.
# Verify if above criteria is met or not and print “Customer eligible for loan.”
# if above criteria is met otherwise print “Customer is not eligible for loan at present.”
# Note: Use if elif else statement
age = int(input("Enter age between 21 to 35 years: "))
salary = int(input("Enter salary: "))

cust_age_low_limit = 18
cust_age_up_limit = 35
cust_sal_limit = 25000

if cust_age_low_limit <= age <= cust_age_up_limit and salary >= cust_sal_limit:
    print("Customer is eligible for loan.")
else:
    print("Customer is not eligible for loan.")
