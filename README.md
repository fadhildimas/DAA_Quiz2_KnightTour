# DAA E & D Quiz2
Knight's Tour Problem Using DFS (Depth First Search) Algorithm

## Problem
The Knight’s Tour is a sequence of moves of knight on a chessboard such that the knight visits every square exactly once. If the knight ends on a square that is one knight’s move from beginning square (so that it could tour the board again immediately, following the same path), the tour is closed; otherwise. It is open

![5x5 knight tour init image](images/knightsTour.png)

## Problem Analysis
The knight’s tour puzzle is played on a chess board with a single chess piece, the knight. The object of the puzzle is to find a sequence of moves that allow the knight to visit every square on the board exactly once.

One sequence is called a “tour”. 

Limiting the problem:
 - Using 5 x 5 size chess board
 - Start initial at 1,1 (x,y)
![Initial State image](images/initState.png)

In this case we will use the 5 x 5 size board. The upper bound on the number of possible 5-5 chessboards is known to be xxxxx ; however there are still even more possible dead ends.

We will solve the problem using 2 main steps which is:
 - Represent the legal moves of a knight on a chessboard as a graph.
 - Use a graph algorithm  to find a path where every vertex on the graph is visited exactly once.

Building the knight’s tour graph
To represent the knight’s tour problem as a graph we will use the following 2 ideas which is:
 - Each square on the chessboard can be represented as a node in the graph.
 - Use a graph algorithm to find a path through the graph of length rows x columns where every node is only visited exactly once.

In this case we will use Python dictionary to hold our graph.

## Design and Analysis Algorithm

Implementing algorithm on knight’s tour

The search algorithm we will use to solve the problem is the Depth First Search (DFS) algorithm. The depth first search creates a search tree by exploring one branch of the tree as deeply as possible.

The depth first exploration of the graph is exactly what we need in order to find a path with exactly 24 edges. We will see that when the depth-first search algorithm finds a dead end (a place in the graph where there are no more possible moves) it backs up the tree to the next deepest vertex that allows it to make a legal move.

### Source Code
Source Code can be read in knightTour.py
