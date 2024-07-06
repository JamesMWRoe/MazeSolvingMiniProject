import curses
import json

'''This module contains a function which can draw a maze given its json file in the terminal, with each of that maze's rooms
labeled with a number that is the same as that room's node number in the graph created alongside the maze. This should be used
solely for testing purposes, to make it easier to check a room's node number when testing whehter the graph created within the maze
class is correct'''

class MazeTerminal:
    def __init__(self, file):
        with open(file, 'r') as f:
            mazeData = json.load(f)

        self.mazeHorizontalLines = mazeData["mazeHorizontal"]
        self.mazeVerticalLines = mazeData["mazeVertical"]

        curses.wrapper(self.main)

    def main(self, stdscr):
        mazePad = self.setupPad(stdscr)

        self.drawHorizontalLines(mazePad, self.mazeHorizontalLines)
        self.drawVerticalLines(mazePad, self.mazeVerticalLines)
        mazePad.refresh(0, 0, 0, 0, 30, 100)


        while(True):
            pass

    def setupPad(self, stdscr):
        curses.resize_term(50, 200)
        padSizeY = len(self.mazeHorizontalLines) * 2 + 1
        padSizeX = len(self.mazeVerticalLines) * 6 + 1
        mazePad = curses.newpad(padSizeY, padSizeX)
        stdscr.clear()
        stdscr.refresh()
        return mazePad

    def drawHorizontalLines(self, pad, horizontalLines):
        currentLine = 0
        vertex = 0

        for line in horizontalLines:
            blockIsWall = not line.pop()
            current = 0
            
            for block in line:
                wall = '#     '
                if blockIsWall:
                    wall ='######'
                
                for i in range(block):
                    pad.addstr(currentLine, current, wall)
                    pad.addstr(currentLine+1, current+1, ' ' + str(vertex))
                    current += 6
                    vertex += 1
                
                blockIsWall = not blockIsWall

            currentLine += 2

    def drawVerticalLines(self, pad, verticalLines):
        currentLine = 0

        for line in verticalLines:
            blockIsWall = not line.pop()
            current = 1

            for block in line:
                wall = ' '
                if blockIsWall:
                    wall = '#'

                for i in range(block):
                    pad.addstr(current, currentLine, wall)
                    pad.addstr(current + 1, currentLine, '#')

                    current += 2
                
                blockIsWall = not blockIsWall
            
            currentLine += 6






if __name__ == '__main__':
    maze = input("Please Enter the maze you would like to view \n")
    fileLocation = "MazeObjects/" + maze + ".json"
    testTerm = MazeTerminal(fileLocation)