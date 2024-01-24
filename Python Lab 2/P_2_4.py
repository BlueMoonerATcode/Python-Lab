# A Fibonacci sequence is defined as follows: the first and second terms in the sequence
# are 0 and 1. Subsequent terms are found by adding the preceding two terms in the
# sequence (Fi=Fi-1+Fi-2). WAP to find out the value of the nth term of the Fibonacci
# sequence by writing a suitable user defined function (say fib) for it.

def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

# Example usage
n = int(input ("Enter your number: "))
result = fib(n)
print(f"The",n,"th term of the Fibonacci sequence is",result)
