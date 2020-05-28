def ft_reduce(function_to_apply, list_of_inputs):
    resultat = list_of_inputs[0]
    lenlist = len(list_of_inputs)
    for i in range(1, lenlist):
        resultat = function_to_apply(resultat, list_of_inputs[i])
    return resultat


# print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))
