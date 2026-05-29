class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = [0] * len(temperatures)
        stack = [(temperatures[0],0)]
        for i in range(1,len(temperatures),1):
        
            while stack and stack[-1][0] < temperatures[i]:
                lst[stack[-1][1]] = i - (stack[-1][1])
                stack.pop()
            stack.append((temperatures[i],i))
        return lst