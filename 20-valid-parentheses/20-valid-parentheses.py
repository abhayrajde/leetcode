class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if(i == "(" or i == "{" or i == "["):
                stack.insert(0,i)
            elif(i == ")"):
                if(stack == []):
                    return(False)
                elif(stack[0] == "("):
                    stack.pop(0)
                else:
                    return(False)
            elif(i == "}"):
                if(stack == []):
                    return(False)
                elif(stack[0] == "{"):
                    stack.pop(0)
                else:
                    return(False)
            elif(i == "]"):
                if(stack == []):
                    return(False)
                elif(stack[0] == "["):
                    stack.pop(0)
                else:
                    return(False)
        if(stack == []):
            return(True)
        else:
            return(False)
            
                
        """
        :type s: str
        :rtype: bool
        """
        