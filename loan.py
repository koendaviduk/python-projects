
# Get details of loan
money_owed = float(input('How much money do you owe, in dollars?\n')) 
apr = float(input('What is the annual percentage rate of the loan?\n')) 
payment = float(input('How much will you pay off each month in dollars?\n')) 
months = int(input('How many months do you want to see the results for?\n')) 

# setting global variable to calculate interest rate
monthly_rate = apr/100/12

for i in range(months):
    # local variable for interest paid monthly
    interest_paid = money_owed * monthly_rate

    # local variable for running total
    money_owed = money_owed + interest_paid
    
    # loop to check when the payment goes negative to calculate the total months that it took to pay 
    # and to check what the final payment was before going negative
    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break

    # calculating the final amount owed each month with the payments being subtracted
    money_owed = money_owed - payment

    # printing the monthly payment + interest paid every interval (months)
    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('Now I owe', money_owed)