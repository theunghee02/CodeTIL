class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        answer = 0
        for i in logs:
            if i == '../': 
                if answer >0 : answer -=1
            elif i != './':
                answer +=1
        return answer
