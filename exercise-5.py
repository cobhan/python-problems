with open("data/iris.csv") as f:
    for line in f:
        line = line.replace(',', ' ')
        line = line.rstrip()
        print(line[:11], line[12:16].strip())
