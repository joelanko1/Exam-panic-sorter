import gradio as gr


def parse_input(numbers_str: str):
    """
    Takes what the user types (like: "73, 65, 80")
    and turns it into a list of integers: [73, 65, 80].

    If the user types something that isn't a number,
    Python will throw an error and we handle it later.
    """
    parts = numbers_str.split(",")
    nums = []

    for p in parts:
        p = p.strip()  # remove extra spaces
        if p == "":
            continue
        nums.append(int(p))  # may raise ValueError (on purpose)

    return nums


def insertion_sort_with_steps(nums):
    """
    Runs insertion sort, but also keeps track of everything
    that happens so we can show it step-by-step to the user.

    We also count how many comparisons and shifts happen,
    so the user can see how much work the algorithm does.
    """
    arr = nums.copy()
    steps = []

    comparisons = 0
    shifts = 0

    # Step 0: starting point
    steps.append({
        "step": 0,
        "current": None,
        "array": arr.copy(),
        "explanation": "We start with the marks exactly how the student entered them."
    })

    # Standard insertion sort loop
    for i in range(1, len(arr)):
        key = arr[i]          # the new mark we're inserting
        j = i - 1             # look to the left of it

        steps.append({
            "step": len(steps),
            "current": key,
            "array": arr.copy(),
            "explanation": (
                f"A new mark ({key}) comes in. "
                "We now place it into the sorted section on the left."
            )
        })

        # Shift bigger marks to the right until key fits
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]   # shift happens here
            shifts += 1

            steps.append({
                "step": len(steps),
                "current": key,
                "array": arr.copy(),
                "explanation": (
                    f"{arr[j + 1]} is higher than {key}, "
                    "so it gets shifted one position to the right."
                )
            })

            j -= 1

        # Count the last comparison when the loop stops
        if j >= 0:
            comparisons += 1

        # Insert key into the correct spot
        arr[j + 1] = key
        steps.append({
            "step": len(steps),
            "current": key,
            "array": arr.copy(),
            "explanation": (
                f"{key} is placed at index {j + 1}. "
                f"Now the first {i + 1} marks are fully sorted."
            )
        })

    return arr, steps, comparisons, shifts


def run_exam_panic_sorter(numbers_str, show_steps):
    """
    This function connects the UI to the actual algorithm.
    It's what runs when the user clicks the button.
    """

    # If the user didn't type anything
    if not numbers_str or numbers_str.strip() == "":
        return "Please enter at least one mark.", "No steps to show."

    # Try converting the input into numbers
    try:
        nums = parse_input(numbers_str)
    except ValueError:
        return (
            "Error: only type whole numbers separated by commas (example: 73, 65, 80).",
            "Steps are hidden because the input was invalid."
        )

    if len(nums) == 0:
        return "Please enter at least one valid mark.", "No steps to show."

    # Run the insertion sort
    sorted_nums, steps, comparisons, shifts = insertion_sort_with_steps(nums)

    # Build the summary box
    summary = (
        "=== Exam Panic Sorter Summary ===\n"
        f"Original marks: {nums}\n"
        f"Sorted marks:   {sorted_nums}\n\n"
        f"Total comparisons: {comparisons}\n"
        f"Total shifts:      {shifts}"
    )

    # Build the step-by-step explanation
    if show_steps:
        step_text = ""
        for step in steps:
            step_text += f"**Step {step['step']}:** {step['array']}  \n"
            step_text += f"_{step['explanation']}_\n\n"
    else:
        step_text = (
            "Step-by-step output is hidden. "
            "Check the box above if you want to see how the algorithm works internally."
        )

    return summary, step_text


# --------- Gradio UI ---------

with gr.Blocks(title="Exam Panic Sorter – Insertion Sort Tutor") as demo:
    gr.Markdown(
        """
        # Exam Panic Sorter – Insertion Sort Tutor

        Paste your exam or quiz marks below (for example: `73, 65, 80, 90, 58`).

        This app uses **Insertion Sort** to organize your grades and explains
        what happens at each step, like adding new marks over the semester.
        """
    )

    input_box = gr.Textbox(
        label="Enter your marks (comma-separated)",
        placeholder="e.g. 73, 65, 80, 90, 58"
    )

    show_steps_checkbox = gr.Checkbox(
        label="Show each step of the algorithm",
        value=True
    )

    sort_button = gr.Button("Sort my marks")

    summary_output = gr.Textbox(
        label="Summary",
        lines=8
    )

    steps_output = gr.Markdown(
        label="Step-by-step walkthrough"
    )

    sort_button.click(
        fn=run_exam_panic_sorter,
        inputs=[input_box, show_steps_checkbox],
        outputs=[summary_output, steps_output]
    )



if __name__ == "__main__":
    demo.launch()
