fruits = {}
cart = []
while True:
	print("enter 1 for Add Fruit")
	print("enter 2 for Delete Fruit")
	print("enter 3 for Search Fruit by Name and Rate")
	print("enter 4 for Change Fruit Data")
	print("enter 5 for Add to cart")
	print("enter 6 for Display all Fruits")
	print("enter 7 for display cart")
	print("enter 8 for exit")
	
	c = int(input("enter the choice : "))

	if c==1:
		fid = int(input("\tEnter the Fruit Id : "))
		name = input("\tEnter the name of Fruit : ")
		rate = int(input("\tEnter the rate of Fruit : "))
		imp_fr = input("\tEnter the place imported from : ")
		imp_date = input("\tEnter the imported date : ")
		buy_rs = int(input("\tEnter the buying Price : "))
		if fid not in fruits.keys():
			fruits[fid] = {"Name":name,"Rate":rate,"Imported From":imp_fr,"Imported Date":imp_date,"Buying Price":buy_rs}

		else:
			print("\tFruit Id id is already present")	

	elif c==2:
		fid = int(input("\tEnter the Fruit id : "))
		if (fid in fruits.keys()):
			del fruits[eid]
		else:
			print("Fruit id is incorrect")

	elif c==3:
		n = input("\tEnter the name to search : ")
		r = int(input("\tEnter the rate to search : "))
		f = False
		for i in fruits.values():
			if i["Name"] == n and i["Rate"] == r: 
				print(f"\t{i['Name']} is found")
				f = True
				break
		if f == False:
			print("\tNot Found")
			 
	elif c==4:
		eid  = int(input("\tEnter the Fruit Id : "))
		if eid in fruits.keys():

			print("\tpress 1 for change Name")
			print("\tpress 2 for change Rate")
			ch = int(input("Enter the choice : "))

			if ch==1:
				fruits[eid]["Name"] = input("\tEnter the new Name : ")
			if ch==2:
				fruits[eid]["Rate"] = int(input("\tEnter the new Rate : "))
		else:
			print("\tFruit Not Found")
	elif c==5:
		
		for i,j in fruits.items():
			print(f"\tPress {i} to add {j['Name']} to cart")
		s = int(input("\tEnter the choice : "))
		sid = int(input("\tEnter the Store Id : "))
		c = int(input("\tEnter the Count : "))
		cart.append({"Fruit_id" :s,"Fruit_Name":fruits[s]["Name"],"Store Id":sid,"Count":c})
				
		
	elif c==6:
		if fruits != None:
			print("\tFruit Id\tName\tRate\tImported From\tImported Date\tBuying Price")
			for i,j in fruits.items():
				print(f"\t{i}\t\t{j['Name']}\t{j['Rate']}\t{j['Imported From']}\t\t{j['Imported Date']}\t{j['Buying Price']}")
						
		else:
			print("There is no fruits")                
	elif c==8:
		break
	elif c==7:
		print("\tFruit Id\tFruit Name\tStore Id\tCount")
		for i in cart:
			print(f"\t{i['Fruit_id']}\t\t{i['Fruit_Name']}\t\t{i['Store Id']}\t\t{i['Count']}")
		
	else:
		print("invalid choice")

