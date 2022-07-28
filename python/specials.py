#map, lambda, list comprehension examples

nums = [1, 2, 3, 4, 5, 6, 7, 8]
def square(n):
    return n*n

#function and map
result = map(square, nums)
print (list(result))

#lambda
result = map(lambda x: x*x, nums)
print (list(result))

#map and lambda
result = map(lambda x, y: x * y, nums, nums)
print(list(result))

#list comprehension
squares = [x**2 for x in nums]
print(squares) 