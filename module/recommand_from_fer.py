cocktail_dict = {
    0:  "마티니",
    1:  "미도리사워",
    2:  "깡쏘주"
}


def recommand_from_fer(fer_score):
    result = 2
    
    if fer_score<0.3:
        result = 0
    elif 0.3<=fer_score<0.6:
        result = 1
    else:
        result =2
        print("in function")

    return cocktail_dict[result]