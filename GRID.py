import pygame
from tkinter import *
from tkinter import ttk
bfsPeeker=False
dfsPeeker=False
aPeeker=False

def bfsFunction():
    global dfsPeeker
    global bfsPeeker
    global aPeeker
    bfsPeeker=True
    dfsPeeker=False
    aPeeker=False
def dfsFunction():
    global dfsPeeker
    global bfsPeeker
    global aPeeker
    dfsPeeker=True
    bfsPeeker=False
    aPeeker=False
def aFunction():
    global dfsPeeker
    global bfsPeeker
    global aPeeker
    aPeeker=True
    bfsPeeker=False
    dfsPeeker=False
def tkinterWindowCreation():
    root=Tk()
    root.geometry("350x250")
    root.configure(bg='white')
    root.title("BFS DFS A*")
    root.resizable(False,False)
    global bfsPeeker
    bfsPeeker=False
    global dfsPeeker
    dfsPeeker=False
    global aPeeker
    aPeeker=False
    bfsButton=Button(root, bg='#00e6b8',fg="black", text="BFS",font=('Verdana', 15, 'bold'),command=bfsFunction)
    bfsButton.pack(pady=8)
    dfsButton=Button(root, bg='#00e6b8',fg="black", text="DFS",font=('Verdana', 15, 'bold'),command=dfsFunction)
    dfsButton.pack(pady=8)
    aButton=Button(root, bg='#00e6b8',fg="black", text="A*",font=('Verdana', 15, 'bold'),command=aFunction)
    aButton.pack(pady=8)
    runButton=Button(root, bg='#ff1a1a',fg="black", text="RUN",font=('Verdana', 25, 'bold'),command=root.destroy)
    runButton.pack(pady=8)
    root.mainloop()



# creating a window of Width=800 title=Visualization Window
width=600
window=pygame.display.set_mode((width,width))
pygame.display.set_caption("Visualization Window")

# Initialize COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# create dataType or class which has row,col,color,x,y,neighbours list, width, totalRow etc variable.
# getPos(), draw(), neighbours() and __lt__() function, where getPos() gives position of object's row and column.
#draw() function draw rectangle according to color, x,y, width which basically represent a cell.
#neighbours() decide which cells are neighbors and then store them.
# __lt__() function just return false when comapring two objects.

class Cell:
    def __init__(self, row, col, width, totalRows):
        self.row=row
        self.col=col
        self.width=width
        self.totalRows=totalRows
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.neighbors=[]
        self.visited=False

        

    def getPos(self):
        return self.col, self.row
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
    
    """ (0,0)


                row-1
        col-1   cell    col+1
                row+1


    (y,x)
    """
    # the condition of being barrier is- color of barrier is always BLACK.
       
    def neighborsOf(self, grid):
        self.nbrs=[]    

        #   upper nbr - row-1
        # if cell has row not 0 then it does not have upper cell
        # if upper cell is not barrier then append the upper cell as neighbour.
        if self.row>0 and not grid[self.row-1][self.col].color == BLACK:
            self.nbrs.append(grid[self.row-1][self.col])

        #   bottom nbr - row+1
        # if cell is not the last row then it has buttom row
        # if bottom cell is not barrier then append the bottom cell as neighbour.
        if self.row< self.totalRows-1 and not grid[self.row+1][self.col].color==BLACK:
            self.nbrs.append(grid[self.row+1][self.col])
        #   left nbr - col-1
        # if cell is not the first col then it has left cell
        # if left cell is not barrier then apend the left cell as neighbour.
        if self.col>0 and not grid[self.row][self.col-1].color==BLACK:
            self.nbrs.append(grid[self.row][self.col-1])
        #   right nbr - col+1
        # if cell is not the last col then it has right cell
        # if right cell is not barrier then apend the right cell as neighbour.
        if self.col < self.totalRows-1 and not grid[self.row][self.col+1].color==BLACK:
            self.nbrs.append(grid[self.row][self.col+1])

    def __lt__(self, other):
        return False

"""
rows=8:-
each cell contains Cell object, each Cell object contains  row,col,color,x,y,neighbours list, width, totalRow etc variables and getPos(), draw(), neighbours() and __lt__() functions.


            0          1          2          3          4         5          6           7
    0-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    1-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    2-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    3-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    4-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    5-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    6-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    7-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]

""" 
def twoDmatrix(rows, width):
    grid=[]
    gap=width//rows # integer division
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cellOBJ= Cell(i,j,gap,rows)
            grid[i].append(cellOBJ)
    return grid


def drawGrid(window,grid, rows, width):
    window.fill(WHITE)
    for eachrow in grid:
        for eachcolumn in eachrow:
            eachcolumn.draw(window)# Draw Rectengale

    # Draw lines- Rows and Cols wise on top of - rectengales or cells
    gap=width//rows
    for i in range(rows):
        pygame.draw.line(window, BLACK,(0, i*gap),(width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, BLACK,(j*gap,0),(j*gap, width))
    pygame.display.update()

def cellIndicator(pos, rows, width):
    # Indicate which cell is clicked by Mouse
    # pos contains the x,y coordinate of window.
    gap=width//rows
    y,x=pos
    row=y//gap
    col=x//gap
    return row, col
#---------------------------------------------------------------------------------------------------
    #BFS Algorithm
def algorithmB(drawGrid,grid, start, end):
    ar=[]
    cameFrom={} #keep track of parent
    ar.append(start) #Start cell is added on the Queue
    while len(ar)!=0: #until Queue is empty loop runs
        curentCell=ar.pop(0) # get the first item from Queue
        if not curentCell.visited: # if the item is not visted then
            curentCell.visited=True # mark the item as visited
            if curentCell != end: # if item is not the goal then
                curentCell.color=YELLOW # chage color of the item to yellow
            if curentCell==end: # if item is goal node then
                drawShortesPath(cameFrom, end, drawGrid) # calling path draw function to backtrack cells from goal to start
                end.color=TURQUOISE # change color of start and end cell 
                start.color=ORANGE
                return True
            for ns in curentCell.nbrs: # here in for loop we traverse all unvisited neighbours
                if(ns.visited==False):
                    cameFrom[ns]=curentCell # here we assign parent of neighbours
                    ar.append(ns) # added neighbours to the Queue
        drawGrid()
#----------------------------------------------------------------------------------------------------
    #DFS Algorithm
def algorithmD(drawGrid,grid, start, end):
    ar=[]
    cameFrom={}
    ar.append(start)#Start cell is added on the Stack
    while len(ar)!=0:
        curentCell=ar.pop()# get the last item from Stack
        if not curentCell.visited:
            curentCell.visited=True
            if curentCell != end:
                curentCell.color=YELLOW
            if curentCell==end:
                drawShortesPath(cameFrom, end, drawGrid)
                end.color=TURQUOISE
                start.color=ORANGE
                return True
            for ns in curentCell.nbrs:
                if(ns.visited==False):
                    cameFrom[ns]=curentCell
                    ar.append(ns)# added neighbours to the Stack
        drawGrid()
#--------------------------------------------------------------------------------------------------
from queue import PriorityQueue
    #A* Algorithm
def hureisticValue(point1, point2):
    x1,y1=point1
    x2,y2=point2
    return abs(x1-x2)+abs(y1-y2) # calculate the h.
'''
g[curentCell] is the cost of the path of each cell from start node to node ‘curentCell’
h[curentCell] is a heuristic function of each cell that estimates cost of the cheapest path from node ‘curentCell’ to the goal node
f[curentCell]=g[curentCell]+h[curentCell]
'''
def drawShortesPath(cameFrom,curentCell,drawGrid):
    while curentCell in cameFrom: # here we backtrack from end to start
        curentCell=cameFrom[curentCell] # we fetch parent of each cell update curentCell to its own parent.
        curentCell.color=PURPLE # change color of curentCell.
        drawGrid()

def algorithmA(drawGrid,grid,start,end):
    pq=PriorityQueue()
    tieBreaker=0 # it is use to break tie of cells which have same f value.
    pq.put((0,tieBreaker,start)) # add start cell to the priority Queue.
    cameFrom={} # keep track of parent of cell
    """
Assign infinity to f and g value of each cell of grid
assign f=0, g=h of start cell. because we starting from start cell.
    """
    g={eachcolumn:float("inf") for eachRow in grid for eachcolumn in eachRow}
    g[start]=0
    f={eachcolumn:float("inf") for eachRow in grid for eachcolumn in eachRow}
    f[start]=hureisticValue(start.getPos(),end.getPos())
    openSet={start} # it is a set which provide the uniqueness, means it is ensure that not a single cell visit more than onece.
    while not pq.empty(): # now until Priority Queue is not empty loop 
        for event in pygame.event.get(): # if user wants to terminate loop
            if event.type == pygame.QUIT:
                pygame.quit()
        curentCell= pq.get()[2] # get first item of priority Queue(Smallest item Present on the Queue)
        openSet.remove(curentCell) # also remove that item from the set
        if curentCell==end: # if item is goal then
            drawShortesPath(cameFrom,end,drawGrid) # bactrack from goal to start
            end.color=TURQUOISE
            start.color=ORANGE
            return True
        for ns in curentCell.nbrs: # adding neighbours which are not visited, in other words which are not present in set
            # beacuse those are unvisited, we just treat the set as visited array.
            #and update its g anf f values of neighbours of cells.
            tempG=g[curentCell]+1 # as it is a grid not graph so distance between cells is 1
            if tempG<g[ns]: # here we update the g of neighbours, if previous g is greater then update g to latest calculated g which is tempG. 
                cameFrom[ns]=curentCell # keep track of parent of each neighbours
                g[ns]=tempG
                f[ns]=tempG+hureisticValue(ns.getPos(), end.getPos()) # calculate and update f of each neighbours.
                if ns not in openSet: # if neighbours are not visited so they are unique
                    tieBreaker+=1
                    pq.put((f[ns],tieBreaker,ns)) #add neighbours to Priority Queue
                    openSet.add(ns) #add neighbours to set
                    # ns.color=GREEN
        drawGrid()
        if curentCell!=start: #if cell(first item of priority Queue) is not start cell change its color to yellow
            curentCell.color=YELLOW
    return False

    

#--------------------------------------------------------------------------------------------------

def main(window, width):
    tkinterWindowCreation()
    Rows=30
    # 1st step- create the 2D matrix. Each cell contains Cell object
    grid= twoDmatrix(Rows, width)
    #
    start=None
    end=None
    run=True
    while run:
        # 2nd step- draw the Grid
        drawGrid(window, grid, Rows, width)
        # from here we basically create the logics of -how to close window, -mouse clicking events, -key press events -runing the algorithm
        # 3rd step- Events handeling
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False

        # Left mouse button press
            if pygame.mouse.get_pressed()[0]:
                positionOfXandY=pygame.mouse.get_pos()# get coordinates
                row, col=cellIndicator(positionOfXandY, Rows, width)# get cell's row and col
                curentCell=grid[row][col]
                # if start and stop are not pointed in grid then first point start then end 
                if not start and curentCell != end:
                    #make curentCell as start
                    start= curentCell
                    # Initialized color ORANGE to start
                    start.color=ORANGE
                elif not end and curentCell != start:
                    #make curentCell as end
                    end= curentCell
                    # Initialized color TURQUOISE to end
                    end.color=TURQUOISE
                # now after start and end is pointed then barriera are pointed
                elif curentCell !=end and curentCell != start:
                    # Initialized color BLACK to curentCell 
                    curentCell.color=BLACK

        # Right mouse button pressed
            elif pygame.mouse.get_pressed()[2]:
                positionOfXandY= pygame.mouse.get_pos()
                row, col= cellIndicator(positionOfXandY, Rows, width)
                curentCell = grid[row][col]
                # just change the color to resetl cell which is initialize before
                curentCell.color= WHITE
                # now after reset modify start and end if the currentcell is start or end
                if curentCell==start:
                    start=None
                elif curentCell==end:
                    end=None

        #Space key pressed        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for eachrow in grid:
                        for eachcolumn in eachrow:
                            eachcolumn.neighborsOf(grid)
                    if bfsPeeker==True:
                        algorithmB(lambda: drawGrid(window, grid, Rows, width), grid, start, end)
                    elif dfsPeeker== True:
                        algorithmD(lambda: drawGrid(window, grid, Rows, width), grid, start, end)
                    elif aPeeker== True:
                        algorithmA(lambda: drawGrid(window, grid, Rows, width), grid, start, end)
                if event.key== pygame.K_c: # When press ctrlC clear everything
                    tkinterWindowCreation()
                    start=None
                    end=None
                    grid=twoDmatrix(Rows,width) # assign new fresh cell-objects to each cells of grid 

                    
    pygame.quit()
main(window, width)
