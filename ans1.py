
# a really simple test example
def f(x, y):
    return x*x + y*y

assert 2 == f(1,1)
assert 25 == f(3,4)

# implement the "FizzBuzz" algorithm
#  given an input
#    if the input is equally divisible by 3, return "fizz"
#    if the input is equally divisible by 5, return "buzz"
#    if the input is equally divisible by both 3 and 5, return "fizzbuzz"
#    otherwise, return the input
def fizzbuzz(input):
    if input % 15 == 0:
        return "fizzbuzz"
    elif input % 5 == 0:
        return "buzz"
    elif input % 3 == 0:
        return "fizz"
    else:
        return input

# write tests, using assert, to verify the operation
# here are a few to get you going
assert 1 == fizzbuzz(1)
assert "fizz" == fizzbuzz(3)
assert "buzz" == fizzbuzz(5)
assert "fizzbuzz" == fizzbuzz(15)




