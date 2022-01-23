# this is based on a string search in the example from the book 
# the author used liner search for an intger array and had i,j,k variables in 
# methode signature
def search(array,key, index):
    if len(array) == 0 :
        return -1
    index +=1
    if array[0] == key:
        return index;
    
    array.pop(0)
    return search(array,key,index)

searchArray = ["aram","hozan","alle","mohammed","kale","john"]
foundIndex = -1
key = "alle2"
print(search(searchArray,key, foundIndex))
