#A* algorithmn : finding the shortest path on graph
class Node:
    def __init__(self,parent=None,position=None):
        self.parent = parent #where it come from e.g. Node
        self.position = position #where it stay in the graph e.g (row,column)
        self.g = 0 #cost from start position to current position
        self.h = 0 #estimated cost from end to current position, a^2 + b^2 = c^2
        self.f = self.g + self.h #g+h = total cost

def A_star_algor(maze,start,end):
    show_path = maze
    openList = [] #storing the set of nodes that is going to be evaluated
    closedList = [] #storing the set of nodes that has been evaluated (e.g. store their position)
    startNode = Node(None,start) #prepare for the start position

    openList.append(startNode)
    while len(openList)>0:
        #find the currentNode which is the one with the LOWEST f cost
        currentNode = openList[0]
        currentNode_index = 0
        for index,node in enumerate(openList):
            if node.f < currentNode.f:
                currentNode = node
                currentNode_index = index

        #remove currentNode from openList and add it to the closedList which indicates that it has been CHOSEN before
        openList.pop(currentNode_index)
        closedList.append(currentNode.position)

        #if currentNode == endNode(destination), end the finding and show and reverse the path
        if currentNode.position == end:
            show_path[currentNode.position[0]][currentNode.position[1]] = 6
            while currentNode.parent != None:
                currentNode = currentNode.parent
                show_path[currentNode.position[0]][currentNode.position[1]] = 6
            return show_path
        #prepare the moving directions to all neighbours
        directions = ((0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1))
        #for each neighbour of currentNode
        for direction in directions:
            #if it is not walkable(e.g. out of range/wall), try next direction
            if currentNode.position[0]+direction[0]<0 or currentNode.position[0]+direction[0]>=len(maze) \
                or currentNode.position[1]+direction[1]<0 or currentNode.position[1]+direction[1]>=len(maze[0]):
                continue
            elif maze[currentNode.position[0]+direction[0]][currentNode.position[1]+direction[1]] != 0:
                continue

            #if it is in closedList, try next
            if (currentNode.position[0]+direction[0],currentNode.position[1]+direction[1]) in closedList:
                continue
            #if it is valid, do something
            neighbour = Node(currentNode,(currentNode.position[0]+direction[0],currentNode.position[1]+direction[1]))
            neighbour.g = currentNode.g + 1 #you can have another methods for calculating it
            neighbour.h = (neighbour.position[1]-end[1])**2+(neighbour.position[0]-end[0])**2
            in_openList = False
            for index,open_Node in enumerate(openList): #check if it is already in the openList, if so, do something
                if neighbour.position == open_Node.position:
                    in_openList = True
                    if neighbour.g < open_Node.g: #if it is better than previous path(based on g cost)
                        openList[index] = neighbour # replace the one with a better path

            if not in_openList:
                openList.append(neighbour)





if __name__ == '__main__':
    maze = ([0,1,0,0,0], #0 for walkable 1 for unwalkable e.g. wall
            [0,0,1,0,0],
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,0,0,0,0])
    start = (0,0)
    end = (3,4)
    result_path = A_star_algor(maze,start,end)
    for row in result_path:
        for column in row:
            print(column,end=' ')
        print()
