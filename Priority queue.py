import heapq

# Task class with comparison based on priority (min-heap behavior)
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

# Priority Queue class using a list as a binary heap
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_min(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)

    def decrease_key(self, task_id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                self.heap[i].priority = new_priority
                heapq.heapify(self.heap)
                break

# Task Simulation Example
if __name__ == "__main__":
    pq = PriorityQueue()

    # Insert tasks
    tasks = [
        Task(task_id="A", priority=3, arrival_time=1, deadline=5),
        Task(task_id="B", priority=1, arrival_time=2, deadline=4),
        Task(task_id="C", priority=4, arrival_time=3, deadline=6),
        Task(task_id="D", priority=2, arrival_time=4, deadline=7),
    ]

    print("Inserting tasks into priority queue:")
    for task in tasks:
        print(f"Inserting {task}")
        pq.insert(task)

    # Decrease priority of Task C
    print("\nDecreasing priority of Task C to 0:")
    pq.decrease_key(task_id="C", new_priority=0)

    # Process tasks in priority order
    print("\nProcessing tasks by priority:")
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Processing {task}")
