# LOOPS
# Nested Loops
# We have seen how we can go through the elements of a list. What if we have a list made up of multiple lists? How can we loop through all of the individual elements?
#
# Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
# If we want to go through each student, we have to put one loop inside another:

for team in project_teams:
  for student in team:
    print(student)
# This results in:

Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel
