Git
1. What is Git?

Git is a Version Control System (VCS) used to track changes in code and files. It helps developers save different versions of a project, collaborate with others, and restore previous versions if needed.

2. What is GitHub?

GitHub is an online platform that stores Git repositories on the cloud. It allows developers to collaborate, share code, manage projects, and keep backups of their repositories.

3. Commands Learned
git init

Creates a new Git repository in the current folder.

git init
git add .

Adds all modified and new files to the staging area.

git add .
git commit

Saves the staged changes with a message.

git commit -m "Initial commit"
git push

Uploads local commits to a remote repository such as GitHub.

git push origin main
Arrays
1. What is an Array?

An array is a data structure used to store multiple elements of the same type in a single variable. Elements are stored in contiguous memory locations and can be accessed using an index.

Example:

arr = [10, 20, 30, 40]
arr[0] = 10
arr[1] = 20
arr[2] = 30
arr[3] = 40
2. O(1) vs O(n)
Complexity	Meaning	Example
O(1)	Constant time. Execution time does not depend on input size.	Accessing an element by index: arr[2]
O(n)	Linear time. Execution time increases with input size.	Searching for an element in an unsorted array

Example:

arr[3]      # O(1)
for i in arr:
    print(i)    # O(n)
3. Maximum Element

The maximum element is the largest value present in the array.

Example:

arr = [5, 8, 2, 12, 7]

Maximum element = 12

Python code:

arr = [5, 8, 2, 12, 7]

max_element = arr[0]

for num in arr:
    if num > max_element:
        max_element = num

print(max_element)

Output:

12

Time Complexity: O(n)

4. Second Largest Element

The second largest element is the largest value after the maximum element.

Example:

arr = [5, 8, 2, 12, 7]
Largest = 12
Second Largest = 8

Python code:

arr = [5, 8, 2, 12, 7]

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)

Output:

8

Time Complexity: O(n)