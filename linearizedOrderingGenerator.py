import sys
from helpers import run5

# logic is 4_4_2
# pattern is [4,4,2]

if __name__ == "__main__":
    logic = sys.argv[1]
    #pattern = list(map(lambda x:int(x),logic.split('_')))
    #restrictedOrdering = list(map(lambda x: int(x),sys.argv[2:]))
    #file_no = int(sys.argv[2])
    #print(subpattern)
    pres = []
    with open('8_2_r.txt','r') as file:
        line = file.readline()[:-1]
        while line:
            line = line.split(' ')
            line = list(map(lambda x: int(x), line))
            pres.append(tuple(line))
            line = file.readline()[:-1]

    #run5(logic,pres[file_no])
    #print(pres[file_no])
    for i in range(len(pres)):
        run5("8_4",pres[i])
