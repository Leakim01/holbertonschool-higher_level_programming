def safe_print_list_integers(my_list=[], x=0):
    jump = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            jump += 1
        except (ValueError, TypeError):
            print(end='')
    print("")
    return jump
