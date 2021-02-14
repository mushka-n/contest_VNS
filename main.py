from funcs import *

plan, m_clusters, p_clusters = Read_Datafile()
m_clusters, p_clusters = VNS(m_clusters, p_clusters, plan)
best_GE = Count_GE(plan, m_clusters, p_clusters)
best_m, best_p = m_clusters, p_clusters

print('DIVIDE STARTED')
repeat = 0
while 1:
    clustersnum = max(m_clusters)
    best_GE = Count_GE(plan, m_clusters, p_clusters)
    old_GE = best_GE

    for cluster in range(1, clustersnum + 1):
        parts_to_divide = Count_to_Divide(cluster, m_clusters, p_clusters)
        for part in parts_to_divide:
            new_m, new_p = [i for i in m_clusters], [i for i in p_clusters]
            for p_index in part[0]:
                new_p[p_index] = clustersnum + 1
            for m_index in part[1]:
                new_m[m_index] = clustersnum + 1

            new_m, new_p = VNS(new_m, new_p, plan)
            new_GE = Count_GE(plan, new_m, new_p)
            if new_GE > best_GE:
                best_m, best_p, best_GE = new_m, new_p, new_GE
                print()
                print(len(m_clusters), 'X', len(p_clusters))
                print(*best_m)
                print(*best_p)
                print(best_GE)

    m_clusters, p_clusters = best_m, best_p




    if repeat == 7:
        break
    elif old_GE == best_GE:
        repeat += 1
    else:
        repeat = 0


print('MERGE STARTED')
repeat = 0
while 1:
    clustersnum = max(m_clusters)
    best_GE = Count_GE(plan, m_clusters, p_clusters)
    old_GE = best_GE

    if 2 in m_clusters:
        for i in range(1, clustersnum):
            for j in range(i, clustersnum + 1):
                new_m, new_p = Merge_Clusters([q for q in m_clusters], [q for q in p_clusters], i, j)
                new_m, new_p = VNS(new_m, new_p, plan)
                new_GE = Count_GE(plan, new_m, new_p)
                if new_GE > best_GE:
                    best_m, best_p, best_GE = new_m, new_p, new_GE
                    print()
                    print(len(m_clusters), 'X', len(p_clusters))
                    print(*best_m)
                    print(*best_p)
                    print(best_GE)
    m_clusters, p_clusters = best_m, best_p
    if repeat == 7:
        break
    elif old_GE == best_GE:
        repeat += 1
    else:
        repeat = 0


print()
print('FINISH')
print(len(m_clusters), 'X', len(p_clusters))
print(*m_clusters)
print(*p_clusters)
print(best_GE)
