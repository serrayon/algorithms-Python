import time

def quick(sequence):
    length = len(sequence)
    if length <= 1:
        return  sequence
    else:
        pivot = sequence.pop()
        
    greater_list = [ ]
    lower_list = [ ]
    
    for item in sequence:
        if item > pivot:
            greater_list.append(item)
        else:
            lower_list.append(item)
            
    return quick(lower_list) + [pivot] + quick(greater_list)

def main():
    st = time.time()
    bin = [45,-3,0,64,8765876,23,23,.2]
    #print (quick([3,6,54,12,78,9,0,0,2,1,2,-9,4321542,.5,-5,-5,-.5,-10,-10]))
    print (quick(bin))
    et = time.time()
    elapsedTime = et - st 
    print(f'The elapsed time is: {elapsedTime} seconds')
if __name__ == '__main__':
    main()
