
import datetime
import pytz
# entering of number
number_entered = input('Enter your number: ')

# asking for correction if entered number is not an integer
while not number_entered.isdigit():
    print("Please enter a valid integer.")
    number_entered = input('Enter your number: ')

# confirming the number entered + saying today's  date
print('So today, on', datetime.date.today(),  'your number is %s\n' % number_entered)

########################## TIME ZONES

# Get the current local time
cet = pytz.timezone('CET')
local_now = datetime.datetime.now(cet)

# Print current time in CET

print('Current local CET time is ', local_now.strftime('%Y-%m-%d %H:%M:%S'))

# Set the time zone to China Standard Time (CST)

cst = pytz.timezone('Asia/Shanghai')
cst_now = datetime.datetime.now(cst)

# Format and print the local Chinese time
print('Current local Chinese time:', cst_now.strftime('%Y-%m-%d %H:%M:%S'))

########################## TIME ZONES END


# declaring the number of decimal places required
howmanydecimals = input('How many decimal places do you want to see? ')

# asking for correction if entered number is not an integer
while not howmanydecimals.isdigit():
    print("Please enter a valid integer.")
    howmanydecimals = input('How many decimal places do you want to see? ')

# converting the entered number into an integer
int_howmanydecimals = int(howmanydecimals)

# checking if the entered number of decimal places is less than 5
while int_howmanydecimals < 5:
    print("Too few! Enter a value greater than or equal to 5")
    howmanydecimals = input('Enter a higher number of decimal places: ')

# asking for correction if entered number is not an integer
while not howmanydecimals.isdigit():
    print("Please enter a valid integer.")
    howmanydecimals = input('Enter a higher number of decimal places: ')

    int_howmanydecimals = int(howmanydecimals)

# displaying the result with the desired number of decimal places
print('Here you are: %.*f' % (int_howmanydecimals, float(number_entered)))

