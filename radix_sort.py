def counting_sort(arr, exp, steps, update_progress=None, text_widget=None):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
        step_text = f"Counting Sort on digit {exp}: {arr}"
        steps.append(step_text)
        if update_progress:
            update_progress(step_text, i / len(arr), text_widget)

def radix_sort(arr, steps, update_progress=None, text_widget=None):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp, steps, update_progress, text_widget)
        exp *= 10
