# ifrost

# Homework 1
import numpy as np
import math

## Part 1 ##
# Loops and Recursion

# Problem 1
# Write a recursive function to compute the nth fibonacci number
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Problem 2
# Write a function which uses a for loop to sum the numbers from 0 to n
def sum(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return(total)


## Part 2 ##
# Lists, matrices, and tuples

# Problem 3
# Write a function which takes a matrix and returns the transpose of that matrix
mat = [[1,2,3],[4,5,6],[7,8,9]];
def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    #makes the element at the i,j position in the new matrix set as
    #the j,i position from the original matrix
    new = [[matrix[j][i] for j in range(row)] for i in range(col)]
    return new

# Problem 4
# Write a function which takes two points of the same dimension, and finds the euclidean distance between them
def euclidean(p1,p2):
    total = 0
    #This assumes that the two tuples are of the same size
    for i in range(len(p1)):
        diff = 0
        sq = 0
        diff = p1[i] - p2[i]
        sq = np.square(diff)
        total += sq
    return np.sqrt(total)

## Part 3 ##
# Objects, Trees

# Problem 5
# A Node is an object
# - value : Number
# - children : List of Nodes
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

exTree = Node(1,[Node(2,[]),Node(3,[Node(4,[Node(5,[]),Node(6,[Node(7,[])])])])])

# Write a function to calculate the sum of every node in a tree (iteratively)
def sumNodes(root):
    total = 0
    #Will hold all the individual nodes to be checked
    current = [root]
    while len(current) != 0:
        #For every node in the list, add the value to the total and check for children
        #If there are any children add them to the list
        for node in current:
            total += node.value
            if len(node.children) != 0:
                for child in node.children:
                    current.append(child)
            current.remove(node)
    return total

# Write a function to calculate the sum of every node in a tree (recursively)
def sumNodesRec(root):
    total = root.value
    #As long as there is a child node add that and all its children's values to the total
    if len(root.children) != 0:
        for node in root.children:
            total += sumNodesRec(node)
    return total

## Part 4 ##
# Higher order functions, lambda

# Problem 6

# There is another way of defining a function in python:
f = lambda x: x**2
# f(5) -> 25

# You can return a function from a function
# makePowerFunction takes a number, and returns a function which will raise its argument to that power
makePowerFunction = lambda x: lambda y: y**x

# What does this return?
# print('makePowerFunction(2)(4): ' + str(makePowerFunction(2)(4)))
# 16

# You can also take a function as an argument to a function
# Write a function compose, which takes an inner and outer function
# and returns a new function applying the inner then the outer function to a value
def compose(fo, fi):
    return lambda x: fo(fi(x))

add2 = lambda x: x+2
times2 = lambda x: x*2

# Bonus

# You are given a tree
# Print each level of the tree on a new line

# printTree(exTree):
# 1
# 23
# 4
# 56
# 7

#This function takes a tree and prints the values at different levels does not return anything
def printTree(root):
    All= [[root]]
    while All[-1]:
        nextLvl = []
        for node in All[-1]:
            #extend is used here to make sure that the nodes are listed together at their own levels
            nextLvl.extend([node for node in node.children if node])
        All.append(nextLvl)
    #After all the nodes are added in at their particular levels
    #This nested loop prints out the numbers on different lines according to their levels
    for lvl in All:
        for node in lvl:
            print(node.value, end = '')
        print()

# Keep this print statement
printTree(exTree)
