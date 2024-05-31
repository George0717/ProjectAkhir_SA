def pivot_sort(arr, steps, update_progress=None, text_widget=None, start=0, end=None, depth=0):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr
    
    pivot = arr[end]
    left = start
    right = end - 1
    
    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        step_text = f"Swapped: {arr}"
        steps.append(step_text)
        if update_progress:
            update_progress(step_text, left / end, text_widget)
    
    arr[left], arr[end] = arr[end], arr[left]
    step_text = f"Moved pivot: {arr}"
    steps.append(step_text)
    if update_progress:
        update_progress(step_text, (left + 1) / end, text_widget)
    
    pivot_sort(arr, steps, update_progress, text_widget, start, left - 1, depth + 1)
    pivot_sort(arr, steps, update_progress, text_widget, left + 1, end, depth + 1)
    return arr
