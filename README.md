# AI FUZZY Tic-Tac-Toe (Minimax Implementation)

A Python CLI application demonstrating the **Minimax Decision Algorithm** for perfect-play AI.

<img width="374" height="702" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/4c3a81ae-0cfb-4adc-bc67-a7a65668f664" />
# Algorithmic Deep-Dive

* **Recursion & Backtracking:** The AI evaluates every possible future board state using a recursive tree search.
* **Optimization:** In-place board mutation to ensure $O(d)$ space complexity where $d$ is the depth of the tree.
* **Perfect Play:** The implementation is mathematically guaranteed to never lose; it will either win or force a draw.

# Execution
python main.py
