
# hey guys this not about your age this primarily for giving you health rating outta 200.And also
# these health scores are on basis of your age & jus create a database of peoples' health

def health_calculator(age,apple_ate,cigs_smoked):
    answer = (100 - age)+(apple_ate * 2)-(cigs_smoked * 2)
    print(answer)

rahuls_data = [15,22,0]
deepeshs_data = [13,15,0]
fathers_data = [40,30,0]
mothers_data = [37,27,0]


health_calculator(rahuls_data[0],rahuls_data[1],rahuls_data[2])
health_calculator(*deepeshs_data)
health_calculator(*fathers_data)
health_calculator(*mothers_data)