# 1. Countdown
def countdown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list    
print(countdown(5))        


#2 Print and Return
def print_and_return(list):
    for x in range(2):
        if x == 0:
            print(list[x])
        else:
            return list[x]

print_and_return([1,2])


# 3. First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))


#4. Values Greater than Second
def values_greater_than_second(list):
    newList = []
    count = 0
    if len(list) < 2:
        return False
    for x in range(len(list)):
        if list[x] > list[1]:
            count = count + 1
            newList.append(list[x])
    print(count)
    return newList

values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])


# 5. This Length, That Value
def length_and_value(size,value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList

length_and_value(4,7)
length_and_value(6,2)
