def is_sorted(array):
    if len(array) == 1 :
        return True
    if array[0] <= array[1]:
        array.pop(0)
        return is_sorted(array)
    else:
        return False

sample = [11,15,24,66,90,100]
print(is_sorted(sample))
