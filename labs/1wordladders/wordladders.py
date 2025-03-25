from dataclasses import dataclass
from collections import deque
from typing import List, Tuple

IN_PATH = "./data/secret/1small1.in"

# for file when testing
def parse_input(file_path: str) -> Tuple[int, int, List[str]]:
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    N, Q = map(int, lines[0].split())  
    words = [line.strip() for line in lines[1:N+1]]
    queries = [line.strip() for line in lines[N+1:]]
    
    return N, Q, words, queries

# builds the graph with an input of words
# first it creates and empty dict with the words as keys
def build_graph(words):
    graph = {word: [] for word in words}
    
    # here we extract the last 4 chars from each words
    for word1 in words:
        last_four = word1[-4:]
        last_four_freq = {}
        # 
        for char in last_four:
            last_four_freq[char] = last_four_freq.get(char, 0) + 1

        # start comparing all other words  
        for word2 in words:
            # if the dupe just continue
            if word1 == word2:
                continue
            
            # store the frequeny of each char in a dict
            word2_freq = {}
            for char in word2:
                word2_freq[char] = word2_freq.get(char, 0) + 1
                
            can_connect = True
            # extract each char and the frequency of that specific char
            for char, freq in last_four_freq.items():
                # compare if the char is in the word2_freq dict OR if the frequency of the char is less than what it needs to be
                if char not in word2_freq or word2_freq[char] < freq:
                    can_connect = False
                    break
            
            if can_connect:
                graph[word1].append(word2)
    
    return graph

def bfs(graph: dict[str, list[str]], start: str, goal: str) -> int:
    if start == goal:
        return 0 
    
    # standard bfs
    # create deque
    queue = deque([(start, 0)])
    # create explored set with the start word added
    explored = set([start]) 
    
    while queue:
        # pop the next word and its distance
        current_word, current_distance = queue.popleft()
        
        if current_word not in graph:
            continue

        # for each adjacanet neighbor in the graph of the current word    
        for neighbor in graph[current_word]:
            # if it is what we are looking for, done, return the distance + 1
            if neighbor == goal:
                return current_distance + 1
            # if we have not seen the new guy, add him to the explored set and append him to the queue to be run through next,
            # the guy will then be poped and ran through the same process until we can find a match or the queue is empty
            # if empty then impossible  
            if neighbor not in explored:
                explored.add(neighbor)
                queue.append((neighbor, current_distance + 1))
    
    return -1

def parse_stdin():
    N, Q = map(int, input().split())
    
    words = [input().strip() for _ in range(N)]
    
    queries = [input().strip() for _ in range(Q)]
    
    return N, Q, words, queries

def main():
    N, Q, words, queries = parse_stdin()
    graph = build_graph(words)
    
    for query in queries:
        start, end = query.split()
        result = bfs(graph, start, end)
        if result == -1:
            print("Impossible")
        else:
            print(result)

if __name__ == "__main__":
    main()