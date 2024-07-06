from SearchFiles import AStar, BreadthFirstSearch, DepthFirstSearch, Dijkstra
import Maze

if __name__ == '__main__':
    mazeList = ['MazeObjects/EmptyMaze.json', 
                'MazeObjects/TinyMaze.json', 
                'MazeObjects/SmallMaze.json', 
                'MazeObjects/CheveningHouse.json',
                'MazeObjects/HamptonCourt.json',
                'MazeObjects/MinotaursLabyrinth.json']
    
    for maze in mazeList:

        testMaze = Maze.Maze(maze)
        print(maze, '\n')
        print('DepthFirstSearch')

        pathTimeline = DepthFirstSearch.search(testMaze)
        print('totalSteps:', pathTimeline.totalSteps)
        print()

        print('BreadthFirstSearch')

        pathTimeline = BreadthFirstSearch.search(testMaze)
        print('totalSteps:', pathTimeline.totalSteps)
        print()

        print("Dijkstra's")

        pathTimeline = Dijkstra.search(testMaze)
        print('totalSteps:', pathTimeline.totalSteps)
        print()

        print("A Star")

        pathTimeline = AStar.search(testMaze)
        print('totalSteps:', pathTimeline.totalSteps)
        print()

        
        