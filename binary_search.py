import random

def binary_search(input_list , target_value):
    '''
    Function executing binary search to find if element is in a list.
    parameters:
    - list
    - target
    return value: True/False (bool) and index
    '''
    input_list.sort()
    min_index = 0
    max_index = len(input_list) -1

    while max_index >= min_index:
        mid_index =(max_index+min_index)//2
        #print (f'min: {min_index} , mid: {mid_index} , max: {max_index}')
        if input_list[mid_index] == target_value:
            return mid_index , True
        elif input_list[mid_index] < target_value:
            min_index = mid_index+1
        else:
            max_index = mid_index-1
    return False

def main():
    #bin_list = list(range(6,501 + 1))
    #bin_list = [1,2,3,5,6,9,11,12,15,20,22,34,35,101,1111,234432]
    bin_list = [23,34,12,1,0,45,23,3,2,45,69,-2,-9]
    search_value_a = 1
    search_value_b = 69

    print (binary_search(bin_list,search_value_a)) 
    print (binary_search(bin_list,search_value_b))
    #print (bin_list)

if __name__ == '__main__':
    main()
