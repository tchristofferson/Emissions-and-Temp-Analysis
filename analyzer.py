import csv

emissions = {}
temp_changes = {}

with open("emissions.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row[1] == "Year":
            continue
        emissions[int(row[1])] = int(row[2])

with open("temperatureChanges.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row[1] == "Year":
            continue
        year = int(row[1])
        temp_changes[year] = 0
        for i in range(2, 14):
            temp_changes[year] += float(row[i])
        temp_changes[year] /= 12

with open("emissiontemps.csv", "x") as csv_file:
    csv_file.write("Year, emissions, tempChange\n")
    for year in emissions:
        csv_file.write(f"{year},{emissions[year]},{temp_changes[year]}\n")
