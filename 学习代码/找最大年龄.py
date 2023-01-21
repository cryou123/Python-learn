person = {"Zhang san":18,"Li hua":20,"Li xiang":22}
def find_maxage(dict):
    age = 0
    for key,value in dict.items():
        if value > age:
            age = value
            name = key
    print(name)
    print(age)
find_maxage(person)