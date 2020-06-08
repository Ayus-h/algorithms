num_list = [1,54,21,54,13,68,34,112,87,43,87,54,23,32,76,65,6,8,23,26,75,27]

def quicksort(n_list):
    if len(n_list)<=1:
        return n_list
    pivot=n_list[0]
    equal,less,more=[],[],[]
    for i in n_list:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            less.append(i)
        elif i>pivot:
            more.append(i)
    
    #print(n_list)
    #print(less+equal+more)
    return quicksort(less)+equal+quicksort(more)

print("Hello")
print(quicksort(num_list))