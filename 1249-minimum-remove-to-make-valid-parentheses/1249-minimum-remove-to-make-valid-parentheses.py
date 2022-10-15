class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        res = []
        open_count = close_count = 0
        for char in s:
            if char == "(":
                open_count += 1
                stack.append(char)
                
            elif char == ")":
                if close_count < open_count:
                    close_count += 1
                    stack.append(char)
            
            else:
                stack.append(char)
        
        if open_count == close_count:
            return ("".join(stack))
        else:
            for i in range(len(stack)-1, -1, -1):
                char = stack[i]
                if char == "(":
                    if open_count <= close_count:
                        res.append(char)
                        # open_count -= 1
                    else:
                        open_count -= 1
                else:
                    res.append(char)
            return ("".join(reversed(res)))