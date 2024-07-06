from Mazes import draw_maze_line
import turtle
import json

def drawMaze(maze):
    horizontalMazeLineList = maze.getHorizontalLineRepresentation()
    verticalMazeLineList = maze.getVerticalLineRepresentation()

    drawMazeFromRepresentation(False, 'black', 20, 2, -120, -200, horizontalMazeLineList, verticalMazeLineList)

def drawMazeFromRepresentation(tracerOn, colour, roomSize, lineWidth, startX, startY, horizontalMazeLineList, verticalMazeLineList):
    mazeTurtle = turtle.Turtle()
    mazeTurtle.reset()
    mazeTurtle.speed(0)
    turtle.tracer(tracerOn)

    mazeTurtle.color(colour)
    mazeTurtle.penup()
    mazeTurtle.goto(startX, startY)
    mazeTurtle.pendown()
    mazeTurtle.width(lineWidth)


    xPos = startX
    yPos = startY + roomSize

    while len(horizontalMazeLineList) > 0: 
        mazeLine = horizontalMazeLineList.pop(0)
        penUp = mazeLine.pop()

        direction = 0
        draw_maze_line(mazeTurtle, roomSize, penUp, mazeLine)
        mazeTurtle.penup()
        mazeTurtle.goto(xPos, yPos)
        mazeTurtle.pendown()
        yPos += roomSize

    mazeTurtle.left(90)
    mazeTurtle.penup()
    mazeTurtle.goto(startX, startY)
    mazeTurtle.pendown()

    xPos = startX + roomSize
    yPos = startY
    while len(verticalMazeLineList) > 0:
        mazeLine = verticalMazeLineList.pop(0)
        penUp = mazeLine.pop()

        draw_maze_line(mazeTurtle, roomSize, penUp, mazeLine)
        mazeTurtle.penup()
        mazeTurtle.goto(xPos, yPos)
        mazeTurtle.pendown()
        xPos += roomSize


def test(mazeFile):
    with open(mazeFile, 'r') as file:
        mazeData = json.load(file)
    
    mazeHoriz = mazeData["mazeHorizontal"]
    mazeVert = mazeData["mazeVertical"]
    
    drawMazeFromRepresentation(True, 'blue', 20, 2, -120, -200, mazeHoriz, mazeVert)
    turtle.exitonclick()


if __name__ == '__main__':
    mazeFile = "MazeObjects/"
    mazeFile += input("select maze file to load: \n")
    mazeFile += '.json'
    test(mazeFile)