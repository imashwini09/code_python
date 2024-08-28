def square_num(nums):
    for i in nums:
        yield (i*i)

my_nums = square_num([1,2,3,4,5])



# print(my_nums)

# To generate Next number we use next key word
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

for num in my_nums:
    print(num)


# list comprehension
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)

# generators
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)
for num in my_nums:
    print(num)

