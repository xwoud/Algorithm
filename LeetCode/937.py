from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs_stack = []
        letter_logs_stack = []

        for log in logs:
            t = log.split()
            identifier, logs = t[0], ' '.join(t[1:])
            if logs[0].isdigit():
                digit_logs_stack.append(log)
            else:
                letter_logs_stack.append((identifier, logs))
        letter_logs_stack.sort(key=lambda x: (x[1],x[0]))

        return [f'{x} {y}' for x,y in letter_logs_stack] + digit_logs_stack