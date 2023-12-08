/*

The ticket booking system of Cinemax theater has to be implemented using C++ program.
There are 10 rows and 7 seats in each row. Doubly circular linked list has to be
maintained to keep track of free seats at rows. Assume some random booking to start
with. Use array to store pointers (Head pointer) to each row. On demand
a) The list of available seats is to be displayed
b) The seats are to be booked
c) The booking can be cancelled.


*/


#include<iostream>
using namespace std;

class node {
public:
    int seat_no;
    char status;
    node *prev, *next;
};

class ticket {
public:
    node *head[10], *last[10];

    // Constructor to initialize head and last pointers
    ticket() {
        for (int i = 0; i < 10; i++) {
            head[i] = NULL;
            last[i] = NULL;
        }
    }

    // Function to create the initial booking system
    void create_bookingsys();

    // Function to display the seat status of each row
    void display();

    // Function to book seats
    void booking();

    // Function to cancel booked seats
    void cancle_booking();
};

void ticket::create_bookingsys() {
    int i, j;
    for (i = 0; i < 10; i++) {
        for (j = 0; j < 7; j++) {
            node *ptr;
            ptr = new node();
            ptr->prev = ptr->next = NULL;
            ptr->seat_no = j + 1;
            ptr->status = 'F';
            if (head[i] == NULL) {
                head[i] = ptr;
                last[i] = ptr;
            } else {
                last[i]->next = ptr;
                ptr->prev = last[i];
                ptr->next = head[i];
                last[i] = ptr;
            }
        }
        head[i]->prev = last[i];
    }
}

void ticket::display() {
    node *temp;
    for (int i = 0; i < 10; i++) {
        temp = head[i];
        cout << "ROW NO" << " " << i + 1 << "->" << "\t";
        do {
            cout << temp->seat_no << "," << temp->status << "\t";
            temp = temp->next;
        } while (temp != head[i]);
        cout << "\n";
    }
}

void ticket::booking() {
    int flag = 0;
    int row, seatno, count = 0;
    node *temp;
    cout << "ENTER THE ROW NO";
    cin >> row;
    cout << "Enter the no of seats";
    cin >> seatno;
    temp = head[row - 1];
    do {
        if (temp->status == 'F') {
            count++;
        } else if (temp->status == 'B') {
            count = 0;
        }
        if (count == seatno) {
            temp = head[row - 1];
            if (temp->status != 'F') {
                while (temp->status != 'F') {
                    temp = temp->next;
                }
                for (int i = 0; i < seatno; i++) {
                    temp->status = 'B';
                    temp = temp->next;
                }
            } else {
                for (int i = 0; i < seatno; i++) {
                    temp->status = 'B';
                    temp = temp->next;
                }
            }
        }
        temp = temp->next;
    } while (temp != head[row - 1]);
}

void ticket::cancle_booking() {
    int row, seatno, loc;
    node *temp;
    cout << "Enter the row from where you want to cancel booking" << endl;
    cin >> row;
    cout << "Enter the location for canceling booking" << endl;
    cin >> loc;
    cout << "Enter the no of seats are to be canceled" << endl;
    cin >> seatno;
    temp = head[row - 1];
    for (int i = 0; i < loc - 1; i++) {
        temp = temp->next;
    }
    for (int i = 0; i < seatno; i++) {
        temp->status = 'F';
        temp = temp->next;
    }
}

int main() {
    int ch;
    ticket c;
    do {
        cout << "ENTER YOUR CHOICE:1.createbookingsy\n2.display\n3.booking\n4.cancelbooking\n5.exit";
        cin >> ch;

        switch (ch) {
            case 1:
                c.create_bookingsys();
                c.display();
                break;
            case 2:
                c.display();
                break;
            case 3:
                c.booking();
                c.display();
                break;
            case 4:
                c.cancle_booking();
                c.display();
                break;
            case 5:
                break;
        }
    } while (ch != 5);

    return 0;
}
