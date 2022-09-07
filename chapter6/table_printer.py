def printTable(lists):
    jutified_lists = []

    for list in lists:
        list_max_length = len(max(list, key=len))
        jutified_lists.append([item.rjust(list_max_length) for item in list])

    for y in range(len(lists[0])):
        for x in range(len(lists)):
            print(jutified_lists[x][y], end=('\n' if x == len(lists) -1 else ' '))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
        

printTable(tableData)