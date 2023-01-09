def displayInventory(inventoryDict):
    print('Inventory:')
    sum = 0
    for k,v in inventoryDict.items():
        print(v,k)
        sum = sum + v
    print('Total number of items: ',sum)

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i] + 1

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv,dragonLoot)
displayInventory(inv)
