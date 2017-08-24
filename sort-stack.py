# Sort a stack, using only stacks. No lists or other data structures allowed.

def sort_stack(stack):
    if not stack: return stack
    temp_stack = []
    sorted_stack = [stack.pop()]

    while stack:
        val = stack.pop()

        if val >= sorted_stack[-1]:
            sorted_stack.append(val)

        else:
            while sorted_stack:
                if val >= sorted_stack[-1]:
                    sorted_stack.append(val)
                    break
                else:
                    temp_stack.append(sorted_stack.pop())

            else:
                sorted_stack.append(val)

            while temp_stack:
                sorted_stack.append(temp_stack.pop())

    return sorted_stack


stack = [1,2 ,5, 3, 6, 3, 8, 43, 3, 2, 33, 44 , 7, 44]

print(sort_stack(stack))

