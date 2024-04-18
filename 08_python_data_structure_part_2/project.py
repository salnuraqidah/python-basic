name = input("Enter your hobby: ")
function_hobby = input("Enter the function of your hobby: ")

hobby_dict = dict(name=name, function = function_hobby)
print(hobby_dict)
hobby_dict["year"] = 2023
hobby_dict["place"] = "Jakarta"
print(hobby_dict)