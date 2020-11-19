mylist = [1, 1, 2, 15, 16, 24]
print(mylist[3])
var = mylist
var[3] = 2 * var[3]
print(var)
print(len(mylist))
i = int(len(mylist) / 2)
print(i)
list(range(i-1, i+1))

print(mylist[i-1:i+1])
print((mylist[i-1] + mylist[i]) / 2)
start = 0
end = 3

list2 = [4, 8 , 15, 16, 23, 42]
print(list2[:1])

print(list2[10])


i = list(range(start, end + 1))
print(i)

mylist.pop(0, 1, 2)




def remove_middle(lst, start, end):
    i = list(range(start, end + 1))
    lst = lst[]


def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst

mylist = mylist + mylist[-2:]
print(mylist)
lst = lst + lst[-2:]


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

def combine_sort(lst1, lst2):
    print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Try and except
def double_index(lst, index):
  try:
    lst[index] = 2 * lst[index]
    return lst
  except:
    return lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
index = 0

while len(students_in_poetry) < 6:
    students_in_poetry.append(all_students.pop(index))
    index += 1
print(all_students.pop(0))

lst2 = ["ali", "sheikhpour", "mexico"]
lst3 = "ali"
lst3[0]
