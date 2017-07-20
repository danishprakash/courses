def displayInventory(invent):
	totalItems = 0
	print('Inventory:')
	for k,v in invent.items():
		print(v, k)
		totalItems += v
	print("The total number of items:", totalItems)


def addToInventory(inventory, addedItems):
    # your code goes here
	for item in addedItems:
		if item in inventory.keys():
			inventory[item] += 1
		else:
			inventory[item] = 1
	return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
