# Sudoku Solver (Simulated Annealing + Backtracking)

A 9x9 Sudoku solver that first tries **Simulated Annealing (SA)** for a fast heuristic solution and automatically falls back to **Backtracking** for a guaranteed solution.

> 🎯 Goal: combine a metaheuristic approach (SA) with an exact search (Backtracking) and compare their behavior.

---

## ✨ Features
- **Two solvers**: Simulated Annealing (probabilistic) + Backtracking (exact).
- **Progress logs** during SA (iteration, cost, temperature).
- Works on standard **9×9** Sudoku puzzles.
- Pure Python, **no external dependencies**.

---

## 📦 Requirements
- Python ≥ 3.8  
(uses only the standard library: `random`, `math`)

---

## 🚀 How to Run
```bash
python sudoku_solver.py
