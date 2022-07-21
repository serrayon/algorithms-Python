def linear_search(input_list, target_value):
    input_list.sort()
    for each in input_list:
        if each==target_value:
            return True, 
    return None
    
    
def main():
    
    bin = [3,2,6,73,4,65,7,678,3]
    target_1 = 2
    print (linear_search(bin,target_1))
    print (bin)
if __name__ == '__main__':
    main()

    
    
def linear(input_list, target):
    
    input_list.sort()
    global index
    index = input_list.index(target)
    
    for each in input_list:
        if each == target:
            return True
    return linear
def main():
    bin = [3,2,6,73,4,65,7,678,3]
    target_1 = 2
    print(linear(bin, target_1)) 
    print('The index of', target_1, 'is',index )
    print('The ordered bin is\n',bin)
    
if __name__ == '__main__':
    main()
    
