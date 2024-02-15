def print_stats_decorator(func):
    def wrapper(numbers):
        result = func(numbers)
        count = len(numbers)
        average = sum(numbers) / count if count > 0 else 0
        maximum = max(numbers) if numbers else None
        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)
        return result
    return wrapper

@print_stats_decorator
def process_numbers(numbers):
    return numbers

def printStats(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            numbers = list(map(float, line.split()))
            process_numbers(numbers)

# Example usage:
# Assuming you have a file named 'data.txt' containing lines of numbers
printStats('data.txt')
