import sys
t = 79
for a0 in range(t):
    s = input().strip()
    stack = []
    flag = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if len(stack) == 0 or stack[len(stack)-1] != '(':
                    flag = False
                    break
                else:
                    stack.pop()
            elif s[i] == '}':
                if len(stack) == 0 or stack[len(stack)-1] != '{':
                    flag = False
                    break
                else:
                    stack.pop()
            elif s[i] == ']':
                if len(stack) == 0 or stack[len(stack)-1] != '[':
                    flag = False
                    break
                else:
                    stack.pop()
    if flag:
        print("YES")
    else:
        print("NO")
