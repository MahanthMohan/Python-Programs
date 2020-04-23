def increment(max):
    for i in range(1,1000):
        lst = []
        lst = lst.append[i]
        print(lst)
        return lst

def removeOdd(lst):
    list_len = len(lst)
    for n in range(0, list_len):
        lst = lst[0][n]
        print(lst)
        return(lst)

Max = 1000
filtered_list = removeOdd(increment(Max))
list_length = len(filtered_list)

while(list_length < 1):
    filtered_list = removeOdd(filtered_list)
    list_length = len(filtered_list)
    print(filtered_list)


