#Aim: Membership and Identity Operators | in, not in,
def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

if overlapping(list1, list2):
    print("overlapping")
else:
    print("not overlapping")
