"""This function allows for the user to copy a line from the measle
text based on the user's input. All lines are
selected if the user's response is any of the values in the set"""

def inputfile(): # funtion to always read measles file
    file1 = open("measles.txt", "r")
    for line in file1:
        print(line)
    file1.close

def outputfile(): #function to prompt user to for the name of an output file
    name = input("Enter the name of a file: ")
    if FileNotFoundError:
        f = open(name, "w") #creating a new file if file doesn't exist
        print("File does NOT exist so file has been created.")
    else: # discarding the contents of file if it does exist
        f.truncate(name)
        print("File exists, the contents of file have been removed.")
    

def yearinput(name): # function to prompt user to enter a year and select the corresponding lines in the text file
    year = input("Enter a year here: ")
    file1 = open("measles.txt", "r")
    for line in file1:
        for year in line:
            if year == "" or "all" or "ALL":
                with open('measles.txt', 'r') as file1, open(name,'a') as file2:
                    content = file1.readlines() #separating the file into lines
                    content = [x.strip() for x in content]
                    if content[3] == year:
                        file2.write(content)
                        print("Data has been copied to new file. ")
                    else:
                        return line
            

def main():
    inputfile()
    outputfile()
    name = input("Enter a name for a file here: ")
    yearinput(name)

main()












# country income percent vaccinated region year
 
