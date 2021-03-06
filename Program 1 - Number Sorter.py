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
            # 3. If it is true, then test if the third number is greater than the fourth number. Display the respective order.
            if thirdNumber > fourthNumber:
                orderOfallnumbers = firstNumber, secondNumber, thirdNumber, fourthNumber
            else:
                # 4. If it is false, then the fourth number is greater than the third number. Display the respective order.
                orderOfallnumbers = firstNumber, secondNumber, fourthNumber, thirdNumber
            # 5. Return the orderOfallnumbers.
            return orderOfallnumbers
        # 6. If the previous statements are false, then test if the third number is greater than the second number and fourth number.
        elif thirdNumber > secondNumber and thirdNumber > fourthNumber:
            # 7. If it is true, then test if the second number is greater than the fourth number. Display the respective order.
            if secondNumber > fourthNumber:
                orderOfallnumbers = firstNumber, thirdNumber, secondNumber, fourthNumber
            else:
                # 8. If it is false, then the fourth number is greater than the second number. Display the respective order.
                orderOfallnumbers = firstNumber, thirdNumber, fourthNumber, secondNumber
            # 9. Return the orderOfallnumbers.
            return orderOfallnumbers
        else:
            # 10. If nothing matches the previous descriptions, then the fourth number is the second largest number.
            # 11. Test if the third number is greater than the second number. Display the respective order.
            if thirdNumber > secondNumber:
                orderOfallnumbers = firstNumber, fourthNumber, thirdNumber, secondNumber
            else:
                # 12. If it is false, then the second number is greater than the third number. Display the respective order.
                orderOfallnumbers = firstNumber, fourthNumber, secondNumber, thirdNumber
            # 13. Return the orderOfallnumbers.
            return orderOfallnumbers

# The Second Number
# 14. If the first number is not the largest number, then test if the second number is the largest number of all.
    if secondNumber > firstNumber and secondNumber > thirdNumber and secondNumber > fourthNumber:
        # 15. If it is true, then test if the first number is greater than the third number and the fourth number.
        if firstNumber > thirdNumber and firstNumber > fourthNumber:
            # 16. If it is true, then test if the third number is greater than the fourth number. Display the respective order.
            if thirdNumber > fourthNumber:
                orderOfallnumbers = secondNumber, firstNumber, thirdNumber, fourthNumber
            else:
                # 17. If it is false, then the fourth number is greater than the third number. Display the respective order.
                orderOfallnumbers = secondNumber, firstNumber, fourthNumber, thirdNumber
            # 18. Return the orderOfallnumbers.
            return orderOfallnumbers
        # 19. If the previous statements are false, then test if the third number is greater than the first number and the fourth number.
        elif thirdNumber > firstNumber and thirdNumber > fourthNumber:
            # 20. If it is true, then test if the first number is greater than the fourth number. Display the respective order.
            if firstNumber > fourthNumber:
                orderOfallnumbers = secondNumber, thirdNumber, firstNumber, fourthNumber
            else:
                # 21. If it is false, then the fourth number is greater than the first number. Display the respective order.
                orderOfallnumbers = secondNumber, thirdNumber, fourthNumber, firstNumber
            # 22. Return the orderOfallnumbers.
            return orderOfallnumbers
        else:
            # 23. If nothing matches the previous descriptions, then the fourth number is the second largest number.
            # 24. Test if the third number is greater than the first number. Display the respective order.
            if thirdNumber > firstNumber:
                orderOfallnumbers = secondNumber, fourthNumber, thirdNumber, firstNumber
            else:
                # 25. If it is false, then the first number is greater than the third number. Display the respective order.
                orderOfallnumbers = secondNumber, fourthNumber, firstNumber, thirdNumber
            # 26. Return the orderOfallnumbers.
            return orderOfallnumbers

# The Third Number
# 27. If the second number is not the largest number, then test if the third number is the largest number of all.
    if thirdNumber > firstNumber and thirdNumber > secondNumber and thirdNumber > fourthNumber:
        # 28. If it is true, then test if the first number is greater than the second number and fourth number.
        if firstNumber > secondNumber and firstNumber > fourthNumber:
            # 29. If it is true, then test if the second number is greater than the fourth number. Display the respective order.
            if secondNumber > fourthNumber:
                orderOfallnumbers = thirdNumber, firstNumber, secondNumber, fourthNumber
            else:
                # 30. If it is false, then the fourth number is greater than the second number. Display the respective order.
                orderOfallnumbers = thirdNumber, firstNumber, fourthNumber, secondNumber
            # 31. Return the orderOfallnumbers.
            return orderOfallnumbers
        # 32. If the previous statements are false, then test if the second number is greater than the first number and the fourth number.
        elif secondNumber > firstNumber and secondNumber > fourthNumber:
            # 33. If it is true, then test if the first number is greater than the fourth number. Display the respective order.
            if firstNumber > fourthNumber:
                orderOfallnumbers = thirdNumber, secondNumber, firstNumber, fourthNumber
            else:
                # 34. If it is false, then the fourth number is greater than the first number. Display the respective order.
                orderOfallnumbers = thirdNumber, secondNumber, fourthNumber, firstNumber
            # 35. Return the orderOfallnumbers.
            return orderOfallnumbers
        else:
            # 36. If nothing matches the previous descriptions, then the fourth number is the second largest number.
            # 37. Test if the first number is greater than the second number. Display the respective order.
            if firstNumber > secondNumber:
                orderOfallnumbers = thirdNumber, fourthNumber, firstNumber, secondNumber
            else:
                # 38. If it is false, then the second number is greater than the first number. Display the respective order.
                orderOfallnumbers = thirdNumber, fourthNumber, secondNumber, firstNumber
            # 39. Return the orderOfallnumbers.
            return orderOfallnumbers

# The Fourth Number
# 40. If the third number is not the largest number, then test if the fourth number is the largest number of all.
    if fourthNumber > firstNumber and fourthNumber > secondNumber and fourthNumber > thirdNumber:
        # 41. If it is true, then test if the first number is greater than the third number and the second number.
        if firstNumber > secondNumber and firstNumber > thirdNumber:
            # 42. If it is true, then test if the second number is greater than the third number. Display the respective order.
            if secondNumber > thirdNumber:
                orderOfallnumbers = fourthNumber, firstNumber, secondNumber, thirdNumber
            else:
                # 43. If it is false, then the third number is greater than the second number. Display the respective order.
                orderOfallnumbers = fourthNumber, firstNumber, thirdNumber, secondNumber
            # 44. Return the orderOfallnumbers.
            return orderOfallnumbers
        # 45. If the previous statements are false, then test if the second number is greater than the first number and third number.
        elif secondNumber > firstNumber and secondNumber > thirdNumber:
            # 46. If it is true, then test if the first number is greater than the third number. Display the respective order.
            if firstNumber > thirdNumber:
                orderOfallnumbers = fourthNumber, secondNumber, firstNumber, thirdNumber
            else:
                # 47. If it is false, the the third number is greater than the first number. Display the respective order.
                orderOfallnumbers = fourthNumber, secondNumber, thirdNumber, firstNumber
            # 48. Return the orderOfallnumbers.
            return orderOfallnumbers
        else:
            # 49. If nothing matches the previous descriptions, then the third number is the second largest number.
            # 50. Test if the first number is greater than the second number. Display the respective order.
            if firstNumber > secondNumber:
                orderOfallnumbers = fourthNumber, thirdNumber, firstNumber, secondNumber
            else:
                # 51. If it is false, then the second number is greater than the first number. Display the respective order.
                orderOfallnumbers = fourthNumber, thirdNumber, secondNumber, firstNumber
            # 52. Return the orderOfallnumbers.
            return orderOfallnumbers

# 53. Call the orderOfallnumbers.
order = orderOfallnumbers()
# 54. Print the final output.
print(f"The order of the numbers from highest to lowest is: {order}.")