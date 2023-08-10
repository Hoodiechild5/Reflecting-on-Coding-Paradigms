# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

from functools import reduce

# Flatten and sort array of integers in functional style  

def flatten_and_sort(nested_list):

  # Flatten nested list  
  flattened = reduce(lambda x, y: x + y, nested_list)

  # Sort flattened list
  sorted_list = sorted(flattened)

  return sorted_list


#How does this solution ensure data immutability?   
# This solution ensures data immutability by not mutating any variables. The reduce and sorted functions return new lists instead of mutating the original list.
#Is this solution a pure function? Why or why not?
# Yes, it is a pure function because it does not mutate any variables and it always returns the same output for the same input.
#Is this solution a higher order function? Why or why not?
# No, it is not a higher order function because it does not take a function as an argument or return a function as a result.
#Would it have been easier to solve this problem using a different programming style?
# No, functional programming is a good paradigm for this problem because it is easy to reason about and the solution is concise.
#Why in particular is functional programming a helpful paradigm when solving this problem?
# Functional programming is a helpful paradigm for this problem because it is easy to reason about and the solution is concise.
