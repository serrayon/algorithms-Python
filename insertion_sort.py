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
