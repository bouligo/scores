#!/bin/env python3
# -*- Coding: utf-8 -*-

import sys
import signal

def displayTotal():
	print("+" + "-"*(len(sys.argv[0])+2) + "+" + "+".join(["-"*(max(len(str(grid[0][z+1])),len(str(total[z])))+2) for z in range(len(total))]) + "+")
	print("| " + "=====>" + " | " + " | ".join([str(total[z])+" "*max(0, len(str(grid[0][z+1]))-len(str(total[z]))) for z in range(len(total))]) + " |")
	print("+" + "-"*(len(sys.argv[0])+2) + "+" + "+".join(["-"*(max(len(str(grid[0][z+1])),len(str(total[z])))+2) for z in range(len(total))]) + "+")
		
def displayNames():
	print("+" + "-"*(len(sys.argv[0])+2) + "+" + "+".join(["-"*(max(len(str(grid[0][z+1])),len(str(total[z])))+2) for z in range(len(total))]) + "+")
	print("| " + sys.argv[0] + " | " + " | ".join([str(grid[0][k+1])+" "*max(0,len(str(total[k]))-len(str(grid[0][k+1]))) for k in range(len(grid[0])-1)]) + " |")
	print("+" + "-"*(len(sys.argv[0])+2) + "+" + "+".join(["-"*(max(len(str(grid[0][z+1])),len(str(total[z])))+2) for z in range(len(total))]) + "+")

def ctrl_c(signal_no, frame):
	print("\nFinal scores :")
	displayNames()
	displayTotal()
	sys.exit(0)
	
if __name__ == '__main__':
	signal.signal(signal.SIGINT, ctrl_c)
	
	if len(sys.argv) < 2:
		print("Usage : " + sys.argv[0] + " name1 name2 ...")
		sys.exit(1)

	grid, total = [0], [0 for i in range(len(sys.argv)-1)]
	sys.argv[0] = "Scores"
	grid[0]= [i for i in sys.argv]

	while True:

		new_scores = input(">>>")

		if len(new_scores) == 0:
			pass
		elif len(list(map(int, new_scores.split()))) != len(total):
			print("Incorrect number of input")
			continue
		else:
			grid.append(list(map(int, new_scores.split())))

		total = [0 for i in range(len(sys.argv)-1)]

		for i in range(len(grid)-1):
			for j in range(len(total)):
				total[j] += grid[i+1][j]

		displayNames()
		
		for i in range(len(grid)-1):
			print("| " + " " * len(sys.argv[0]) + " | " + " | ".join([str(grid[i+1][z])+" "*(max(len(str(grid[0][z+1])), len(str(total[z]))) - len(str(grid[i+1][z]))) for z in range(len(grid[i+1]))]) + " |")		

		displayTotal()
