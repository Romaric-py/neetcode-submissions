class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {o:c for o, c in zip('([{', ')]}')}
        stack = []
        for c in s:
            if self.is_open_bracket(c):
                stack.append(c)
            elif self.is_closed_bracket(c):
                if not stack or brackets[stack[-1]] != c:
                    return False
                stack.pop()
        return not stack
            
    
    def is_open_bracket(self, c):
        return c in '([{'
    
    def is_closed_bracket(self, c):
        return c in '}])'