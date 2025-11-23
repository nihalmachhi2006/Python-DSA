def push(stack, item):
    stack.append(item)
    print(f"Pushed: {item}")

def pop_item(stack):
    if not stack:
        print("Stack is empty")
    else:
        print("Popped:", stack.pop())

def peek(stack):
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def display(stack):
    print("Stack:", stack)


stack = []

push(stack, 10)
push(stack, 20)
push(stack, 30)

display(stack)

peek(stack)

pop_item(stack)
display(stack)

peek(stack)
