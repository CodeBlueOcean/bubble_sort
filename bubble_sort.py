# Bubble sort
# Takes unordered list and orders it 
# Traverse a list from front to end repeatedly
# Large values "bubble" to end of list

# example
# 65 3 100 10 
# Start a front and compare first two items (index 0 and 1)
# 3 65 100 10
# Swap if values are out of order, since is in correct order no need
# No swapping needed if values are in correct order 
# Reaching last pair of items indicates end of first full traversal of list 
# If list is not fully sorted, repeat the traversal 
# Swap 100 and 10 
# 3 65 10 1000
# Going back to the begining, same process, 
# (3 65) no need to do anything 
# Algorithm is done when list is sorted 
# Swap 10 and 65 
# Then you reached to the end of, no need to swap. 
# 3, 10, 65, 100 Bubble Sort, is a brute force technquie

# Introduction to Bubble Sort