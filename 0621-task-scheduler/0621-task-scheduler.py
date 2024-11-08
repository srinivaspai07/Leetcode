from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Maximum frequency of any task
        max_freq = max(task_counts.values())
        
        # Number of tasks with the maximum frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Calculate the minimum intervals required
        part_count = max_freq - 1  # Number of parts between the most frequent tasks
        part_length = n - (max_count - 1)  # Length of each part excluding the most frequent tasks
        empty_slots = part_count * part_length  # Total empty slots
        available_tasks = len(tasks) - (max_freq * max_count)  # Remaining tasks to fill the slots
        idles = max(0, empty_slots - available_tasks)  # Idle intervals needed
        
        return len(tasks) + idles
