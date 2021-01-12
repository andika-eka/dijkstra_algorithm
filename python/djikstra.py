
import sys
infinity = sys.maxsize # mensimulasikan nilai takhingga

file1 = open("./graph.csv")


def ambil_label(file):
    # mengambil header dari file csv sebagai label
    line = file.readline()
    label = line.split(",")
    label = label[1:]
    label[-1] = label[-1][0]
    return label
lable1 = ambil_label(file1)


def csvToArr(file):
    # mengubah matrix dalam file Csv menjadi array 2D
    arr = list()

    for x in file:
        row = x.split(",")
        row = list(map(int, row[1:]))
        arr.append(row)

    return arr


class Graf():
    def __int__(self, ):
        self.matrix = list() # matrix dari csv
        self.jumNode = int()

    def dijkstra(self, start): # start = node paling awal dihitung dari 0
        jarak = [infinity] * self.jumNode  # jarak dari node ka node awal (di asumsikan infinity)
        jarak[start] = 0
        treeSet = [False] * self.jumNode   # menandai node yang sudah dilalui (dilalui = True)
        prev = [0 ] *self.jumNode  # node sebelumnya

        for i in range(self.jumNode):
            jalur = self.jarakTerpendek(jarak, treeSet)
            treeSet[jalur] = True

            for x in range(self.jumNode):
                if (self.matrix[jalur][x] > 0) and not (treeSet[x]) and \
                        (jarak[x] > (jarak[jalur] + self.matrix[jalur][x])):

                    jarak[x] = jarak[jalur] + self.matrix[jalur][x]
                    prev[x] = jalur

        # print(prev)
        return list(zip(jarak, prev))

    def jarakTerpendek(self, jarak, treeSet): # mencari node neighbor dengan jarak terdekat
        min = infinity
        for x in range(self.jumNode):
            if (jarak[x] < min) and not (treeSet[x]):
                min = jarak[x]
                index = x
        return index

    def printdijkstra(self, jarak, label):
        print("node \t|jarak dari start \t|node sebelumnya")
        for node in range(self.jumNode):
            print(label[node], "\t  ", jarak[node][0], "\t\t\t  ", label[jarak[node][1]])
            # print(label[node], "\t ", jarak[node][0])


if __name__ == "__main__":
    file = open("./graph.csv")
    label = ambil_label(file)
    table = csvToArr(file)

    graf1 = Graf()
    graf1.matrix = table
    graf1.jumNode = len(table)

    arr = graf1.dijkstra(0)
    graf1.printdijkstra(arr, label)

# author : Andika Eka
#  https://github.com/andika-eka
