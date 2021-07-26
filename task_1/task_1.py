import csv

entry = 0

def rbf_2004():
    global entry
    print("Reel Big Fish albums released after 2004 are:")
    with open("albums.csv", "r") as csv_file:
        albums = csv.DictReader(csv_file)

        for row in albums:
            year = int(row["year"])
            if year > 2004:
                print(row)
                entry += 1
            else:
                entry += 1

    print("                           ")
    csv_file.close()

def rbf_leapyear():
    global entry
    print("Reel Big Fish albums released on a leap year are:")
    with open("albums.csv", "r") as csv_file:
        albums = csv.DictReader(csv_file)

        for row in albums:
            year = int(row["year"])
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        print(row)
                        entry += 1
                    else:
                        entry += 1
                else:
                    print(row)
                    entry += 1
            else:
                entry += 1

    print("                           ")
    csv_file.close()

rbf_2004()
rbf_leapyear()