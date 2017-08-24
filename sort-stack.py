# Sort a stack, using only stacks. No lists or other data structures allowed.

def sort_stack(stack):
    if not stack: return stack
    temp_stack = []
    sorted_stack = [stack.pop()]

    while stack:
        val = stack.pop()

        if val >= sorted_stack[-1]:
            sorted_stack.append(val) # Insert into sorted stack if it's the largest element

        else:
            while sorted_stack:  # Loop through the sorted stack until we find the correct place to insert the element
                if val >= sorted_stack[-1]:
                    sorted_stack.append(val)
                    break
                else: 
                    temp_stack.append(sorted_stack.pop())

            else: 
                sorted_stack.append(val)  # The val is the lowest value if we hit the else condition.

            while temp_stack: 
                sorted_stack.append(temp_stack.pop())  # Push all the elements in order back onto the sorted stack

    return sorted_stack


stack = [1,2 ,5, 3, 6, 3, 8, 43, 3, 2, 33, 44 , 7, 44]

print(sort_stack(stack))

