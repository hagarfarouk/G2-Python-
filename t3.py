
ava_list =["banana","apple"]
costs = [5 , 10]
id = [177 , 717]
stock= [100,177]
import random
#pwa = "1234"
#ownera = "AA"
#pwb = "1234"
#ownerb = "BB"

def owner():
	pwa = "1234"
	ownera = "AA"
	pwb = "1234"
	ownerb = "BB"
	owner = input("Enter Username ")
	if owner == ownera:
		pw=input("Enter your password")
		if pw == pwa:
			print("   ")
			print("Welcome To ITI Shop", owner)
			print("   ")
		else:
			for p in range (3):
				pw=input("Wrong password! Try Again ")
				if pw == pwa:
					break
	elif owner == ownerb:
		pw=input("Enter your password")
		if pw == pwb:
			print("   ")
			print("Welcome To ITI Shop", owner)
			print("   ")
		else:
			for p in range (3):
				pw=input("Wrong password! Try Again ")
				if pw == pwb:
					break		
	else : 
		print("  ")
		print(" You Have NO ACCESS")
		exit()
		
	if pw!=pwa or pw!=pwb:
		print("   ")
		print("Wrong Passord! You Can't Access Owner Mode Right Now")
		exit()
	print("To Change Username or Password press 0")	
	print("To Add New products press 1")
	print("To Show products press 2")
	print("To Add Cost press 3")
	print("To Add to Stock press 4")
	print("To Remove any product press 5")
	print("To Exit press 6 ")


	
	x= int(input())
	if x ==0:
		if owner == ownera:
			ownera = input("Enter New Username ")
			pwa = input("Enter New Password  ")
		if owner == ownerb:
			ownerb = input("Enter New Username ")
			pwb = input("Enter New Password  ")
				

	if x==1:                                                              #adding new products
		
		n = input("enter new product ")   
		ava_list.append(n)  
		ne = int(input("enter cost "))
		costs.append(ne)
		nw = int(input("enter their stock "))
		stock.append(nw)
		dd = random.randint(1,200)   #to generate uniqe id for new product in range 1 to 200 then add this number to id list
		id.append(int(dd))
		print("in Stock      id      cost        product")
		for i in range (len(ava_list)):
			print(stock[i],"        ",id[i],"      ",costs[i],"        ",ava_list[i])
	if x==2:                                                                                   #show all products 
		print("in Stock      id      cost        product")
		for i in range (len(ava_list)):
			print(stock[i],"        ",id[i],"      ",costs[i],"        ",ava_list[i])
		#print(ava_list[-1:-1:-1])
	if x==3:                                                                                  #change price of any product
		y   =input("enter the required product: ")
		z   = ava_list.index(y)     #take product index to access
		new = int(input("enter new price"))     #casting to int to be located in costs list 
		costs[z]= new  
		print("in Stock      id      cost        product")
		for i in range (len(ava_list)):
			print(stock[i],"        ",id[i],"      ",costs[i],"        ",ava_list[i])
	if x==4:                                                                                  #adding to stock                                                              
		y   =input("enter the required product: ")
		z   = ava_list.index(y)   
		nst = int(input("Add New Quantity "))
		stock[z]= stock[z]+nst            #adding new quantity to the already instock quantity 
		print("in Stock      id      cost        product")
		for i in range (len(ava_list)):
			print(stock[i],"        ",id[i],"      ",costs[i],"        ",ava_list[i])
	if x==5:                                                                                #remove Products
		rmv= int(input("Enter the ID of the Required Product "))
		g = id.index(rmv)
		id.remove(rmv)
		ava_list.pop(g)
		costs.pop(g)
		stock.pop(g)
		print("in Stock      id      cost        product")
		for i in range (len(ava_list)):
			print(stock[i],"        ",id[i],"      ",costs[i],"        ",ava_list[i])
	
			
	if x==6:                                                                         #exit
		exit()
			
		
def custmer():
	print("To Show Our Products please press 1 ")
	print("To Buy from Our Products please press 2 ")
	print("To Exit Please Press 3 ")
	x = int(input())
	if x==1:
		print("id    cost         product")
		for i in range (len(ava_list)):
			print(id[i],"    ",costs[i],"        ",ava_list[i])
		
		
	if x==2:
		sum=0
		#print("Enter id of required products ")
		y = list(input("Enter id of required products ").split(" "))
		Q = list(input("Enter The  Quantity of required products ").split(" "))
		print("id    cost         product         Quantity")	
		for z in range (len(y)):
			item= int( y[z] )
			ht = id.index(item)
			c = int ( ht )
			qq= int (Q[z])
			if (qq>stock[c]):
				print("Sorry! Out of Stock")
				print("Availabe only ", stock[c])
				continue
			stock[c]=stock[c]-qq	
			sum=sum+costs[c]*qq
			print(id[c],"    ",costs[c],"        ",ava_list[c],"       ",qq)
		print("sum=  ",sum)
		#print("id    cost    product")	
		#for h in range (len(ava_list)):	
			#print(ava_list.index(),"    ",costs[h],"        ",ava_list[h])
		#print("sum=  ",sum)
			
	if x==3:
		exit()
			#for z in range (len(y)):
				#item= y[z]
				#print("id    cost    product")
				#print(item,"    ",costs[item],"        ",ava_list[item])
				#print("sum=  ",sum)
			
			
		
	
print("Welcome To ITI Shop")
x = input("select Mode " )
if x=="owner": 
	owner()
if x=="custmer":
	custmer()
	
	
	