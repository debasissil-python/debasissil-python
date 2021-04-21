input_storage = []
openings = ('why','how','where','when','what')

while True:
    a = input("Say Something: ").capitalize()
    
    if a == '/end':
        break 
    elif a != '/end':
        input_storage.append(a)
        continue 

if a.startswith(openings):
    c = '? '.join(input_storage)
else:
    c = '. '.join(input_storage)    

print (c)

