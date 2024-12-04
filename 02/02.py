def input():
    data = []
    with open("input 02.txt") as f:


        f.seek(0)
        lines = f.read().split("\n")
        for i in range(len(lines)):
            data.append([int(x) for x in lines[i].split(" ")])

    return data

data1 = [[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]


#data1=[[1, 2, 7, 8, 9]]
def SafeReport(report):
    error_margin = True
    errors = 0
    n = report[0]
    i = 0
    direction = (report[-1] - report[0])/(abs(report[-1] - report[0])+0.000001)
    while errors < 2 and i < len(report)-2 and error_margin:

        safe = 0 < (report[i+1] - report[i]) * direction <= 3

        if not safe and     :
            errors +=1

            error_margin = 0 < (report[i + 2] - report[i]) * direction <= 3

            print("not safe")
            i += 1



        i += 1
    print(errors, error_margin)
    return errors < 1 and error_margin




def CountSafeReports(data):
    count = 0
    for i in range(len(data)):
        count += (SafeReport(data[i]))
    print(count)

data = input()
print(data1)
CountSafeReports(data)
