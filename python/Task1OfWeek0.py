#task 1 of 7.1
temperatures = [
    8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
    16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
    13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
    7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
    16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5
]

cold = []
mild = []
comfortable = []

for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)

classified_temperatures = {
    "Cold": cold,
    "Mild": mild,
    "Comfortable": comfortable
}
print(classified_temperatures,"\n");

#task 2 of 7.1

print("Cold temperatures:", len(cold),"\n")
print("Mild temperatures:", len(mild),"\n")
print("Comfortable temperatures:", len(comfortable),"\n")

#task 3 of 7.1
temperatures_fahrenheit = []

for temp in temperatures:
    fahrenheit = (temp * 9/5) + 32
    temperatures_fahrenheit.append(fahrenheit)
    
print("Temperatures in Fahrenheit:", temperatures_fahrenheit,"\n")

#task 4 of 7.1

night_temps = []
evening_temps = []
day_temps = []

for i in range(0, len(temperatures), 3):
    night_temps.append(temperatures[i])
    evening_temps.append(temperatures[i + 1])
    day_temps.append(temperatures[i + 2])

average_day_temp = sum(day_temps) / len(day_temps)

print("Night temperatures:", night_temps,"\n")
print("Evening temperatures:", evening_temps,"\n")
print("Day temperatures:", day_temps,"\n")
print("Average day-time temperature:", average_day_temp,"\n")


## Task 2 of 8.1.1
def generate_permutations(s):
    """
    Generate all unique permutations of a string using recursion.
    
    Args:
        s (str): The input string.
        
    Returns:
        list: A list of all unique permutations of the string.
        
    Example:
        >>> generate_permutations("abc")
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    if len(s) == 1:
        return [s]
    
    permutations = []
    for i, char in enumerate(s):
      
        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(char + perm)
    
    return list(set(permutations))
    
print("Permutations of 'jkl':", generate_permutations("jkl"),"\n")

print("Permutations of 'def':", generate_permutations("def"),"\n")

# task 3 of 8.1.1
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250,
            "file6.txt": 150
        }
    }
}

def calculate_directory_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):
            total_size += calculate_directory_size(value)
        else:
            total_size += value
    return total_size

total_size = calculate_directory_size(directory_structure)
print(f"Total directory size: {total_size} KB \n")

## task 2 of 8.2.2
def longest_common_subsequence(s1, s2):
    """
    Finds the length of the longest common subsequence (LCS) between two strings using dynamic programming.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The length of the LCS.

    Example:
        >>> longest_common_subsequence("abcde", "ace")
        3
    """
    
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]

print("Length of LCS:", longest_common_subsequence("abcde", "abce"),"\n")

#task 3 of 8.2.2
def knapsack(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights.
        values (list): List of item values.
        capacity (int): Maximum weight capacity of the knapsack.
        
    Returns:
        int: Maximum value achievable within the given weight capacity.
        
    Example:
        >>> knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
    """
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value = knapsack(weights, values, capacity)
print("Maximum Value:", max_value)
