list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20,4]
def mean_(x):
    return sum(x)/len(x)
# print(mean_(list1))


def median_(y):
    y = sorted(y)
    if len(y)%2 == 0:
        pos1 = y[len(y)//2]
        pos2 = y[(len(y)//2)-1]
        Med = (pos1+pos2)/2
    else:
        Med = y[len(y)//2]
    print(y)
    return Med
# print(median_(list1))

def find_most_common(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    max_count = max(count_dict.values())
    most_common_values = [i for i, value in count_dict.items() if value == max_count]
    print(count_dict)
    return most_common_values, max_count

common_values, max_count = find_most_common(list1)

