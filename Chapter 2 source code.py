# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:nomarker
#     text_representation:
#       extension: .py
#       format_name: nomarker
#       format_version: '1.0'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Source code for Chapter 2

# ### Table of contents
#
# - [Displaying output with the print function](#Displaying-output-with-the-print-function)
# - [Variables](#Variables)
# - [Reading input from the keyboard](#Reading-input-from-the-keyboard)
# - [More on formatting output](#More-on-formatting-output)

# ### Displaying output with the print function

print("Hello!")  # Note that we can use either double or single quotation marks
print('Kate Austen')
print('123 Full Circle Drive')
print('Asheville, NC 28899')

print("Don't fear!") # If we want to display an apostrophe in a string value, we have to use the double quotation marks
print("I'm here!")
print('Your assignment is to read "Hamlet" by tomorrow.') # To display a double quotation marks, use the single quotation marks

# We use triple quotes to display output with multiple lines
print("""Hello
Good morning!
How are you?""")

# ### Variables

# Simple variable types
fname = "Kevin" # String or text
hours_worked = 8 # Integer
hourly_rate = 20.50 # Float or numbers with decimal places
has_a_degree = True # Boolean which takes either True or False value
type(has_a_degree)

# If we want hours_worked to become a float variable, we can cast its type
hours_worked = float(8)
type(hours_worked)
# Other common type casting functions are int() and str()

# A rectangle has a width of 5 units and length of 10 units
width = 5 # Assigning a value of 5 to a variable called width
length = 10 # Assigning a value of 10 to a variable called length
print(width) # Using the print function to display the value of a variable
print(length)
# Note that Python is case sensitive. Therefore, using print(Length) or print(Width) will cause an error

print(f'Width = {width}') # Using print and F-strings to format the output
print(f'Length =  {length}')
print("Calculating the area of the rectangle")
print(width * length) # Can you modify the last two lines and F-strings to format the output for the area of the rectagle?

# Variables can also have text or string values
customer_id = "123456789"
customer_fname = 'Kevin'
customer_lname = 'Lertwachara'
customer_fullname = customer_fname + " " + customer_lname # The + sign concatenates two string variables
print(customer_id + ": " + customer_fullname)
# Consider the previous example, can we use the following statement: print("Width =" + width)? Why/Why not?
# What if we use this statement: print("Width = " + str(width))?
# Or what if we use this statement: print("Width = " , width)

# ### Reading input from the keyboard

customer_id = input("Please enter your customer ID")
customer_fname = input("Tell me your first name")
customer_lname = input('Tell me your last name')
customer_fullname = customer_fname + " " + customer_lname
print(customer_id + ": " + customer_fullname)

width = input("Enter the width of a rectangle")
length = input("Enter the length of a rectangle")
print("Calculating the area of the rectangle")
print(float(width) * float(length)) 
# The float function converts the input into numerical values with decimal places. # The int function converts the input into integers 
# The str function converts a number into a string/text value

area = float(width) * float(length)
print(f'The area of the rectangle is  {area:.4f}.') #Using the F-strings to format a numerical output with 4 decimal places

# ### More on formatting output

# A floating-point number is displayed with no formatting.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment}.')

# A floating-point number can be rounded.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment:.2f}.')

# A floating-point number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay:,.2f}')

# A floating-point number can be displayed as percentage.
discount = 0.12
print(f'{discount:%}')
print(f'{discount:.2%}')

# A floating-point number can be displayed in scientific notation.
number = 12345678.9213457
print(f'{number:e}')
print(f'{number:.2e}')

# Formatting integer values in the output
number = 1234567890
print(f'{number:d}')
print(f'{number:,d}')
print(f'Displaying a number: {number:,d}')

# [Back to the TOC](#Table-of-contents)


