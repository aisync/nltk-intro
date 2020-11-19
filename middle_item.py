# Create a function called middle_element that has one parameter named lst.
#
# If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
#Write your function here
def middle_element(lst):
  i =  int(len(lst) / 2)
  if len(lst) % 2 == 0:
    # even
    return (lst[i-1] + lst[i]) / 2
  else:
    return (lst[i])



#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
