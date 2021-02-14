from termcolor import colored
from random import randint, shuffle, sample


def Read_Datafile():
    datafile = open('data.txt', 'r')
    filelines = datafile.readlines()
    m, p = map(int, filelines[0].split())

    plan = [[0] * p] * m
    data = [[]] * m

    for i in range(1, m + 1):
        data[i - 1] = list(map(int, filelines[i].split()))[1:]

    for i in range(m):
        machine = [0] * p
        for j in range(len(data[i])):
            machine[data[i][j] - 1] = 1
        plan[i] = machine

    clustersnum = randint(2, min(m, p))

    clusterslist = [i + 1 for i in range(clustersnum)]
    m_clusters = sample(clusterslist, clustersnum)
    for i in range(clustersnum, m):
        m_clusters.append(randint(1, clustersnum))
    shuffle(m_clusters)

    p_clusters = sample(clusterslist, clustersnum)
    for i in range(clustersnum, p):
        p_clusters.append(randint(1, clustersnum))
    shuffle(p_clusters)

    return plan, m_clusters, p_clusters


def List_to_Str(arr):
    string = ''
    for i in range(len(arr) - 1):
        string += str(arr[i]) + ' '
    string += str(arr[len(arr) - 1])
    return string


def Find_Indexes(arr, elem):
    out = []
    if elem in arr:
        out.append(arr.index(elem))
        for i in range(arr.count(elem) - 1):
            out.append(arr.index(elem, out[-1] + 1))
    return out


def Print_Plan(plan, m_clusters, p_clusters):
    print(' ' * (len(str(max(m_clusters))) + 1), colored(List_to_Str(p_clusters), 'yellow'))
    for i in range(len(m_clusters)):
        print(colored(m_clusters[i], 'yellow'), end='')
        if m_clusters[i] < 10:
            print(' ', end='')
        for j in range(len(plan[i])):
            if p_clusters[j] > 9:
                print(end=' ')
            if plan[i][j]:
                print(' +', end='')
            else:
                print('  ', end='')
        print()


def Swap_Arr(arr, i1, i2):
    new = arr
    new[i1], new[i2] = new[i2], new[i1]
    return new
