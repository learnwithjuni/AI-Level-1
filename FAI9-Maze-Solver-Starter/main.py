import maze as mz
import queue

# construct maze
# X is goal (located at (2, 0))
# O is the player (we'll start at (0, 0))
# * are cells with quicksand (higher cost to travel from this cell to another)
maze = ""
maze += "+---+---+---+\n"  
maze += "|           |\n" # row0
maze += "+   +---+   +\n"
maze += "|     * |   |\n" # row1
maze += "+---+   +   +\n"
maze += "| X         |\n" # row2
maze += "+---+---+---+\n"
      # col0 col1 col2

# row has 14 characters (including new line) so maze width is 14

maze = mz.Maze(maze, 14)
maze.print_maze()