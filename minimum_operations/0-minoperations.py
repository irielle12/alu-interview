def minOperations(n):
  """
  Calculates the minimum number of operations to reach n characters with Copy All and Paste operations.

  Args:
      n: The target number of characters.

  Returns:
      The minimum number of operations needed, or 0 if n is impossible.
  """
  if n <= 1:
    return 0  # No operations needed for n <= 1

  # Find the largest power of 2 less than or equal to n
  power_of_2 = 1
  while power_of_2 <= n:
    power_of_2 *= 2

  # Calculate the number of copy operations needed (excluding the initial H)
  copy_operations = power_of_2 // 2 - 1

  # Calculate the number of paste operations (excluding the initial H)
  paste_operations = n - power_of_2

  # Total operations is copy + paste + 1 (initial H)
  return copy_operations + paste_operations + 1
