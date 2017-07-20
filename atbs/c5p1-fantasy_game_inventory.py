inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(invent):
	totalItems = 0
	print('Inventory:')
	for k,v in invent.items():
		print(v, k)
		totalItems += v
	print("The total number of items:", totalItems)

displayInventory(inventory)
