tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]
max_ = [0] * len(tableData)

for i in range(0,3):
	max_[i] = len(max(tableData[i])) + 1

print(max_)

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(max_[j]), end='')
    print()
