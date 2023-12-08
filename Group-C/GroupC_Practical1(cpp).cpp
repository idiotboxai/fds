/*

Department of Computer Engineering has student's club named 'Pinnacle Club'. Students
of second, third and final year of department can be granted membership on request.
Similarly one may cancel the membership of club. First node is reserved for president of
club and last node is reserved for secretary of club. Write C++ program to maintain club
member‘s information using singly linked list. Store student PRN and Name. Write
functions to:
a) Add and delete the members as well as president or even secretary.
b) Compute total number of members of club
c) Display members
d) Two linked lists exists for two divisions. Concatenate two lists.
  
*/

#include<iostream>
using namespace std;

class Node {
public:
    string name = "";
    string prn = "";
    Node* next = NULL;

    Node(string sname, string sprn) : name(sname), prn(sprn), next(NULL) {}
};

Node* head = NULL;

// Function to add the president to the club
void add_president(string name = "President", string prn = "111") {
    Node* temp = new Node(name, prn);
    if (head == NULL) head = temp;
}

// Function to add the secretary to the end of the club
void add_secretary(string name = "Secretary", string prn = "999") {
    Node* temp = new Node(name, prn);
    
    Node* cur = head;
    while (cur->next != NULL) cur = cur->next;

    cur->next = temp;
}

// Function to add a member to the club
void add_member(string name = "Member", string prn = "555") {
    Node* temp = new Node(name, prn);
    temp->next = head->next;
    head->next = temp;
}

// Function to display the members of the club
void display_list(Node* head) {
    cout << "#########################" << endl;
    Node* cur = head;
    while (cur->next != NULL) {
        cout << cur->name << " " << cur->prn << " ";
        cout << cur->next << endl;
        cur = cur->next;
    }
    cout << cur->name << " " << cur->prn << " " << cur->next << endl;	
    cout << "#########################" << endl;
}

int main() {
    add_president();
    add_secretary();
    add_member("1");
    add_member("2");
    add_member("3");
    display_list(head);
    return 0;
}
