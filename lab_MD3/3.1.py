with open('C:\\Users\\liviu\\Desktop\\lab_MD3\\Data\\matrix.txt', 'r') as f:
    data = f.read().splitlines()

people_list = data[0].split(" | ")
people_list[0] = people_list[0][5:]
nr_ppl = 20
people = {}
adj_matrix = []
for i in range(1, nr_ppl + 1):
    line = data[i]
    temp = []
    for j in line:
        if j.isdigit():
            temp.append(int(j))
    adj_matrix.append(sum(temp))

for i in range(nr_ppl):
    people[people_list[i]] = adj_matrix[i]

most_friends = max(people, key=people.get)
print(f"The person with the most friends is {most_friends} and he has {people[most_friends]} friends")