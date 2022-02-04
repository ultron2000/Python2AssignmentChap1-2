# This is the annual salary calculator!

# This is the primary function, used to calculate annual salary.
def calculate():
    # This collects the hourly wage of the user.
    hourly_wage = int(input('Enter your hourly wage: $'))

    # This collects the average hours worked per week.
    hours = int(input('Enter your average hours per week: '))

    # This takes the collected hourly wage and average hours and calculates the
    # annual wage given the provided inputs.
    final_wage = str(((hourly_wage * hours) * 52))

    # Displays the calculated annual salary.
    print('Your annual salary is: $' + final_wage)


# This runs the calculate function.
if __name__ == '__main__':
    calculate()
