class Solution(object):
    def isValid(self, s):

        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        newString = list(s)

        for s in newString:
            if(s not in brackets):
                stack.append(s)
            else:
                if(brackets[s] not in stack): #cases where string is ']'
                    return False
                if(len(stack) > 0):
                    popped = stack.pop()
                    if (brackets[s] != popped):
                        return False
       
        if (len(stack) == 0):
            return True
        else:
            return False
