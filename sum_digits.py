#Function to compute sum of digits of a number
def sum_digits(n):
  total = 0
  while n> 0:
    digit = n % 10
    total += digit
    n //= 10
  return total

print(sum_digits(167))
