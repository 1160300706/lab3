# -*- coding: utf-8 -*-
def calculates(numberSequence, network, name):
    length = len(name)
    sums = 1
    for i in range(0, length):
        value = numberSequence[i]
        temp = name[i]
        listTemp = network[temp]
        if cmp((None,), listTemp[0]) == 0:
            if value == '0':
                sums *= float(listTemp[1][1])
            else:
                sums *= float(listTemp[1][0])
        else:
            numberOfFather = len(listTemp[0])
            chooseposition = 0
            for j in range(0, numberOfFather):
                temp = listTemp[0][j]
                value2 = numberSequence[name.index(temp)]
                if value2 == '0':
                    continue
                else:
                    chooseposition += pow(2, numberOfFather - j - 1)
            if value == '0':
                sums *= float(listTemp[chooseposition + 1][1])
            else:
                sums *= float(listTemp[chooseposition + 1][0])
    return str(sums)


# 处理数据文件
with open('burglarnetwork.txt', 'r') as f:
    list1 = f.readlines()
for i in range(0, len(list1)):
    list1[i] = list1[i].rstrip('\n')
while '' in list1:
    list1.remove('')
N = int(list1[0])
list2 = list1[1].split(" ")
listName = list1[1].split(' ')
Network = {}
for i in range(0, N):
    Network[list2[i]] = []
    # print Network
# 保存01表
Maps = [[0 for i in range(N)] for j in range(0, N)]
# print Maps
j = 0
list2 = []
for i in range(2, N + 2):
    list2 = list1[i].split(' ')
    # print list3
    for k in range(0, N):
        Maps[j][k] = int(list2[k])
    #  print list3
    j += 1
# print Maps
j = 0
list3 = [None] * N
sums = 0
sumOfRows = N + 2
list2 = []
# 遍历每一个节点的概率数据
for i in range(0, N):
    # 遍历每一列
    for k in range(0, N):
        list3[k] = Maps[k][j]
        sums += list3[k]
    j += 1
    if sums == 0:
        list4 = []
        list4.append((None,))
        list2 = list1[sumOfRows].split(' ')
        list4.append(tuple(list2))
        sumOfRows += 1
        Network[listName[i]] = list4
    else:
        list4 = []
        listTemp = []
        for col in range(0, N):
            if Maps[col][i] == 1:
                listTemp.append(listName[col])
        list4.append(tuple(listTemp))
        for k in range(sumOfRows, sumOfRows + pow(2, sums)):
            list2 = list1[k].split(' ')
            list4.append(tuple(list2))
            sumOfRows += 1
        Network[listName[i]] = list4
    sums = 0
# 处理问题文件
with open('burglarqueries.txt', 'r') as f:
    list1 = f.readlines()
for i in range(0, len(list1)):
    list1[i] = list1[i].rstrip('\n')
while '' in list1:
    list1.remove('')
problemlist = []
for i in range(0, len(list1)):
    temp = list1[i]
    list1[i] = temp[2:-1]
    temp = list1[i].split('|')
    nametuple = tuple([temp[0]])
    temp2 = temp[1].split(',')
    problemlist2 = []
    problemlist2.append(nametuple)
    for j in range(0, len(temp2)):
        temp = temp2[j].split('=')
        problemlist2.append(tuple(temp))
    problemlist.append(problemlist2)
Maps = [[0 for i in range(2)] for j in range(0, pow(2, N))]
for i in range(0, pow(2, N)):
    Maps[i][0] = bin(i).replace('0b', '').zfill(N)
    temp = Maps[i][0]
    Maps[i][1] = calculates(temp.zfill(N), Network, listName)
# print problemlist
print Maps
check = [0 for i in range(0, N)]
# print check
# print listName
# print Maps
for i in range(0, len(problemlist)):
    list1 = problemlist[i]
    listTemp = ''.join(list(list1[0][0])[0:-1])
    position = listName.index(listTemp)
    # print position
    #  print listTemp
    check[position] = 1
    for j in range(1, len(list1)):
        list2 = list1[j]
        listTemp = ''.join(list(list2[0][1:]))
        position = listName.index(listTemp)
        #  print listTemp
        # print position
        if cmp(list2[1], 'true') == 0:
            check[position] = 1
    check = [str(x) for x in check]
    # print check
    s = ''.join(check)
    number = int(s)
    # print number
    check = [0 for i in range(0, N)]
    results = 0
    flag = 0
    # print s
    for k in range(0, pow(2, N)):
        for j in range(0, N):
            if cmp(s[j], '1') == 0 and cmp(s[j], Maps[k][0][j]) != 0:
                flag = 1
        if flag == 0:
            results += float(Maps[k][1])
        flag = 0
    # print float(results)
