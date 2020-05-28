def ft_map(function_to_apply, list_of_inputs):
    resultat = (function_to_apply(inputs) for inputs in list_of_inputs)
    return resultat

# liste = ['a', 'coucou', 'HelloW']
#
# print("ft_map list :{}\nft_map {}\nmap list {}\nmap {}".format(
# list(ft_map(str.swapcase, liste)),
# ft_map(str.swapcase, liste),
# list(map(str.swapcase, liste)),
# map(str.swapcase, liste)))
