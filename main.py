balance = 1000
inventory = {"хлеб":10}
while True :
	print("Баланс",balance)
	print("Инвентарь",inventory)
	x = int(input("\nГЛАВНОЕ МЕНЮ\nЧто вы хотите сделать\n1.Посмотреть товары\n2.Дождаться покупателя\n3.Открыть сундук\n4.Выйти из игры\n"))
	if x == 4:
		break
	if x == 1:
		for i in inventory:
			print(f"\n{i}: {inventory[i]}")