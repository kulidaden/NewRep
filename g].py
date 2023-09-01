# list=[1,2,4.6,'audi','bmw','zoo',12,12,34,45,23,4,234,234,234,1]
# litr=[]
# for index, enumerate in enumerate(list):
#     print('index:', index , '  value:',  enumerate)
#
# for i in set(list):
#     litr.append(i)
# print(litr)
# print("\n")
#
#
# print(list)
# print("\n")
#
# print(litr)
# print("\n")
# dict_info=dict(zip(list,litr))
# print(dict_info)


# \\\\\\\\\\\\\\\\\\\


# num_1=[i for i in range(1,10)]
# print(num_1)
#
# num_1=[i**2 for i in range(1,10)]
# print(num_1)
#
# num_1=[i for i in range(-10,10)]
# print(num_1)

# \\\\\\\\\\\\\\\\\\\

# def get_min_max_num(numbers):
#
#     numbers = list(filter(lambda x: type(x)==int or type(x)==float, numbers))
#
#     for index, enumerate1 in enumerate(numbers):
#         print('index:', index , '  value:',  enumerate1)
#
#     get_min = min(numbers)
#     get_max = max(numbers)
#     print('min:', get_min)
#     print('max:', get_max)
#
# nums=[1,2,4,65,7,54,-83433.4,3,223,1-873,52,-4,'j','er','g',2,-4]
# get_min_max_num(nums)

# ////////////////////////

# join=['ABraKadabra is','a taxi\n number','24']
# j2=' '.join(join)
# print(j2)

# /////

# join=['ABraKadabra is','a taxi\n number','24']*2
# print(join)

# ///////


list=['lower','higer','324','al3yyrtyrty42','disignore','hello']
list.sort()
print(list)
list.reverse()
print(list)



for index,elements in enumerate(list):
    print('index: ',index,"elements: ", elements)

list=" ".join(list)
print(list)