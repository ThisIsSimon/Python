"""
https://leetcode.com/problems/add-two-numbers/description/

list1 = [1, 2, 3]
list2 = [4, 5, 6]

321 + 654 = 975
"""


class ClassAddTwoNumbers:

    def _func_combine_numbers(list):
        """
        Loops over a given nested list and returns them together as strings
        i.e.:
        [[1, 2, 3], [4, 5, 6]]
        becomes:
        ['321', '654']
        """
        nested_numbers = []

        for i in range(len(list)):
            string = ""
            for j in range(len(list[i]) - 1, -1, -1):
                string += str(list[i][j])
                # string = string + str(list[i]) -- Why doesn't this work? Find out
            nested_numbers.append(string)

        return nested_numbers

    def _func_add_nested_list(list):
        sum_of_list = 0
        for i in list:
            sum_of_list += int(i)
        return sum_of_list


# given list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# This isn't part of the problem
# But given scalability, we should be using a function to append all given lists into one nested list

big_list = [[1, 2, 3], [4, 5, 6]]

string_list = ClassAddTwoNumbers._func_combine_numbers(big_list)
result = ClassAddTwoNumbers._func_add_nested_list(string_list)
print(result)
