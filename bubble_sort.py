import time

def bubble(list_a ):
    
    indexing_length = len(list_a) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        
        for i in range(0 , indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a
def main():
    st = time.time()   
    print(bubble([4,9,0,1,-1,0,3,6,764576]))
    et = time.time()
    elapsedTime = et - st
    print(f'The elapsed time is: {elapsedTime} seconds')
if __name__=='__main__':
    main()
