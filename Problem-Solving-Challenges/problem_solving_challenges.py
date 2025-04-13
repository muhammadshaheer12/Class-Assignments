# Problem 1: Reverse a String
def reverse_string(s):
    return s[::-1]  

# Problem 2: Count Vowels in a String
def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count  

# Problem 3: Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))  

# Example usage of all three functions

# Test for problem 1
input_string1 = "hello"
print("Reversed string:", reverse_string(input_string1))  

# Test for problem 2
input_string2 = "Apple"
print("Number of vowels:", count_vowels(input_string2))

# Test for problem 3
input_number = 1234
print("Sum of digits:", sum_of_digits(input_number))
