Assignment 4: Heap Data Structures

This assignment includes the implementation and analysis of heap-based algorithms including **Heapsort** and **Priority Queue** operations. The project is split into two main parts:

Part 1: Heapsort
- Implemented a complete Heapsort algorithm in Python.
- Analyzed time complexity: O(n log n) for best, average, and worst cases.
- Compared empirically with Quicksort and Merge Sort across different input sizes and distributions.

Files:
- `heapsort.py`: Contains the implementation of the heapsort algorithm and test comparisons.
- `sorting_comparison.py`: Measures and prints runtime of Heapsort vs Quicksort vs Merge Sort.

Part 2: Priority Queue
- Implemented a min-heap-based priority queue.
- Created a `Task` class to represent tasks with fields like `task_id`, `priority`, `arrival_time`, and `deadline`.
- Implemented core heap operations:
  - `insert(task)`
  - `extract_min()`
  - `decrease_key(task_id, new_priority)`
  - `is_empty()`

Files:
- `priority_queue.py`: Implements the priority queue and task processing simulation.


Report
- `Assignment4_Heap_Data_Structures_Report.docx`: Detailed report including algorithm descriptions, complexity analysis, and simulation results.

How to Run
```bash
python heapsort.py
python priority_queue.py
```

Make sure Python 3.x is installed.
