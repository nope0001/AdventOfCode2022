from aocd.models import Puzzle
import datetime

current_time = datetime.datetime.now()

puzzle = Puzzle(year=2022, day=current_time.day)

with open(".\\input_data\\" + str(puzzle.day) + ".txt", "w") as file:
    file.write(puzzle.input_data)