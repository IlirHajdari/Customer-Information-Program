f = open("PastCustomers.txt", "wb")
print("PastCustomers", f.name)
print("Closed or not : ", f.closed)
print("Opening mode : ", f.mode)
f.close()

f = open("PastCustomers.txt", "a")
f.write("Past Customers\n--------------\n")
f.write("\n1.Customer number: 401 \nCustomer name: John Smith \nAddress: ThisWay, ln, somewhere on Earth \nDate of Job: January 1 2018 \nPrice of Job: $10,000\n")
f.write("\n2.Customer number: 501 \nCustomer name: Anakin Skywalker \nAddress: Jedi Temple, Coruscant \nDate of Job: May 4 2019 \nPrice of Job: $20,000\n")
f.write("\n3.Customer number: 601 \nCustomer name: Willy Nilly \nAddress: OverThere Cr. USA \nDate of Job: June 17 2020 \nPrice of job: $7,000\n")
f.write("\n4.Customer number: 701 \nCustomer name: Frodo Baggins \nAddress: The Shire, USA \nDate of Job: September 3 2020 \nPrice of job: $12,000\n")
f.close

#Open and read the file after append

f = open("PastCustomers.txt", "r")
print(f.read())


#Second text file

f = open("JobsNotYetPerformed.txt", "wb")
print("Jobs Not Yet Performed", f.name)
print("Closed or not : ", f.closed)
print("Opening mode : ", f.mode)

f = open("JobsNotYetPerformed.txt", "a")
f.write("Proposed Jobs\n-------------\n")
f.write("\n1.Customer number: 001 \nCustomer name: Tom the Cat \nAddress: AverageTown, USA \nProposed Job Date: Febuary 22 2022 \nProposed Job Price: $10,000 \n")
f.write("\n2.Customer number: 002 \nCustomer name: Mike Ike \nAddress: CandyCity, USA \nProposed Job Date: July 7 2022 \nProposed Job Price: $5,000 \n")
f.write("\n3.Customer number: 003 \nCustomer name: Manguy Manfred \nAddress: SomeTown, USA \nProposed Job Date: August 1 2023 \nProposed Job Price: $12,000 \n")
f.write("\n4. Customer number: 004 \nCustomer name: Thomas Train \nAddress: TrainYard, USA \nProposed Job Date: December 10 2024 \nProposed Job Price: $15,000")
f.close

#Open and read the file after append

f = open("JobsNotYetPerformed.txt", "r")
print(f.read())

#Merge files into one

filename = ["PastCustomers.txt", "JobsNotYetPerformed.txt"]

with open("CustomerData.txt", "w") as outfile:
    for names in filename:
        with open(names) as infile:
            outfile.write(infile.read())
        outfile.write("\n")