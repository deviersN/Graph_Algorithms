def dataParser(filename):
    import csv
    rest = []
    for i in range(10):
        rest.append([])
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            elif row[10] == 'Summer' and int(row[9]) >= 1980:
                index = int((int(row[9]) - 1980) / 4)
                rest[index].append(row[9] + " " + row[1])
            line_count += 1
        printer2d(rest)
        print(f'Processed {line_count} lines.')
    return rest

def printer2d(array):
    for string in array:
        print(len(string))

def graphViewer(data):
    import pandas as pd
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    years = [1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
    values = [len(data[0]), len(data[1]), len(data[2]), len(data[3]), len(data[4]), len(data[5]), len(data[6]), len(data[7]), len(data[8]), len(data[9])]
    ax.scatter(years, values)
    ax.set_title('Olympic games contesters from 1980 to now.')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Olympians')
    plt.show()

if __name__ == "__main__":
    filename = '../dataset/athlete_events.csv'
    data = dataParser(filename)
    graphViewer(data)