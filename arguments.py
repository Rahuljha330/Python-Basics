def get_gender(sex="Unknown"):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex  = "female"
    else:
        sex = "rather not specify"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()