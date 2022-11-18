import time
def linear_search(input_list, target_value):
    input_list.sort()
    for each in input_list:
        if each==target_value:
            return True, 
    return None
    
    
def main():
    st = time.time()
    bin = [3,2,6,73,4,65,7,678,3]
    target_1 = 2
    print (linear_search(bin,target_1))
    print (bin)
    et = time.time()
    elapsedTime = et - st 
    print(f'The elapsed time is: {elapsedTime} seconds')
if __name__ == '__main__':
    main()

    #deleted the index was not working, figure it out later
def linear(input_list, target):
    input_list.sort()
    
    for each in input_list:
        
        if each == target:
            
            return True, target, input_list
    return False
def main():
    bin = [3,2,6,73,4,65,7,678,3]
    target_1 = 2
    print(linear(bin, target_1)) 
    print('The ordered bin is\n',bin)
    
if __name__ == '__main__':
    main()
