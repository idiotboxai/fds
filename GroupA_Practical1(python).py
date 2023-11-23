#"List of students who play both Cricket and Badminton
def intersection(list1, list2):
    x = []
    for i in list1:
        for j in list2:
            if i == j:
                x.append(i)
    print("List of students who play both Cricket and Badminton: ", x)
#List of students who either play Cricket or Badminton but not both
def different(l1, l2):
    y = []
    for i in l1:
        if i not in l2:
            y.append(i)
    for k in l2:
        if k not in l1:
            y.append(k)
    print("List of students who either play Cricket or Badminton but not both: ", y)
#List of students who play only Football
def only_football(l1, l2, l3):
    y = []
    for i in l3:
        if i not in l1 and i not in l2:
            y.append(i)
    print("List of students who play only Football: ", y)

# Sample data
group_a_players = ["Student1", "Student2", "Student3", "Student5"]
group_b_players = ["Student3", "Student4", "Student5", "Student6"]
group_c_players = ["Student1", "Student5", "Student7", "Student8"]

# a) List of students who play both cricket and badminton
intersection(group_a_players, group_b_players)

# b) List of students who play either cricket or badminton but not both
different(group_a_players, group_b_players)

# c) List of students who play only football
only_football(group_a_players, group_b_players, group_c_players)
