class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for ch in s:
            if ch == '[' or ch == '(' or ch == "{":
                stk.append(ch)
            elif ch == ']' or ch == ')' or ch == "}":
                if len(stk) == 0:
                    return False
                curr_parr = stk[-1]
                if curr_parr == "[" and ch == ']':
                    stk.pop()
                elif curr_parr == '{' and ch == '}':
                    stk.pop()
                elif curr_parr == '(' and ch == ')':
                    stk.pop()
                else:
                    return False
        
        if len(stk):
            return False
        return True

        

        