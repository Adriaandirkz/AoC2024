def input():
    L1, L2 = [], []
    with open("input 01.txt") as f:
        f.seek(0)
        lines = f.read().split("\n")
        for i in range(len(lines)):
            L1.append(int(lines[i].split("  ")[0]))
            L2.append(int(lines[i].split("  ")[1]))
    return L1, L2


def MinimalListDifferance(L1,L2):
    L1.sort()
    L2.sort()
    diff = 0
    for i in range(len(L1)):
        diff +=  abs(L1[i] - L2[i])
    return diff

def NumberTimesOccurances(L1, L2):
    result = 0
    for i in range(len(L1)):
        result += NumberOccurancesInList(L1[i],L2) * L1[i]
    return result

def NumberOccurancesInList(N1,L2):
    index, count = 0, 0
    m = N1 in L2
    while m:
        index = index + L2[index:].index(N1) +1
        count += 1
        m = N1 in L2[index:]
    return count

L1 ,L2 = input()
print(L1)
print(NumberTimesOccurances(L1,L2))



