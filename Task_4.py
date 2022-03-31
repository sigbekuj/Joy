""" A sorting algorithm that takes in the user input and puts elements in a certain order"""



def outputfile(name): #function to prompt user to for the name of an output file
    if FileNotFoundError:
        f = open(name, "w") #opening file in read mode and creating a new file if file doesn't exist
        print("File does NOT exist so file has been created.")
    else: # discarding the contents of file if it does exist
        f.truncate(name)
        print("File exists, the contents of file have been removed.")


def random_generator(name):
	import random
	from timeit import default_timer as timer
	start = timer()
	f = open("data.txt", 'w')
	for i in range(1000): #range set to 1000
		num = str(random.randint(0,1000)) #random number in range 1000
		f.write(num)
		f.write("\n")
		f.close
		end = timer()
		print("Time taken for random generator:",end-start)

def sorting(): #function to sort a list in alphabetical order
	from timeit import default_timer as timer
	start = timer()
	list1 = [ ]
	i = 0
	for i in range(len(list1)):
		small = i
	for j in range (i+1, len(list)):
		if list1[small]>list1[j]:
			small = j
			temporary = list1[i]
			list1[i] = temporary
		end = timer() #storing the time it ends
		print("Time taken for selection sort :",end-start) #printing elasped time


name = input("Enter the name of a file: ") 
outputfile(name)
random_generator(name)
sorting()
percentage = random_generator()/sorting(list1)
print("The percentage difference of times is:", float(percentage))


