# import csv 
# companies = []
# sales = []


# with open('output.csv') as file:
#     readFile = csv.reader(file) 
#     file.readline() # reads and moves to next line
#     for i in readFile:
#         companies.append(str(i[0]))
#         # print(i[0])
#         sales.append([int(y.replace(",", "")) for y in i[1:]])
# print(companies)
# print(sales)

# jan = []
# feb = []
# mar = []
# apr = []
# may = []
# june = []
# july = []
# aug = []

# for i in sales:
#     # print(i[0])
#     jan.append(int(i[0]))
#     feb.append(int(i[1]))
#     mar.append(int(i[2]))
#     apr.append(int(i[3]))
#     may.append(int(i[4]))
#     june.append(int(i[5]))
#     july.append(int(i[6]))
#     aug.append(int(i[7]))
# print(f"January 2019 total sales: £{sum(jan)}")
# print(f"Febuary 2019 total sales: £{sum(feb)}")
# print(f"March 2019 total sales: £{sum(mar)}")
# print(f"April 2019 total sales: £{sum(apr)}")
# print(f"May 2019 total sales: £{sum(may)}")
# print(f"June 2019 total sales: £{sum(june)}")
# print(f"July 2019 total sales: £{sum(july)}")
# print(f"August 2019 total sales: £{sum(aug)}")

# ford = sum(sales[0])
# volks = sum(sales[1])
# merc = sum(sales[2])
# vaux = sum(sales[3])
# bmw = sum(sales[4])
# print(f"Ford Motor Company total yearly sales: £{ford}")
# print(f"Volkswagen UK total yearly sales: £{volks}")
# print(f"Mercedes-Benz UK total yearly sales: £{merc}")
# print(f"Vauxhall Motors total yearly sales: £{vaux}")
# print(f"BMW  total yearly sales: £{bmw}")



import csv

companies = []
sales = []

with open("output.csv") as csvfile: # dont need r or w as csv module handles this. 
    reader = csv.reader(csvfile) # reader function from the cvs module, which reads all the lines.
    next(reader) # skips the first line dont need the header data
    for row in reader:
        companies.append(row[0])
        sales.append([int(x.replace(",", "")) for x in row[1:]]) # iterates from index 1 to the end, changes from str to int and gets rid of ","

#print(sales)
monthly_sum = [sum(x) for x in zip(*sales)] # unpacks the list of lists into tuples, and sums.

#print(monthly_sum)

yearly_sum = {}
for i in range(len(companies)):
    yearly_sum[companies[i]] = sum(sales[i])

print("monthly sales:", monthly_sum)
print("yearly sales:")
for company, sales in yearly_sum.items():
    print(company, sales)
