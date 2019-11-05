def allowed_dating_age(my_age):
    girls_age = my_age/2 + 10
    return girls_age

Buckys_limit = allowed_dating_age(27)
print("Bucky can date girls",Buckys_limit,"or older")

# now we gonna do some multiple exampples

Rahuls_limit = allowed_dating_age(15)
print("Rahul can date girls",Rahuls_limit,"or older")

sandys_limit = allowed_dating_age(75)
print("sandy can date girls",sandys_limit,"or older")
