#.implement a recursive function  to calculate the factorial of a given number.
def fact_rec(n):
  if n == 0 or n == 1:
   return  1
  else:
   return  n * fact_rec(n - 1)


number  = int(input("Enter the value:"))
res = fact_rec(number)

print("The factorialof{}is{}.".format(number, res))
             

