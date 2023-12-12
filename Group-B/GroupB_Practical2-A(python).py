''''

Write a python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using binary search (recursive and nonrecursive).
Insert friend if not present in phonebook.


'''

class Book:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


book_list = []


def add_book(name, cost):
    # Function to add a new book to the library
    book = Book(name, cost)
    book_list.append(book)


# Example books added to the library
add_book("DSA", 500)
add_book("CG", 400)
add_book("DELD", 300)
add_book("OOP", 700)
add_book("DM", 590)
add_book("DSA", 500)
add_book("DELD", 300)
add_book("OOP", 700)

# Display the original list of books
print("\nOriginal Book List:")
for book in book_list:
    print(book.name, book.cost)


def delete_duplicate(book_list):
    # Function to delete duplicate entries from the book list
    unique_book_list = []
    for book in book_list:
        does_copy_exists = False
        for u_book in unique_book_list:
            if u_book.name == book.name and u_book.cost == book.cost:
                does_copy_exists = True
        if not does_copy_exists:
            unique_book_list.append(book)
    return unique_book_list


# Delete duplicate entries
book_list = delete_duplicate(book_list)

# Display the list after deleting duplicates
print("\na. After Deleting Duplicates:")
for book in book_list:
    print(book.name, book.cost)


def arrange_books(book_list):
    # Function to arrange books in ascending order based on cost using selection sort
    n = len(book_list)
    for j in range(n - 1):
        min_value_index = j
        for i in range(j, n):
            if book_list[min_value_index].cost > book_list[i].cost:
                min_value_index = i
        book_list[j], book_list[min_value_index] = (
            book_list[min_value_index],
            book_list[j],
        )


# Sort books by cost in ascending order
arrange_books(book_list)

# Display the list after sorting by cost
print("\nb. After Sorting by Cost:")
for book in book_list:
    print(book.name, book.cost)


def count_book_filter(cost=500):
    # Function to count the number of books with cost more than a specified threshold
    cnt = 0
    for book in book_list:
        if book.cost >= cost:
            cnt += 1
    return cnt


# Count the number of books with cost more than 500
print("\nc. Number of Books with Cost More Than 500:", count_book_filter())


def separate_book_filter(cost=500):
    # Function to filter books with cost less than a specified threshold into a new list
    less_cost_book = []
    for book in book_list:
        if book.cost < cost:
            less_cost_book.append(book)
    return less_cost_book


# Copy books with cost less than 500 to a new list
less_than_500_books = separate_book_filter()

# Display the list of books with cost less than 500
print("\nd. Books with Cost Less Than 500:")
for book in less_than_500_books:
    print(book.name, book.cost)
