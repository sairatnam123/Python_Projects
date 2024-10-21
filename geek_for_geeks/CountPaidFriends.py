def count_paid_friends(n, friends, paid):
    # Step 1: Build a graph to represent friendships
    graph = {i: [] for i in range(1, n + 1)}  # Create an adjacency list for the graph
    for u, v in friends:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Create a visited set to track nodes we've already processed
    visited = set()

    # Step 3: DFS function to explore all connected components
    def dfs(student):
        stack = [student]
        component = []  # List to hold the current connected component
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                component.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited and paid[neighbor - 1] == 1:  # Only consider paid neighbors
                        stack.append(neighbor)
        return component

    # Step 4: Traverse all students and find the connected components of paid students
    paid_groups = 0
    for student in range(1, n + 1):
        if student not in visited and paid[student - 1] == 1:  # Only start DFS if the student has paid
            component = dfs(student)
            if component:  # If the component has paid students, count it
                paid_groups += 1

    return paid_groups

# Example usage:
n = 3  # Number of students
friends = [[2, 1], [1, 3], [2, 3]]  # Friendships between students
paid = [1, 0, 1]  # 1 means paid, 0 means not paid

result = count_paid_friends(n, friends, paid)
print("Number of distinct paid groups:", result)  # Output should be 2
