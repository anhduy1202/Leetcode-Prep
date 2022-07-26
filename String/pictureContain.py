data = [
    ("cat","yes"),
    ("cat","yes"),
    ("cat","yes"),
    ("dog","no"),
    ("dog","yes"),
    ("dog","no"),
    ("dog","no"),
    ("giraffe","no"),
    ("giraffe","no"),
    ("giraffe","no"),
]


def test(tuple,data):
    yes_filtered_animal = list(filter(lambda t: t[0] == tuple[0] and t[1] == "yes",data))
    no_filtered_animal = list(filter(lambda t: t[0] == tuple[0] and t[1] == "no",data))
    if len(yes_filtered_animal) >= len(no_filtered_animal) and tuple[1] == "yes":
        return True
    if len(no_filtered_animal) >= len(yes_filtered_animal) and tuple[1] == "no":
        return True
    else:
        return False  

def test2(tuple,data):
    count = 0 
    for animal in data:
        if animal[0] == tuple[0]:
            if animal[1] == "yes": count += 1
            else: count -=1
    if count >= 0 and tuple[1] == "yes":
        return True
    if count < 0 and tuple[1] == "no":
        return True
    else:
        return False 


print(test2(("cat","yes"),data))
print(test2(("dog","yes"),data))
print(test2(("giraffe","no"),data))