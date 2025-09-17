# how to create a function that passes data 

# step 1: create a function definition
def doordashrefund(username, refundamount): 
    print('sorry ' + username + ' for your missing food. ')
    print('we will refund you $' + refundamount + ' in 2-3 days.')
 
# step 2:call the function/execute instruction
doordashrefund('Michael B. Jordan', str(35.16))
# how to creat a function that passes data 

def birthdayemail(name, birthdate):
    print('hello, my name is ' + name)
    print('And my birthday is ' + birthdate)
birthdayemail('Michael B. Jordan', 'feb 9th')


def pape(dollar):
    pennie=dollar*100
    print('my ' + str(dollar) + ' dollars is equals to ' + str(pennie) + ' pennies' )
pape(4765)

def triangle(length, width):
    area = length*width*0.5
    print('the area of a triangle is ' + str(area))

triangle(20, 15)


def temp(Fahrenheit):
    celsius = Fahrenheit-32 * 5.9 
    print('the temperature today in Fahrenheit is ' + str(Fahrenheit) + ' but ' + str(celsius) + ' in celsius' )  

temp(32)

# test