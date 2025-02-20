
# Problem
## graph with each node representing a five-letter words

## we draw a edge from u to v if ALL of the last four letters in u, are also in v, anywhere in the word

## hello -> lolem, but not lolem to hello
### this is because 'hello' last four letters exist in lolem (anywhere in the word)

## there -> where, where -> there
### this because the 4 last words are exactly the same

## there -> retch, no edge 

# Input
## first row consists of two integers N, Q, n for number of words, Q for number of queries

## N lines containg one five letter word each
## Q lines follow containing two space separted five-letter words each, the queries

# Output

## for each query, output a single line with the answer
## if success print length of shortest path
## if fail print "Impossible"

# Our task

1. Implement BFS with correct time complexity 
2. Understandable code
3. Good variable names and comments
4. Fix the report
5. Run successful `check_solution.sh` to validate

# Questions

1. How do you represent the problem as a graph and how is the graph built?
- Answer: 

2. If one were to perform backtracking (find the path along which we went), how would that be done?
- Answer:

3. What is the time complexity, and more importantly why?
- Answer:

4. Is it possible to solve the problem with DFS: why or why not?
- Answer

5. Can you think of any applications of this? Of BFS/DFS in general?
- Answer: