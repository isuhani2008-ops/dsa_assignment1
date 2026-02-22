# ---

## 1️ Factorial (Simple Recursion)

### Time Complexity: O(n)

# **Justification:**
# - The function makes one recursive call for each value from `n` down to `1`.
# - So total calls = `n`.
# - Each call performs one multiplication.
# - Therefore, total operations grow linearly with `n`.

# ➡ **Time Complexity = O(n)**

### Space Complexity: O(n)

# **Justification:**
# - Each recursive call stays in the call stack until the base case is reached.
# - Maximum recursion depth = `n`.
# - So stack space used is proportional to `n`.

# ➡ **Space Complexity = O(n)**

# ---