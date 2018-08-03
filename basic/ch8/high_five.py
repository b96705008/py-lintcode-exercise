"""
Description
There are two properties in the node student id and scores, 
to ensure that each student will have at least 5 points, 
find the average of 5 highest scores for each person.


Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return
"""
from Queue import PriorityQueue

class Record:
    def __init__(self, student_id, score):
        self.student_id = student_id
        self.score = score


class Solution:
    """
     * @param results a list of [student_id, score]
     * @return find the average of 5 highest scores for each person
     * Map (student_id, average_score)
    """
    def highFive(self, records):
        k = 5
        if records is None or len(records) == 0:
            return {}

        results = {}
        grades = {}

        for r in records:
            student_id = r[0]
            score = r[1]

            if student_id not in grades:
                grades[student_id] = PriorityQueue(maxsize=k)

            if not grades[student_id].full():
                grades[student_id].put(score)
            elif score > grades[student_id].queue[0]:
                grades[student_id].get()
                grades[student_id].put(score)

        return {s_id: sum(q.queue) / 5.0 for s_id, q in grades.items()}


if __name__ == '__main__':
    sol = Solution()

    records = [[1,100],[1,91],[1,92],[2,10],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
    print sol.highFive(records)





