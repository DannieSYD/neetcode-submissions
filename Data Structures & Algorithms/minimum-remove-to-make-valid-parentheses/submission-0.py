class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_output = ""
        for c in s:
            if c == ")":
                if len(stack) == 0:
                    continue;
                else:
                    stack.pop()
            elif c == "(":
                stack.append(c)
            s_output += c
        
        stack = []
        reversed_s = s_output[::-1]
        s_reverse_output = ""
        for c in reversed_s:
            if c == "(":
                if len(stack) == 0:
                    continue;
                else:
                    stack.pop()
            elif c == ")":
                stack.append(c)
            s_reverse_output += c
        
        return s_reverse_output[::-1]



        