def horners_method(coefficients, x):
  """Evaluates a polynomial using Horner's Rule.

  coefficients: List of coefficients from highest degree to lowest.
  """
  mult_count = 0
  add_count = 0
  loop_iterations = 0

  result = coefficients[0]
  for i in range(1, len(coefficients)):
    loop_iterations += 1
    result = (result * x) + coefficients[i]
    mult_count += 1  # One multiplication per iteration
    add_count += 1  # One addition per iteration

  return result, mult_count, add_count, loop_iterations


def brute_force_method(coefficients, x):
  """Evaluates a polynomial using the Brute Force method (naive exponentiation)."""
  n = len(coefficients) - 1
  mult_count = 0
  add_count = 0
  total_val = 0

  for i, coeff in enumerate(coefficients):
    degree = n - i
    if degree == 0:
      term_val = coeff
    else:
      # Compute x^degree naively
      term_val = 1
      for _ in range(degree):
        term_val *= x
        mult_count += 1
      # Multiply by the coefficient
      term_val *= coeff
      mult_count += 1

    total_val += term_val
    if degree > 0:
      add_count += 1

  return total_val, mult_count, add_count


# Given Polynomial: P(x) = 6x^6 + 5x^5 + 4x^4 - 3x^3 + 2x^2 + 8x - 7
# Coefficients from highest degree to lowest:
coefficients = [6, 5, 4, -3, 2, 8, -7]
x_val = 3

# Run Horner's Method
h_result, h_mult, h_add, h_iters = horners_method(coefficients, x_val)
print("--- Horner's Method (Q2 Part i) ---")
print(f"Result: {h_result}")
print(f"Multiplications: {h_mult}")
print(f"Additions: {h_add}")
print(f"Loop Iterations: {h_iters}\n")

# Run Brute Force Method
bf_result, bf_mult, bf_add = brute_force_method(coefficients, x_val)
print("--- Brute Force Method (Q2 Part ii) ---")
print(f"Result: {bf_result}")
print(f"Multiplications: {bf_mult}")
print(f"Additions: {bf_add}")