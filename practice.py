def mean_of(number_list):
    if number_list == []:
        return None
    else:
        return sum(number_list)/len(number_list)
result = mean_of([642.1, 642.5, 643.0])
print(result)