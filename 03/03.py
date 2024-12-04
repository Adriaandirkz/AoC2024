string= "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

#index += 1 + string[index:].index("mul(")
#present = "mul(" in string[index:]


def input():
    with open("input 03.txt") as f:
        string = f.read()
    return string

def MulFinder(string):
    present = True
    index = 0
    i=0
    result = 0
    while present:
        n = ["", ""]
        temp = True

        index += 1 + string[index:].index("mul(")
        present = "mul(" in string[index:]

        while temp:
            if string[index+3].isdigit():
                #Counts digits
                n[i] += string[index+3]
                index+=1

            elif string[index+3] == "," and i == 0:
                #Finds ,
                i =1
                index+=1

            elif i == 1 and string[index+3] == ")":
                #Finds closing )
                result += int(n[0]) * int(n[1])
                temp = False
                i = 0

            else:
                #Non found
                temp = False
                i = 0

        index +=1
    return result
string = input()
print(string)
print(MulFinder(string))