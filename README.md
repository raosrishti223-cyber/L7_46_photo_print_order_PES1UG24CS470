## Lab 7: Fuzz Testing

### About

This project focuses on fuzz testing a Python-based Photo Print Order application using the Hypothesis library. The application contains three functions for parsing print orders, calculating average file sizes, and calculating payable amounts.

The original application was tested with automatically generated inputs to identify errors caused by unexpected or invalid inputs. The identified issues were fixed by adding input validation and defensive programming.

### Files

| File | Description |
|---|---|
| `photo_print_order.py` | Modified application with fixes for input validation issues. |
| `test_photo_print_order.py` | Hypothesis test file containing tests for all three functions. |
| `Lab7_Report.pdf` | Report containing screenshots of the original application, failing test results, fixed application, and successful test results. |

### Functions Tested

1. `parse_order()` – Parses print size and number of copies.
2. `file_size_average()` – Calculates the average file size from comma-separated values.
3. `payable_amount()` – Calculates the payable amount after tax and discount.

### Testing Performed

- Executed the original application.
- Used Hypothesis to generate unexpected inputs and identify failures.
- Captured screenshots of the failing test results.
- Modified the application to handle invalid and unexpected inputs.
- Executed the fixed application.
- Reran the Hypothesis tests to verify the fixes.

### Test Result

All three Hypothesis test functions passed after modifying the application.

### Technologies Used

- Python
- Hypothesis
- Pytest

`LAB_7_Fuzzing_for_Input_Validation_Bugs_PES1UG24CS470.pdf` can be referred for the execution screenshots and test results.