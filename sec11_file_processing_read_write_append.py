#def func(*args):
#    return str(sorted(list(args))).upper()

#print (func('apple', 'orange', 'guava','cherry', 'blueberry', 'kiwi','lemon'))

# Define a function to read how many times a character is used in a txt file --->

#def func(char, path ='bear.txt'):
#    f = open(path,'r')
#    a = f.read()
#    return a.count(char)
#print(func('American'))
    
#def func(char,"bear.txt"):
#    file = open("bear.txt", 'r')
#    content = file.read()
#    return content.count(char)
#print(func('American'))

# To read up to 90 characters from a txt file and copy it in another txt file --->

#f = open('bear.txt', 'r')
#f_1 = (f.read(90))
#print(f_1)

#ff = open('first.txt','w')
#ff.write(f_1)
#ff.close()

#a = open('first.txt', 'r')
#a1 = a.read()

#print (a1)

# To read a full txt file and append it in another txt file --->

#with open('bear.txt', 'r')as b:
#    bear_txt = b.read()
#    b.close()

#with open('first.txt','a+')as f:
#    new_f = f.write(bear_txt)
#    f.close()

#with open('first.txt', 'r')as check:
#    print(check.read())

# Opening a new txt file and writing inside it using 'x' --->

#f = open('godzila.txt','x')
#f_w = f.write('Hallo this is Godzilla speaking')
#f.close()

# To read a full txt file and append it 'n' times in another file --->

with open ('bear.txt', 'r')as b:
    bear_read = b.read()
    b.close()
#print(bear_read)


with open("godzila.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)







