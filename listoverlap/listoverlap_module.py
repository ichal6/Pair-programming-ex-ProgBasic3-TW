def listoverlap(list1, list2):
    list3 = []
    for el1 in list1:
        for el2 in list2:
            if el1 == el2:
                list3.append(el1)
    
    list3 = set(list3)
    list3 = list(list3)
    
    return list3


def main():
    return


if __name__ == '__main__':
    main()
