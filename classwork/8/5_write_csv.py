import csv

with open("result.csv", mode="w") as f:
    writer = csv.writer(f)
    print(writer)
    writer.writerow((123,546,2132134,64547))
    writer.writerow(("asdas","cxxc", "vcfgh"))
    writer.writerow(("eewww","wwwe","www","wwww"))
