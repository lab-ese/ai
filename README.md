# AI Lab Practical Examination Guide

This guide contains the theory, explanations, and viva questions for all 19 experiments in the AI Lab syllabus.

---

## 1. Tic Tac Toe (Non-AI)
- **Explanation**: Uses rule-based heuristics (Win > Block > Center > Corners > Edges) without searching future states.
- **Complexity**: Time O(1), Space O(1).
- **Viva**: Difference between AI and Non-AI? Why Center first?

## 2. N-Queens (Non-AI)
- **Explanation**: Uses Backtracking to place N queens such that no two attack each other.
- **Complexity**: Time O(N!), Space O(N^2).
- **Viva**: What is Backtracking? Why check only the left side?

## 3. Magic Square (Non-AI)
- **Explanation**: Siamese Method for odd-sized squares where sum of all rows/cols/diagonals is constant.
- **Complexity**: Time O(N^2), Space O(N^2).
- **Viva**: Magic Sum formula? Can it work for N=4?

## 4 & 5. Water Jug (DFS & BFS)
- **Explanation**: State-space search using Stack (DFS) or Queue (BFS). BFS finds shortest path.
- **Complexity**: Time O(M*N), Space O(M*N).
- **Viva**: BFS vs DFS? Mathematical condition for solution (GCD)?

## 6. Hill Climbing (8-Puzzle)
- **Explanation**: Greedy local search moving to the neighbor with the best heuristic (Manhattan Distance).
- **Complexity**: Time O(Steps * N^2), Space O(N^2).
- **Viva**: Local Maxima? Plateaus? Ridge?

## 7, 8 & 9. Best First Search (8-Puzzle, Robot, Cities)
- **Explanation**: Informed search using only h(n). Always expands node with lowest heuristic.
- **Complexity**: Time O(b^d), Space O(b^d).
- **Viva**: Is it optimal? Difference from A*?

## 10, 11 & 12. A* Algorithm (8-Puzzle, Robot, Cities)
- **Explanation**: Optimal search using f(n) = g(n) + h(n).
- **Complexity**: Time O(b^d), Space O(b^d).
- **Viva**: What is Admissibility? Consistency? A* vs Dijkstra?

## 13. CSP (Cryptarithmetic)
- **Explanation**: Assigning digits to letters such that mathematical constraints are met. Uses Backtracking.
- **Complexity**: Time O(10!), Space O(K).
- **Viva**: What is CSP? What are All-Diff constraints?

## 14. CSP (Crossword)
- **Explanation**: Fitting words into grid slots using Backtracking and intersection constraints.
- **Complexity**: Time O(Words^Slots), Space O(Grid).
- **Viva**: Unary vs Binary constraints?

## 15. CSP (Map Coloring)
- **Explanation**: Coloring adjacent regions differently using Backtracking.
- **Complexity**: Time O(Colors^Nodes), Space O(Nodes).
- **Viva**: Four Color Theorem? What is Tasmania's impact?

## 16. Minimax (Tic Tac Toe)
- **Explanation**: Recursive algorithm for zero-sum games. Maximizer vs Minimizer.
- **Complexity**: Time O(b^d), Space O(d).
- **Viva**: What is Alpha-Beta pruning? Depth-based scoring?

## 17. NLP (POS Tagging)
- **Explanation**: Marking words as Nouns, Verbs, etc. using NLTK's Averaged Perceptron Tagger.
- **Complexity**: Time O(N), Space O(N).
- **Viva**: Tokenization? Penn Treebank?

## 18. NLP (Similarity Score)
- **Explanation**: Comparing texts using Cosine Similarity (vector angle) and Jaccard Similarity (set overlap).
- **Complexity**: Time O(N), Space O(U).
- **Viva**: Vector Space model? Bag of Words?

## 19. NLP (Spell Checker)
- **Explanation**: Suggesting corrections based on Levenshtein Edit Distance.
- **Complexity**: Time O(L1*L2), Space O(L1*L2).
- **Viva**: Edit operations (Insert, Delete, Substitute)? Levenshtein Distance?
