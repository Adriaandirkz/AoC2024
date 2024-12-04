string= "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

#index += 1 + string[index:].index("mul(")
#present = "mul(" in string[index:]


def input():
    with open("input 03.txt") as f:
        string = f.read()
    return string

def Reader(string):
    present = True
    index = 0
    result = 0
    func = True
    while present:

        index_1 = index
        index += 1 + string[index:].index("mul(")
        #Check index of do and dont in text before found mul(
        do = FindReverseIndex(string[index_1:index],"do()")
        dont = FindReverseIndex(string[index_1:index],"don't()")

        #update func if there is a change in
        if do < dont:
            func = True
        if do > dont:
            func = False



        present = "mul(" in string[index:]
        if func:
            result += MulDecriptor(string,index)
        index +=1
    return result

def FindReverseIndex(seg,code):
    index = code in seg
    if index:
        index = seg[::-1].index(code[::-1])
        return index
    return 999999999

def MulDecriptor(string, index):
    result = 0
    i = 0
    n = ["",""]
    temp = True
    while temp:
        if string[index + 3].isdigit():
            # Counts digits
            n[i] += string[index + 3]
            index += 1
        elif string[index + 3] == "," and i == 0:
            # Finds ,
            i = 1
            index += 1
        elif i == 1 and string[index + 3] == ")":
            # Finds closing )
            result = int(n[0]) * int(n[1])
            print(result)
            temp = False
        else:
            # Non found
            temp = False
    return result


string = input()
string1= "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print(string)

print(Reader(string))



