# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def orderOfallnumbers():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    thirdNumber = float(input("Enter the third number: "))
    fourthNumber = float(input("Enter the fourth number: "))

# The First Number
#  1. Test if the first number is the largest number of all.
    if firstNumber > secondNumber and firstNumber > thirdNumber and firstNumber > fourthNumber:
        # 2. If it is true, then test if the second number is greater than the third number and fourth number.
        if secondNumber > thirdNumber and secondNumber > fourthNumber:
            # 3. If it is true, then test if the third number is greater than the fourth number. Print the respective order.
            if thirdNumber > fourthNumber:
                orderOfallnumbers = firstNumber, secondNumber, thirdNumber, fourthNumber
            else:
                # 4. If it is false, then the fourth number is greater than the third number. Print the respective order.
                orderOfallnumbers = firstNumber, secondNumber, fourthNumber, thirdNumber
            # 5. Return the orderOfallnumbers.
            return orderOfallnumbers
        # 6. If the previous statements are false, then test if the third number is greater than the second number and fourth number.
        elif thirdNumber > secondNumber and thirdNumber > fourthNumber:
            # 7. If it is true, then test if the second number is greater than the fourth number. Print the respective order.
            if secondNumber > fourthNumber:
                orderOfallnumbers = firstNumber, thirdNumber, secondNumber, fourthNumber
            else:
                # 8. If it is false, then the fourth number is greater than the second number. Print the respective order.
                orderOfallnumbers = firstNumber, thirdNumber, fourthNumber, secondNumber
            # 9. Return the orderOfallnumbers.
            return orderOfallnumbers
        else:
            # 10. If nothing matches the previous descriptions, then the fourth number is the second largest number.
            # 11. Test if the third number is greater than the second number. Print the respective order.
            if thirdNumber > secondNumber:
                orderOfallnumbers = firstNumber, fourthNumber, thirdNumber, secondNumber