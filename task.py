import random  # import module to generate random numbers
import string  # import module to work with letters

# Step 1: create a list of random dicts
num_dicts = random.randint(2, 10)  # random number of dicts between 2 and 10
dict_list = []  # list to store all dicts

for i in range(num_dicts):  # loop over number of dicts
    num_keys = random.randint(1, 5)  # random number of keys in each dict (1 to 5)
    keys = random.sample(string.ascii_lowercase, num_keys)  # pick random letters for keys
    current_dict = {k: random.randint(0, 100) for k in keys}  # create dict with letter keys and random values
    dict_list.append(current_dict)  # add dict to list

print("Generated list of dicts:")
print(dict_list)  # print generated list of dicts for verification

# Step 2: create one common dict with rules
common_dict = {}  # initialize empty dict for final result

# flatten all keys with dict indices
key_sources = {}  # temporary dict to track which dict each key comes from and its value

for index, d in enumerate(dict_list, start=1):  # loop over dicts with 1-based index
    for k, v in d.items():  # iterate through each key-value pair
        if k not in key_sources:  # if key is new
            key_sources[k] = [(v, index)]  # store value and dict index as a tuple in list
        else:
            key_sources[k].append((v, index))  # append new value and dict index

# now process keys to pick max values and rename if necessary
for k, values in key_sources.items():
    if len(values) == 1:  # key is only in one dict
        common_dict[k] = values[0][0]  # take the value as is
    else:  # key is in multiple dicts
        max_val, max_idx = max(values, key=lambda x: x[0])  # find tuple with maximum value
        common_dict[f"{k}_{max_idx}"] = max_val  # rename key with dict number and store max value

print("Combined dict with max values and renamed keys:")
print(common_dict)  # print final combined dict