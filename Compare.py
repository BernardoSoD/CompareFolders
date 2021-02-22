import sys


def divideSubString(string):
    for index in range(2, len(string)):
        if string[-index] == ' ' and string[-index + 1].isdigit():
            return [
                string[:-index],
                string[-index:]
                    ]



if __name__ == "__main__" and len(sys.argv) > 2:
    with open(sys.argv[1],'r') as arq1:
        list1 = []
        for item in arq1.readlines():
            list1.append(divideSubString(item))
    with open(sys.argv[2],'r') as arq2:
        list2 = []
        for item in arq2.readlines():
            list2.append(divideSubString(item))

    # the function that it's going to compare both files
    # its kinda inefficient but its the first that comes in mind
    with open('compared.txt','w') as saida:
        for item in list1:
            for comparador in list2:
                if item[0] == comparador[0] and item[1] == comparador[1]:
                    list2.remove(comparador)
                    break
        for sobra in list2:
            saida.write(sobra[0] + "\n")
else:
    print("Missing one or two path arguments")
