class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.fval = fval
        self.level = level

    def generate_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []

        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                childnode = Node(child, self.level+1, 0)
                children.append(childnode)

        return children

    def shuffle(self, pus, x1, y1, x2, y2):
        temp_puz = self.copy(pus)
        if 0 <= x2 < len(pus) and 0 <= y2 < len(pus):
            temp = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp
            return temp_puz
        else:
            return None

    def copy(self, puz):
        temp = []
        for i in puz:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        for i in range(len(puz)):
            for j in range(len(puz)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self):
        self.n = 3
        self.open = []
        self.closed = []

    def accept(self):
        temp = []
        for _ in range(self.n):
            t = []
            for _ in range(self.n):
                tempv = input("Enter value = ")
                t.append(tempv)
            temp.append(t)
        return temp

    def printt(self, data):
        for i in data:
            print(i)

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        print("Enter start state !!")
        start_state = self.accept()
        print("Start state=")
        self.printt(start_state)
        print("Enter Goal State = ")
        goal = self.accept()
        print("Print Goal State ")
        self.printt(goal)

        start = Node(start_state, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        start_changes = 0
        while True:
            if start_changes > 100:
                print("Sorry Not Able to find solution")
                break
            cur = self.open[0]
            print("   |   ")
            print("\n\\\\/////\n")
            self.printt(cur.data)

            h_v = self.h(cur.data, goal)
            print("\n\n\n\nHeuristic Value = ", h_v)
            print("\n\n Changes state = ", start_changes)
            if h_v == 0:
                break

            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            self.closed.append(cur)
            del self.open[0]
            start_changes += 1
            self.open = sorted(self.open, key=lambda x: x.fval)


puz = Puzzle()
puz.process()


'''
OUTPUT

Enter start state !!
Enter value = 1
Enter value = 2
Enter value = 3
Enter value = 8
Enter value = 6
Enter value = _
Enter value = 7
Enter value = 5
Enter value = 4
Start state=
['1', '2', '3']
['8', '6', '_']
['7', '5', '4']
Enter Goal State = 
Enter value = 1
Enter value = 2
Enter value = 3
Enter value = 8
Enter value = _
Enter value = 4
Enter value = 7
Enter value = 6
Enter value = 5
Print Goal State 
['1', '2', '3']
['8', '_', '4']
['7', '6', '5']
   |   

\\/////

['1', '2', '3']
['8', '6', '_']
['7', '5', '4']




Heuristic Value =  3


 Changes state =  0
   |   

\\/////

['1', '2', '3']
['8', '6', '4']
['7', '5', '_']




Heuristic Value =  2


 Changes state =  1
   |   

\\/////

['1', '2', '3']
['8', '6', '4']
['7', '_', '5']




Heuristic Value =  1


 Changes state =  2
   |   

\\/////

['1', '2', '3']
['8', '_', '4']
['7', '6', '5']




Heuristic Value =  0


 Changes state =  3

'''
