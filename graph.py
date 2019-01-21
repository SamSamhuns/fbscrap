# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

time_list = []
exist_set = set()

with open('active_friend_list.txt', 'r') as fdata:
    start = (fdata.readline()).strip().split(',')
    for line in fdata:
        nline = line.strip().split(',')
        if nline[0] not in exist_set:
            exist_set.add(nline[0])
        if start[1] != nline[1]:
            time_list.append([start[1], exist_set])
        start = nline
while True:
    print(time_list)
