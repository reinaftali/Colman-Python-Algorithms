

def dnc(base, combine):
    def recursive_dnc(arr, left, right):
        if left == right:
            return base(arr[left])
        mid = (left + right) // 2
        left_result = recursive_dnc(arr, left, mid)
        right_result = recursive_dnc(arr, mid + 1, right)
        return combine(left_result, right_result)

    def wrapper(arr):
        if not arr:
            raise ValueError("Array cannot be empty")
        return recursive_dnc(arr, 0, len(arr) - 1)

    return wrapper


def maxAreaHist(hist):
    stack = []
    max_area = 0
    index = 0

    while index < len(hist):
        if not stack or hist[stack[-1]] <= hist[index]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (hist[top_of_stack] *
                   ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (hist[top_of_stack] *
               ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area
