def fibonacci(n):
  if n <= 1:
    return n
  result = fibonacci(n-1) + fibonacci(n-2)
  return result

n = int(input())
print(fibonacci(n))
