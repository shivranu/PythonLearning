#Difference between the sums of odd and even digits in a given number using functions:

def sum_of_even_digits(num):
    even_sum = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
    return even_sum

def sum_of_odd_digits(num):
    """
    Returns the sum of odd digits in a given number.
    """
    odd_sum = 0
    for digit in str(num):
        if int(digit) % 2 != 0:
            odd_sum += int(digit)
    return odd_sum

def difference_between_sums(num):
    """
    Finds the difference between the sums of odd and even digits in a given number.
    """
    even_sum = sum_of_even_digits(num)
    odd_sum = sum_of_odd_digits(num)
    return abs(odd_sum - even_sum)

# Example usage
number = int(input("Enter a number: "))
diff = difference_between_sums(number)
print(f"The difference between the sums of odd and even digits in {number} is {diff}")