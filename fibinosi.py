def fibonacci_upto(limit):
   a, b = 0, 1
   series = []
   while a <= limit:
       series.append(a)
       a, b = b, a + b
   return series
# Example usage:
num = int(input("Enter the maximum number: "))
print(f"Fibonacci series up to {num}: {fibonacci_upto(num)}")
