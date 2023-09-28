class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for number in tokens:
            if number == '+':
                a=stack.pop()
                b=stack.pop()
                c=a+b
                stack.append(c)
            elif number =="/":
                a=stack.pop()
                b=stack.pop()
                c = int(b / a)
                stack.append(c)
            elif number =="*":
                a=stack.pop()
                b=stack.pop()
                c = b * a
                stack.append(c)
            elif number =="-":
                a=stack.pop()
                b=stack.pop()
                c = b - a
                stack.append(c)
            else:
                stack.append(int(number))
        return stack[-1]