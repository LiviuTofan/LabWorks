import ast

class Solution(object):
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            output += [i + [num] for i in output]
        return output

input_str = input("Enter a list of unique elements in the form [a, b, c]: ")

input_set = ast.literal_eval(input_str)
s = Solution()
result = s.subsets(input_set)
print(result)