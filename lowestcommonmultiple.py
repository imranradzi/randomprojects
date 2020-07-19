# program to return list of prime factors that make up the lowest common multiple of 2 numbers
# inputs for numbers are the list containing their prime factors (including repetitions)
# based on the output of primefactors, since it returned a list of prime factors


def lcm(list1, list2):
    product1 = 1
    product2 = 1
    product3 = 1

    for a in list1:
        product1 *= a

    for b in list2:  # blocks of code just to compute the product of the elements of the list
        product2 *= b  # basically just to find the original number associated with the prime factors in the list

    for i in list2:
        list1.append(i)  # merges both list together

    for j in list1:
        product3 *= j  # multiplies all the elements in the list to get a common multiple of the two numbers

    index = 0
    for k in list1:
        # for each element in the new list we made, divide prod3 by it and see if both numbers divide prod3
        # deletes that element if it indeed satisfies that condition
        # once loop's done, we've basically got a list of prime factors that make up the smallest such number
        # divisible by both number
        if (product3 / k) % product1 == 0 and (product3 / k) % product2 == 0:
            list1.pop(index)
            product3 = product3 / k
        index += 1

    list1.sort()

    prodend = 1
    # include this block of code if you want the lowest common multiple alongside the list of the prime factors the make up the lcm
    for z in list1:
        prodend *= z
    print(prodend)

    return list1
