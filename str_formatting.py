name = input("What's Your Name: ")
surname = input ("And Your surname please: ")
age = input('May we know your age: ')
address = input("Where do you live: ")

work = input("What do You do: ")
move = input ("Do you want to relocate to Canada: ")
where = input('Which Province: ')
when = input("When can You relocate: ")

job = input ("Do you have a job: ")
search = input('Have You searched: ')
need = input ("Do you need a job: ")
how_many = input ('How many jobs: ')


total = "Hallo %s %s ! You are %s and you live in %s ." % (name, surname, age, address)

thoughts = f"You are {work} and it's a {move} that you want to come to {where} {when}"

jobs = "You {} but {}. You {} and I recommend you will need {}.".format(job, search, need, how_many)

print (total)
print(thoughts)
print(jobs)




