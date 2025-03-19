def powerof4(number):
    count = 0

    if(number &(~(number and (number - 1)))):


        while(number > 1):
            number >>= 1
            count += 1

        if(count % 2 == 0):
            return True
        else:
            return False

number = int(input("Enter your number : "))
if(powerof4(number)):
    print(number, "The number is power 4")
else:
    print(number, "The number is not power 4")