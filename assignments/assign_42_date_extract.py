# Assignment: 42
# Write a program to collect the dates of given month from the input list
# which consists of dates in format is dd/mm/yyyy.
# The collected dates should be saved into new list. If dates of given month are
# not available then "No data found." message should be displayed.
# Input:
# bill_dates = ["01/02/2019", "21/02/2019", "05/03/2019", "22/03/2019",
# "11/04/2019", "19/04/2019", "06/05/2019", "26/05/2019", "11/06/2019",
# "21/06/2019", "25/06/2019"]
# month = User Input in range 1 to 12, any other input should throw warning message.
# Sample Input:
# month = 3
# Sample Output:
# Dates of given month: ["05/03/2019", "22/03/2019"]

bill_dates = ["01/02/2019", "21/02/2019", "05/03/2019", "22/03/2019","11/04/2019", "19/04/2019", "06/05/2019", "26/05/2019", "11/06/2019", "21/06/2019", "25/06/2019"]

mnth = int(input("Enter month: "))
op_bill_dates = []

# Validate the input month
if mnth >= 1 and mnth <=12:
    for bill_dt in bill_dates:
        # split the bill to extract month
        dt_list = bill_dt.split("/")
        # second item will be month as per the format
        temp_mnth = int(dt_list[1])
        if mnth == temp_mnth:
            op_bill_dates.append(bill_dt)
        else:
            continue
    if len(op_bill_dates) > 0:
        print("Bill dates for given month: ", op_bill_dates)
    else:
        print("No data found.")
else:
    print("Invalid month entered.")
