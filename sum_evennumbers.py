def sum_even_numbers(numbers):
  sum_even = 0
  for number in numbers:
    if number % 2 == 0:
      sum_even += number
  return sum_even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even_numbers = sum_even_numbers(numbers)
print(f"The sum of all even numbers in the array is: {sum_of_even_numbers}")