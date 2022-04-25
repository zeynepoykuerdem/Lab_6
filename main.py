n = int(input("Please enter a number:"))
func = lambda x: (x - 3) / x ** 2
my_list = []
for i in range(1, n + 1):
    my_list.append(func(i))
print(my_list)


def func(n):
    """This function prints the result of this equation"""

    if (n == 1):
        return (n / (n + 2))-10

    else:
        return func(n-1) * ((n / (n + 2))-10)

#find base case then find the result

print(func(2))
print(func.__doc__)

def multiplication (num_a, num_b):
    if num_a ==0 or num_b==0:
        return 0
    return num_a+multiplication(num_a,num_b-1)

#print(multiplication(3,5))
