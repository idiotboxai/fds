'''
b) Write a python program to store roll numbers of student array who attended training
program in sorted order. Write function for searching whether particular student
attended training program or not, using Binary search and Fibonacci search
'''
def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False

def fibonacci_search(arr, x):
    def fibonacci(n):
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return fib

    n = len(arr)
    fib = fibonacci(n)

    offset = 0
    while fib[-2] > 0:
        i = min(offset + fib[-2], n - 1)
        if arr[i] == x:
            return True
        elif arr[i] < x:
            fib = fib[:-2]
            offset = i
        else:
            fib = fib[:-1]

    return False

def main():
    # Example data: sorted roll numbers of students who attended training
    roll_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    while True:
        print("\nMenu:")
        print("1. Search for a student (Binary Search)")
        print("2. Search for a student (Fibonacci Search)")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            student_to_search = int(input("Enter the student roll number to search: "))
            if binary_search(roll_numbers, student_to_search):
                print(f"Student {student_to_search} attended the training program (Binary Search)")
            else:
                print(f"Student {student_to_search} did not attend the training program (Binary Search)")
        elif choice == "2":
            student_to_search = int(input("Enter the student roll number to search: "))
            if fibonacci_search(roll_numbers, student_to_search):
                print(f"Student {student_to_search} attended the training program (Fibonacci Search)")
            else:
                print(f"Student {student_to_search} did not attend the training program (Fibonacci Search)")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
