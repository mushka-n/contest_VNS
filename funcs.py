from um_funs import *


def Count_GE(plan, m_clusters, p_clusters):
    m, p = len(m_clusters), len(p_clusters)
    ones, cl_ones, cl_zeros = 0, 0, 0
    for machine in plan: ones += machine.count(1)
    for i in range(m):
        for j in range(p):
            if m_clusters[i] == p_clusters[j]:
                if plan[i][j]:
                    cl_ones += 1
                else:
                    cl_zeros += 1
    return cl_ones / (ones + cl_zeros)


def Divide_Clusters(m_clusters, p_clusters, indexes_x, indexes_y, x, y):
    clustersnum = max(m_clusters)

    new_clust_x = indexes_x[x + 1:]
    new_clust_y = indexes_y[y + 1:]
    new_m_divide = [err for err in m_clusters]
    new_p_divide = [err for err in p_clusters]

    for j in range(len(new_clust_y)):
        new_m_divide[new_clust_y[j]] = clustersnum + 1
    for j in range(len(new_clust_x)):
        new_p_divide[new_clust_x[j]] = clustersnum + 1

    return new_m_divide, new_p_divide


def Merge_Clusters(m_clusters, p_clusters, merge1, merge2):
    new_m, new_p = m_clusters, p_clusters
    indexes_2 = [Find_Indexes(p_clusters, merge2), Find_Indexes(m_clusters, merge2)]
    for p_ind in indexes_2[0]:
        new_p[p_ind] = merge1
    for m_ind in indexes_2[1]:
        new_p[m_ind] = merge1
    for i in range(len(new_m)):
        if new_m[i] > merge1:
            new_m[i] -= 1
    for i in range(len(new_p)):
        if new_p[i] > merge1:
            new_p[i] -= 1
    return new_m, new_p


def VNS(m_clusters, p_clusters, plan):
    best_GE = Count_GE(plan, m_clusters, p_clusters)
    repeat = 0

    while 1:
        old_GE = best_GE

        best_m = m_clusters
        for i in range(len(m_clusters) - 1):
            repeat_m = 0
            for j in range(i, len(m_clusters)):
                new_m = Swap_Arr([i for i in m_clusters], i, j)
                new_GE = Count_GE(plan, new_m, p_clusters)
                if new_GE >= best_GE:
                    if new_GE == best_GE:
                        repeat_m += 1
                        if repeat_m == 2:
                            break
                    best_GE, best_m = new_GE, new_m
        m_clusters = best_m

        best_p = p_clusters
        for i in range(len(p_clusters) - 1):
            repeat_p = 0
            for j in range(i, len(p_clusters)):
                new_p = Swap_Arr([i for i in p_clusters], i, j)
                new_GE = Count_GE(plan, m_clusters, new_p)
                if new_GE >= best_GE:
                    if new_GE == best_GE:
                        repeat_p += 1
                        if repeat_p == 2:
                            break
                    best_GE, best_p = new_GE, new_p
        p_clusters = best_p

        if repeat == 7:
            return m_clusters, p_clusters
        elif old_GE < best_GE:
            repeat = 0
        else:
            repeat += 1


def Count_to_Divide(cluster, m_clusters, p_clusters):
    strs, cols = p_clusters.count(cluster), m_clusters.count(cluster)
    indexes_x = Find_Indexes(p_clusters, cluster)
    indexes_y = Find_Indexes(m_clusters, cluster)
    parts_to_divide = []
    if strs > 1 and cols > 1:
        for x in range(strs - 1):
            new_part = [indexes_x[:x + 1]]
            for y in range(cols - 1):
                new_part += [indexes_y[:y + 1]]
                parts_to_divide.append(new_part)
    return parts_to_divide
