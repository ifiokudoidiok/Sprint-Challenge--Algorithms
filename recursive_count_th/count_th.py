'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
'''
function takes in string
convert string to array/list
Check for letters t and h in the list
if they have indices of [i] and [i+1] increase count
else return count = 0
==> base case returns count = 0
'''
# def demo(str_num):
#     sum = 0
#     for i in range(len(str_num)):
#         if str_num[i] == 't' and str_num[i+1] == 'h':
#             sum += 1
#     return sum
# # print(demo('thetha'))


def count_th(word):
    count = 0
    index = 0
    if len(word) < 2:
        return count
    elif word[index] == 't' and word[index+1] == 'h':
        count += 1
        return count + count_th(word[1:])
    return count_th(word[1:])
    # TBC
print(count_th('thethth'))
