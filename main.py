"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return(x)
    else:
        return(foo(x-1)+foo(x-2))

def longest_run(mylist, key):
    longest = 0
    current = 0
    for i in mylist:
        if i == key:
            current+=1
            if current > longest:
                longest = current
        else:
            current = 0   
    return(longest)

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
def combineLR(left,right):
    if left.is_entire_range == True: #Left is all key
        if right.is_entire_range == True: #and right is all key
            addlr = left.left_size + right.left_size
            return(Result(addlr,addlr,addlr,True))
        else: #left all key right is not all key
            return(Result((left.longest_size+right.right_size),right,max(left.longest_size,right.longest_size),False))
    else: #left not all key
        if right.is_entire_range == True: #and right all key
            return(Result(left,(left.right_size+right.longest_size),max(left.longest_size,right.longest_size),False))
        else: #left not all key and right not all key
            return(Result(left.left_size,right.right_size,max(left.longest_size,right.longest_size),False))

def longest_run_recursive(mylist, key):
    #Base case: List size of one
    if len(mylist) == 1:
        if mylist[0] == key:
            xresult = Result(1,1,1,True)
        else:
            xresult= Result(0,0,0,False)
    else:
        half = len(mylist)//2
        left = longest_run_recursive(mylist[:half],key)
        right = longest_run_recursive(mylist[half:],key)
        xresult = combineLR(left,right)
    return xresult

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


