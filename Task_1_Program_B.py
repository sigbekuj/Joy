"""This program will display a summary report to the user selected 
based on the user's input """
def inputfile():
    # prompting the user to input a file 
    name = input("Enter a file name here: ")
    try:
        with open(name) as infile:
            print("File exists")
    except FileNotFoundError:
        print("File does NOT exist")
        return programB()


def data(x):
    year = input("Enter a year here: ")
    print("Income levels: 1 = low income, 2 = lower middle income, 3 = upper middle income and 4 = high income")
    income = int(input( "Enter an income level here: "))
    str1 = ""
    if income == 1:
        str1 = "WB_LI";
    if income == 2:
        str1 = "WB_LMI";
    if income == 3:
        str1 = "WB_UMI";
    if income == 4:
        str1 = "WB_HI";
    if income < 1 or income > 4:
        str1 = "WB_LMI";
    a = [] 
    high = 0;
    low = 100;
    total = 0;
    for lines in a:
        lines.split()
        if line:
            print(str(line[1]));
            if line[4].startswith(year) and line[1] == str1:
                a.append(lines)
                total = total + int(line[2])
                if high < int(line[2]):
                    high = int(line[2])
                if low > int(line[2]):
                    low = int(line[2])
    lower_ = []
    higher_ = []
    for lines in a:
        line = lines.split()
        if line:
            if int(line[2]) == high:
                high_.append(line[0])
            if int(line[2]) == low:
                lower_.append(line[0])
    if a:
        print("Count of records =" + str(len(a)))
        print("Average percentage =", float(total)/float(len(a)))
        print("Country with the lowest percentage ="+ str(lower_))
        print("Country with the highest percentage ="+ str(higher_))
    else:
        print("There is NO data records")


def programB(): 
    x = inputfile()
    data(x)


programB()

