# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE2

from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    """Ask the user for an intitial balance"""
    savings_balance = float(input("Enter the amount of you savings balance: $"))

    """Ask the user for the interest rate"""
    savings_interest = float(input("Enter the savings interest rate in APR: "))
    
    """Ask the user for the number of months the savings interest rate must by applied"""
    savings_maturity = int(input("Enter the number of months since the initial balance: "))

    # Call the create_savings_account function and pass the variables from the user.
    #updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    updated_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print('Your updated balance in your savings accounct is $', format(updated_balance, ',.2f'))
    print('Your interest earned in your savings account is $', format(interest_earned, ',.2f'))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    """Ask the user for an intitial balance"""
    cd_balance = float(input("Enter the amount of your CD balance: $"))

    """Ask the user for the interest rate"""
    cd_interest = float(input("Enter the CD interest rate in APR: "))
    
    """Ask the user for the number of months the interest rate must by applied"""
    cd_maturity = int(input("Enter the number of months since the initial balance: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print('Your updated balance in your cd accounct is $', format(updated_cd_balance, ',.2f'))
    print('Your interest earned in your cd account is $', format(interest_earned, ',.2f'))

if __name__ == "__main__":
    # Call the main function.
    main()