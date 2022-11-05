import time

x=0
while x<1:
	for i in range (10):                      #print first triangle 
		print(" ",end=" ")
		for j in range (10-i):
			print(".", end=" ")
		
		print(" ")	
	time.sleep(1)
	
	for i in range (10):					#print first and last triangle
		print("",end=" ")
		for b in range (10-i):
			print(".", end=" ")
		#print(" ")	
		print("",end=" ")
		for j in range (9):
			l=9-i
			if (l<=j):
				print(".", end="  ")
			else:	
				print(end=" ")
		print("")
	time.sleep(1)
	
	print(" ")          #to make empety line between up and down 
	for i in range (11):        #first triangle in the bottom
		print("       ",end=" ")
		for j in range (11):
			if i>j :
				print(" ", end=" ")
			else :
				print(".", end=" ")
		print("")
	time.sleep(1)
	
	
	for i in range (10):       #the first 2 triangle again to appear in less time 
		print("",end=" ")
		for b in range (10-i):
			print(".", end=" ")
		#print(" ")	
		print("",end=" ")
		for j in range (9):
			l=9-i
			if (l<=j):
				print(".", end="  ")
			else:	
				print(end=" ")
		print("")
	time.sleep(0.005)
	
	
	print(" ")
	
	
	
	

	for i in range (10):    #the last 2 triangleS
		
		for a in range (i+1):
			print(".", end=" ")
#if i!= 10:	
	#print(" ")	
#time.sleep(0.5)
		print(end="")
	#rint("",end=" ")
		for j in range (10):
			if i<j :
				print(".", end="  ")
			else :
				print(" ",end="")
		print(" ")
	
			
		#print("")
		
	x=x+1
	