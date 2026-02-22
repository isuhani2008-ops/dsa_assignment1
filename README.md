Recursion Algorithms Project
Project Overview
This project explores the concept of recursion in problem solving.
Recursion is a technique where a function calls itself to solve smaller instances of a problem.

The goal of this project is to:

Understand how recursion works
Compare simple recursive solutions with optimized versions
Analyze time and space complexity
Study how recursion behaves in different types of problems
The project includes four classical recursive problems:

Factorial
Fibonacci
Tower of Hanoi
Binary Search
1. Recursive Factorial
Factorial is a simple example of linear recursion.

It follows the rule:

n! = n × (n-1)!

The recursive solution reduces the problem size by 1 each time until it reaches the base case (0 or 1).

This demonstrates:

Linear recursion
Single recursive call per function
Basic stack behavior
Time Complexity: O(n)
Space Complexity: O(n)

2. Recursive Fibonacci
The Fibonacci sequence follows:

F(n) = F(n-1) + F(n-2)

Two versions were implemented:

Simple Recursive Version
This version directly follows the mathematical definition.

However, it is inefficient because:

Each call makes two new recursive calls.
Many values are recalculated multiple times.
The number of calls grows exponentially.
Time Complexity: O(2^n)
Space Complexity: O(n)

Optimized Version (Using Stored Values)
In this version, previously calculated values are stored and reused.

This avoids repeated computation and improves performance significantly.

Time Complexity: O(n)
Space Complexity: O(n)

This comparison clearly shows why naive Fibonacci recursion is inefficient.

3. Tower of Hanoi
Tower of Hanoi is a classic recursive problem that involves moving disks between rods following specific rules.

The recursive strategy:

Move n-1 disks to helper rod.
Move the largest disk.
Move n-1 disks to destination rod.
This problem demonstrates:

Divide and conquer strategy
Recursive problem breakdown
Exponential growth in recursive calls
Time Complexity: O(2^n)
Space Complexity: O(n)

A trace was shown for N = 3 to understand the movement sequence.

4. Recursive Binary Search
Binary search is a divide-and-conquer algorithm used on sorted arrays.

Instead of checking every element, the array is divided into half in each recursive call.

This demonstrates:

Efficient recursion
Halving search space
Logarithmic complexity
Recurrence Relation: T(n) = T(n/2) + 1

Time Complexity: O(log n)
Space Complexity: O(log n)

Key Learning Outcomes
Through this project, we understand:

Difference between linear, exponential, and logarithmic recursion
Why some recursive algorithms are inefficient
How memoization improves performance
How recursion affects memory usage (call stack)
How recurrence relations determine time complexity
Conclusion
This project highlights the importance of analyzing recursion carefully.

While recursion provides elegant solutions, its efficiency depends on:

Number of recursive calls
Repeated computations
Depth of recursion
Optimized recursive techniques such as memoization and divide-and-conquer significantly improve performance.
