class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for element in s:
            if element =='{':
                stack.append(element)
            elif element =='[':
                stack.append(element)
            elif element == '(':
                stack.append(element)
            else:
                if stack:
                    if element =='}':
                        if stack.pop() != '{':
                            return False
                    if element ==']':
                        if stack.pop() != '[':
                            return False
                    if element ==')':
                        if stack.pop() != '(':
                            return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False