def ft_filter(function_to_apply, list_of_inputs):
    resultat = []
    for inputs in list_of_inputs:
        if function_to_apply(inputs) is True:
            resultat.append(inputs)
    return resultat

# number_list = range(-5, 5)
# less_than_zero = ft_filter(lambda x: x < 0, number_list)
# print(less_than_zero)
