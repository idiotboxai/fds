#b) Write a python program to store names and mobile numbers of your friends in sorted
#order on names. Search your friend from list using Fibonacci search. Insert friend if not
#present in phonebook.

def fibonacci_search(arr, x):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1
    while fib > 1:
        i = offset + fib_m_minus_2 if fib_m_minus_2 <= len(arr) - 1 else len(arr) - 1
        if arr[i][0] < x:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i
        elif arr[i][0] > x:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
        else:
            return i
    return -1

def insert_friend(phonebook, friend_name, mobile_number):
    index = fibonacci_search(phonebook, friend_name)
    if index == -1:
        i = len(phonebook) - 1
        while i >= 0 and phonebook[i][0] > friend_name:
            i -= 1
        phonebook.append(None)
        j = len(phonebook) - 1
        while j > i + 1:
            phonebook[j] = phonebook[j - 1]
            j -= 1
        phonebook[i + 1] = (friend_name, mobile_number)
        print(f"Friend '{friend_name}' with mobile number '{mobile_number}' added successfully.")
    else:
        print(f"Friend '{friend_name}' already exists in the phonebook.")

# Sample phonebook
phonebook = [("Alice", "1234567890"), ("Bob", "9876543210"), ("Eve", "5678901234")]

# Sort the phonebook by names
phonebook.sort(key=lambda x: x[0])

# Search for a friend
friend_to_find = "Bob"
result = fibonacci_search(phonebook, friend_to_find)
if result != -1:
    print(f"Friend '{friend_to_find}' found at index {result}.")
else:
    print(f"Friend '{friend_to_find}' not found in the phonebook.")

# Insert a new friend
new_friend_name = "Charlie"
new_mobile_number = "1112223334"
insert_friend(phonebook, new_friend_name, new_mobile_number)

# Display the updated phonebook
print("Updated Phonebook:")
for name, number in phonebook:
    print(f"Name: {name}, Mobile Number: {number}")
