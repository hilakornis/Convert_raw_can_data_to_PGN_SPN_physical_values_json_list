from collections import defaultdict

def get_array(lines_from_file):
    array_id = []
    for line in lines_from_file:
        array_id.append(line.strip())
    return array_id


def fill_dict(array, dict):
    for num in array:

        if(dict.__contains__(num)):
            dict[num] = dict[num] + 1
        else:
            dict[num] = 1



file_input_canID1_hex = open('canbus_canID1_hex_res_compare_me.txt', 'r')
file_input_canID2_hex = open('canbus_canID2.txt', 'r')

lines1 = file_input_canID1_hex.readlines()
lines2 = file_input_canID2_hex.readlines()

array1 = get_array(lines1)
array2 = get_array(lines2)

array1.sort()
array2.sort()

set1 = set(array1)
set2 = set(array2)

set3 = set1.intersection(set2)
# found that there are duplicates in set1 that are found in set2.
print(set3)


print("done?")

file_input_canID2_hex.close()
file_input_canID1_hex.close()