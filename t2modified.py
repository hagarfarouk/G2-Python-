import time
import os
x=0
while x<7:
	

	
	
	for i in range (10):
		print(" ",end=" ")
		for j in range (10):
			l=10-i
			if (l<=j):
				print("*", end=" ")
			else:	
				print(" ",end=" ")
		print("  ")
		
	print("  **********************************")
	
	for i in range (10):
		print(" ",end=" ")
		for j in range (10):
			if i>j :
				print(" ", end=" ")
			else :
				print("*", end=" ")
		print(" ")

	time.sleep(0.2)
	os.system("cls")
	r=10
	rows = int(r)

	k = 0

	for i in range(1, rows+1):
		print("      ",end=" ")
		for space in range(1, (rows-i)+1):
			print(end="  ")
   
		while k!=(2*i-1):
			print("* ", end="")
			k += 1
   
		k = 0
		print()
	for i in range (10):
		print("                        *")
	time.sleep(0.2)	
	os.system("cls")
	for i in range (10):
		print("                   ",end=" ")
		for j in range (i+1):
			print("*", end=" ")
		if i!= 10:	
			print(" ")			
		
	print("****************************************")
		
	for i in range (10):
		print("                   ",end=" ")
		for j in range (10-i):
			print("*", end=" ")
		
		print(" ")			
	
	time.sleep(0.2)
	os.system("cls")
	for i in range (10):
		print("              *")
	r = 10
	rows = int(r)
	for i in range(rows, 1, -1):
		for space in range(0, rows-i):
			print("  ", end="")
		for j in range(i, 2*i-1):
			print("* ", end="")
		for j in range(1, i-1):
			print("* ", end="")
		print()
	x=x+1
	time.sleep(0.1)
	os.system("cls")