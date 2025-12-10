---
title: Exam Panic Sorter
emoji: 📝
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: mit
---


# Exam Panic Sorter – Insertion Sort Tutor

### App Overview

![App overview](screenshots/screenshots:app_overview.png)

### Example Step-by-Step Output

![Insertion sort steps](screenshots/screenshots:example_steps.png)

---

## Problem Breakdown & Computational Thinking

This project simulates **Insertion Sort** using student marks (exam/quiz scores) as the data. The goal is to help beginners understand how the algorithm works *step by step* in a realistic and relatable context.

**Decomposition**

* Accept a list of marks from the user
* Sort the marks using insertion sort
* Track comparisons and shifts
* Explain each step in plain language
* Display a summary and optional step-by-step output

**Pattern Recognition**

* Each new mark is compared against previously sorted marks
* Larger values shift right until the correct position is found
* This repeated behavior matches how students add new grades over time

**Abstraction**

* Technical details (loops, indices) are hidden from the user
* The user only sees meaningful explanations like “a mark moves right” or “a mark is inserted”

**Algorithm Design (IPO)**

* **Input:** Comma-separated list of marks
* **Processing:** Insertion sort with comparison and shift counting
* **Output:** Sorted list, step explanations, total comparisons, total shifts

---

## Steps to Run Locally

1. Clone or download this repository.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:

   ```bash
   python app.py
   ```
5. Open the Gradio link in your browser (usually `http://127.0.0.1:7860`).

---

## Hugging Face Link

Try the deployed version of the app here:

👉 **(https://huggingface.co/spaces/Joelanko2/Exam-panic-sorter/upload/main)**

---

## Testing & Verification

The app was tested with a variety of inputs to ensure correctness and robustness:

* **Normal case:** `73, 65, 78, 90, 83`

  * Correctly sorted to `[65, 73, 78, 83, 90]`
  * Step-by-step output matches insertion sort behavior

* **Single value:** `80`

  * Output remains `[80]` with zero comparisons and shifts

* **Duplicate values:** `70, 70, 65`

  * Correctly sorted to `[65, 70, 70]`

* **Invalid input:** `73, abc, 80`

  * App displays a clear error message asking for valid numbers

* *Empty input:** *(no marks entered)*

  * App prompts the user to enter at least one valid mark

The sorted output was also cross-checked with Python’s built-in `sorted()` function for verification.

---

# Author & Acknowledgment

*Author:* Joel Ankomah
*Course:* CISC‑121 – Introduction to Computing

*AI Acknowledgment:*
I used ChatGPT (AI Level up to 4) to help improve README wording and review the structure of my project. I wrote, tested, and verified the final Python code myself.
