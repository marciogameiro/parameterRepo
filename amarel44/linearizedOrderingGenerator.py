import sys
from helpers import run5

# logic is 4_2_2
# pattern is [4,2,2]

if __name__ == "__main__":
    #pattern = list(map(lambda x:int(x),logic.split('_')))
    #restrictedOrdering = list(map(lambda x: int(x),sys.argv[2:]))
    logic=sys.argv[1]
    file_no = int(sys.argv[2])
    extraFile = sys.argv[3]
    #print(subpattern)
    pres = []
    #with open('4_2_2_r.txt','r') as file:
    #    line = file.readline()
    #    while line:
    #        line = line[1:-2].split(',')
    #        line = list(map(lambda x: int(x), line))
    #        pres.append(tuple(line))
    #        line = file.readline()
    #print(pres[file_no]) 
    run5(logic,pres,extraFile)
    
    
