def counter(n_customers):
    adder = 0
    list_of_groups = {6 : 0}

    for i in list(str(n_customers)):
        adder += int(i)

    sum = adder
    
    if sum in list_of_groups:
        list_of_groups[sum] += 1
        
    else:
        new_group = {sum : 1}
        list_of_groups.update(new_group)
        
    return list_of_groups

counter("Some values")