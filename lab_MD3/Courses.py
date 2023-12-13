print('Number of courses:')
total_courses = int(input())
print('Prerequisites:')
prerequisites = [[0]*2]*total_courses
visited = {int(x) for x in range(total_courses)}
verify, minus = list(), list()
visited_list = []
def search(graph, v):
    for i in range(total_courses):
        flag = 1
        for j in prerequisites:
            if j[0] == graph[i][0] and j[1] not in v:
                flag = 0
        if flag and graph[i][0] not in v:
            v.add(graph[i][0])
            if search(graph, v):
                return True
        if v == visited:
            visited_list.append(v)
            return True


for i in range(total_courses-1):
    prerequisites[i] = [int(x) for x in input().split()]
    verify.append(prerequisites[i][1])
    minus.append(prerequisites[i][0])

for i in minus:
    if i in verify:
        verify.remove(i)

answer = False
for i in verify:
    answer = search(prerequisites, {i})
    if answer:
        break
if answer is None:
    answer = True

print(answer)

# Example of Input:
# 4
# 1 0
# 2 1
# 3 2