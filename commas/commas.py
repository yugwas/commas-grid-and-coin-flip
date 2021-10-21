def comma_code(input_list):
    output = ""
    for i in range(len(input_list)):
        if i < len(input_list) - 1:
            output += (str(input_list[i]) + ", ")
        # elif i == 0:
        #     output = input_list
        #     return("List not valid!")
        else:
            output += ("and " + str(input_list[i]) + ".")
    return output


spam = ['apples', 'bananas', 'tofu', 'cats']
numbers = [1, 2, 3, 4, 5]
blank = []


print(comma_code(spam))
print(comma_code(numbers))
print(comma_code(blank))

#ask for help on list6 and list3
