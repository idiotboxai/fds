"""Write a Python program for department library which has N books, write functions for
following:
a) Delete the duplicate entries
b) Display books in ascending order based on cost of books
c) Count number of books with cost more than 500.
d) Copy books in a new list which has cost less than 500.
"""

print(__doc__)


class Book:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


book_list = []


def add_book(name, cost):
    book = Book(name, cost)
    book_list.append(book)


add_book("DSA", 500)
add_book("CG", 400)
add_book("DELD", 300)
add_book("OOP", 700)
add_book("DM", 590)
add_book("DSA", 500)
add_book("DELD", 300)
add_book("OOP", 700)

for book in book_list:
    print(book.name, book.cost)


def delete_duplicate(book_list):
    does_copy_exists = False
    unique_book_list = []
    for book in book_list:
        for u_book in unique_book_list:
            if u_book.name == book.name and u_book.cost == book.cost:
                does_copy_exists = True
        if not does_copy_exists:
            unique_book_list.append(book)
    return unique_book_list


book_list = delete_duplicate(book_list)

print("\na.")
for book in book_list:
    print(book.name, book.cost)


def arrange_books(book_list):
    for j in range(len(book_list) - 1):
        min_value_index = j
        for i in range(j, len(book_list)):
            if book_list[min_value_index].cost > book_list[i].cost:
                min_value_index = i
        book_list[j], book_list[min_value_index] = (
            book_list[min_value_index],
            book_list[j],
        )


arrange_books(book_list)
print("\nb.")
for book in book_list:
    print(book.name, book.cost)


def count_book_filter(cost=500):
    cnt = 0
    for book in book_list:
        if book.cost >= cost:
            cnt += 1  # cnt = cnt+1
    return cnt


print("\nc.", count_book_filter())


def seperate_book_filter(cost=500):
    less_cost_book = []
    for book in book_list:
        if book.cost < cost:
            less_cost_book.append(book)
    return less_cost_book


print("\nd.")
for book in seperate_book_filter():
    print(book.name, book.cost)
