"""
TS05 - Compulsary Task 1
Capstone Project I

financial_calulators.py allows the user to access two different
financial calculators: an investment calculator and a home loan 
repayement calculator

# Richard Tate - 16/03/2023
"""

import math

print("\nThank you for running Fin_Calc!\n")

# which calc would the user like to use?

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n\n")

calc_choice = str(input("Enter either 'investment' or 'bond' "
                         "from the menu above to proceed. "))

if calc_choice.lower() == "investment":
    # code here for investment choice
    print("\nInvestment calculator chosen\n")
    
    #set variables and which calculator to use
    deposit = float(input("Please enter the sum you'd like to invest, in GBP? £"))
    interest_rate = float(input("\nWhat's the interest rate in %? "))
    years_invested = int(input("\nAnd how many years would you like to invest over? "))
    interest_type_question = str(input("\nWhat type of interest? Please enter simple "
                              "or compound: "))
    

    # simple calc
    # REFERENCE: I used stackoverflow.com to find how to format the float number to 2 decimal places
    if interest_type_question.lower() == "simple":
        interest_type = "simple"
        print(f"\n\nCalculating total final amount using simple interest model, "
              f"with an deposit of £{deposit:.2f},  "
              f"with an interest rate of {interest_rate:.2f}%,  "
              f"over a period of {years_invested} years.\n")
        
        total_simple = deposit * (1 + ((interest_rate  / 100) * float(years_invested)))

        print(f"By the end of the {years_invested} year period you will have"
              f" £{total_simple:.2f}, having earnt £{(total_simple - deposit):.2f} in interest.\n\n\n")


    # compound calc
    elif interest_type_question.lower() == "compound":
        interest_type = "compound"

        print(f"\n\nCalculating total final amount using compound interest model, "
              f"with an deposit of £{deposit:.2f},  "
              f"with an interest rate of {interest_rate:.2f}%,  "
              f"over a period of {years_invested} years.\n")
        
        total_complex = deposit * math.pow((1+(interest_rate/100)),years_invested)

        print(f"By the end of the {years_invested} year period you will have"
              f" £{total_complex:.2f}, having earnt £{(total_complex - deposit):.2f} in interest.\n\n\n")

    else:
        print("Invalid interest type, please try again.")
        quit()              # exit from the program on incorrect input

elif calc_choice.lower() == "bond":
    # code here for bond choice
    print("\nBond calculator chosen\n")

    house_value = float(input("Please enter the value of the house, in GBP? £"))
    interest_rate = float(input("\nWhat's the interest rate in %? "))
    num_months = int(input("\nAnd how many months will you be repaying over? "))
    
    # REFERENCE: I used stackoverflow.com to find how to change the num_months string to a negative
    monthly_repayment = ((interest_rate/1200) * house_value) / (1 - ((1 + (interest_rate/1200)) ** -abs(num_months)))

    print(f"\nMonthly repayments on a house worth £{house_value:.2f}, with an interest rate of "
          f"{interest_rate:.2f}% over {num_months} months will be £{monthly_repayment:.2f}"
          f" and you'll have paid a total of £{(monthly_repayment * num_months):.2f}\n\n\n")

else:
    print("You've not entered a valid choice.  Please try again.\n\n\n")