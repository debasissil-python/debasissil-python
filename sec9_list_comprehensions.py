# ALWAYS REMEMBER ---->
                    # For list comprehension with or without if statement, the code should be -
                    # [a for a in list if a>10] ---> It'll iterate through the list and give the output

                    # For list comprehension with if else statement, the code should be -
                    # [a if a>10 else 'none' for a in list] ---> The for loop goes at the very end
                    

#l = [99, 95, 94,'no data']
#def func(l):
#   new_l = [num for num in l if isinstance(num, int)]
#   print (new_l)

#int_list = [2,3,5,'hallo']
#def func(int_list):
#    new_list = [i for i in int_list if isinstance(i, int)]


# if else statement
#list = [2,3,78,65,0,100]
#new_list = [n if n > 50 else 'Below Grade' for n in list ]
#print (new_list)


# if else statement
#list = [2,3,78,65,0,100,'hhh', 'xxx']
#new_list = [a > 50 if isinstance(a, int) else 'A Str' for a in list]
#print (new_list)


# if else statement
#list = [2,3,78,65,0,100,'hhh', 'xxx']
#new_list = [a > 50 for a in list if isinstance(a, int)]
#print (new_list)


# if else statement
#list = [2,3,78,65,0,100,'hhh', 'xxx']
#new_list = [a for a in list if isinstance(a, int)]
#print (new_list)


# if else statement
#list = [2,3,78,65,0,100,'hhh', 'xxx']
#new_list = [a for a in list if isinstance(a, int) if a>50]
#print (new_list)



l = [ 2, 3, 6, 'no num', 'all num']
#new_l = [a if isinstance (a, int) else a == 0 for a in l] 
#print(new_l)
n_l = [a for a in l]
n_l_1 = [a for a in l if isinstance(a, int)]
n_l_2 = [a if isinstance(a, int) else 0 for a in l]
n_l_3 = [a if not isinstance(a, str) else 0 for a in l]
print (n_l)
print (n_l_1)
print (n_l_2)
print (n_l_3)

lst = [65,98,32,'lkjh','poiu']
def func(lst):
    return [a if isinstance(a, int) else 0 for a in lst]
print (func(lst))   

# A list comprises of str with floating numbers. Output needs to be sum of all those numbers and 
# changing them to float


#l = [99.3, 95.8, 94.5]

#def func(l):
#    return sum(l)
#print (func(l))


lst = ['99.3', '95.8', '94.5']
#def func(lst):
#    return sum([float(a) for a in lst])
#print (func(sum([float(a) for a in lst])))


n_l = sum(float(a) for a in lst)
print (n_l)



