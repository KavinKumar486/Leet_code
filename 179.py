arr = [1, 2, 20]

def custom_cmp(n1, n2):
    if str(n1) + str(n2) > str(n2) + str(n1):
        return -1
    else:
        return 1

arr.sort(key=lambda x: (str(x), -x), cmp=custom_cmp)
print(arr)
