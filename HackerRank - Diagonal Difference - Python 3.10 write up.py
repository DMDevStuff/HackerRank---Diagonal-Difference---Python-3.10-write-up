#   Given a square matrix, calculate the absolute difference between the
#   sums of its diagonals.

##### ##### ##### #####

#   An iterative solution.
#   O(n).  n is the length of two_dimensional_array.
#   Solved in one pass over the 2d array.
#   Two variables used to keep track of the indices are initalized
#   The 2d array is iterated over row by row.  At each row the index
#   variables are used to grab the appropriate values - add them to the appropriate sums -
#   and then are incremented accordingly.
#   Returns an integer.

def solutionOne(two_dimensional_array):

    left_to_right_sum = 0
    right_to_left_sum = 0

    left_index = 0
    right_index = len(two_dimensional_array) - 1

    for row in two_dimensional_array:

        left_to_right_sum += row[left_index]
        left_index += 1

        right_to_left_sum += row[right_index]
        right_index -= 1

    return abs(left_to_right_sum - right_to_left_sum)

##### ##### ##### #####

def test():

    border = '##### ##### ##### #####'

    test_case_one = [[11,2,4],
                     [4,5,6],
                     [10,8,-12]]
    expected_result_one = 15

    solution_one_test_one = solutionOne(test_case_one)

    print()
    print(border)
    print()

    print('Test Case One Result: ' + str(solution_one_test_one))
    print('Expected Result: ' + str(expected_result_one))

    print()
    print(border)
    print()

    return None
