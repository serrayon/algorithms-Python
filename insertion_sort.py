import time 
def insert(list_a):
    indexing_length = range(1,len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]
        
        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1 
    return list_a

def main():
    st = time.time()
    bin =[423,-2,0,33,-2,66,90,66,-.5]
    #print (insert([4,34,1,0,9,0,9,1,2,7,0 -3, -3, .5, 432154]))
    print (insert(bin))
    et = time.time()
    elapsedTime = et - st 
    print(f'Elapsed time is: {elapsedTime} seconds')
if __name__=='__main__':
    main()


#This makes more sense the index 1 is removed, It would still work but only because its making the list from left to right
# the list is now being compared from index 0 and index 1
def insertion(integers):
    index_length = range(len(integers))
    for i in index_length:
        value_sort = integers[i]
        while integers[i-1] > value_sort and i > 0:
            integers[i],integers[i-1]=integers[i-1],integers[i]
            i = i - 1 
    return integers
bin = [9,8,7,6,5,4,3,2,1,98,7,6,5,4,6,7,345,2,2,57,3,-8,9,0,0,.8]
print(insertion(bin))
