dog_age = int(input("enter age your do :"))

human_age = 0

if dog_age < 2:
    human_age = 11
    age = dog_age*human_age
    print(f"age your doge comprea human : {age}")
else:
    human_age = 4
    result = (human_age - 2)*11
    dog_age = dog_age - 2
    age = (dog_age *human_age)+result
    print(f"age your doge comprea human : {age}")
