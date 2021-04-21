input_storage = []
openings = ('Why','How','Where','When','What')

while True:
    a = input("Say Something: ").capitalize()
    
    if a == '/end':
        break 
    elif a.startswith(openings):
        input_storage.append(a + ' ?')
 
    else:
        input_storage.append(a + ' .')
        
print (''.join(input_storage))