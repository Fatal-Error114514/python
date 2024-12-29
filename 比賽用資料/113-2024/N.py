weight = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
stack = []
post = []
s = input().split()
for i in s:
    if i.isalpha(): # 運算元
        post.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            post.append(stack.pop())
        stack.pop()
    else:   # 運算子
        while stack and weight[stack[-1]] >= weight[i]:
            post.append(stack.pop())
        stack.append(i)
    
while stack:
    post.append(stack.pop())

print(' '.join(post))