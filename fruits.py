fruits = []
while True:

	print("Press 1 for Add Fruit")
	print("Press 2 for Delete Fruit by Name")
	print("Press 3 for Search Fruit by Name and Rate")
	print("Press 4 for Change Fruit Name, Rate")
	print("Press 5 for Display Fruits")
	print("Press 6 for exit")

	c = int(input("enter the choice : "))
	if c==1:
		name = input("Enter the name of Fruit : ")
		rate = int(input("Enter the rate of Fruit : "))
		if name != None and rate != None :
			fruits.append([name,rate])
			print("fruit added successfully")
		else:
			print("fruit insertion failed")
	if c==2:
		print(fruits)
		name = input("Enter the name of Fruit from above to delete : ")
		if name != None:
			for i in fruits:
				if i[0] == name:
					fruits.remove(i)
			print("deleted successfully")
		else:
			print("deletion failed")
	if c==3:
		name = input("Enter the name of Fruit to search : ")
		rate = int(input("Enter the rate of Fruit to search : "))
		for i in fruits:
			#f = [name,rate]
			if i[0] == name and i[1] == rate:
			#if i == f:
				print(name+" is present in the fruits")
	if c==4:
		name = input("Enter the name of Fruit : ")
		rate = int(input("Enter the rate of Fruit : "))
		if name != None and rate != None :
			for i in fruits:
				if i[0] == name and i[1] == rate :
					i[0] == input("enter the new fruit : ")
					i[1] == input("enetr the new rate : ")
	if c==5:
		for i in range(len(fruits)):
			
			print(str(i+1)+". "+fruits[i][0]+" - "+str(fruits[i][1]))	

	if c==6:
		break
 		
	else:
		print("Choice is invalid")
