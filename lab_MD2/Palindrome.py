message = input()
palindrome = []
for i in message:
    palindrome.append(i)

j = 0
for i in range(len(palindrome)):
    if palindrome[i] != palindrome[len(palindrome)-i-1]:
        palindrome.insert(j, palindrome[len(palindrome)-i-1])
    j += 1
for i in palindrome:
    print(i, end = '')