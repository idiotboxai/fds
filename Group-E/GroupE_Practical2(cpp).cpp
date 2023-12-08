/*

A double-ended queue (deque) is a linear list in which additions and deletions may be made at either end. 
Obtain a data representation mapping a deque into a onedimensional array. Write C++ program to simulate deque 
with functions to add and delete elements from either end of the deque

*/
#include<iostream>
using namespace std;

class Deque{
public:
	const static int size = 10;
	int array[size];
	int front=-1,rear=-1;

	bool isFull(){
		if((front == 0 && rear == size-1) || (rear == front - 1)){
			return 1;
		}
		return 0;
	}

	bool isEmpty(){
		if(front == -1 && rear == -1){
			return 1;
		}
		return 0;
	}

	void insertFront(int x){
		if(isFull()){
			cout << "Deque Overflow" << endl;
			return;
		}
		if(front == -1){
			front = 0;
			rear = 0;
		}else if(front == 0){
			front  = size - 1;
		}else{
			front = front - 1; // front--;
		}

		array[front] = x;
		// cout << "Front is: " << front << endl;
	}

	void insertRear(int x){
		if(isFull()){
			cout << "Deque Overflow" << endl;
			return;
		}

		if(rear == -1){
			front = 0;
			rear = 0;
		} else if(rear == size - 1){
			rear = 0;
		}else{
			rear = rear + 1; // rear++; rear += 1;
		}

		array[rear] = x;
		// cout << "Rear is: " << rear << endl;
	}

	void deleteFront(){
		if(isEmpty()){
			cout << "Deque Underflow" << endl;
			return;
		}

		if(front == rear){
			front = -1;
			rear = -1;
		}else if(front == size-1){
			front = 0;
		}else{
			front++;
		}


	}

	void deleteRear(){
		if(isEmpty()){
			cout << "Deque Underflow" << endl;
			return;
		}

		if(front == rear){
			front = -1;
			rear = -1;
		} else if(rear == 0){
			rear = size-1;
		}else{
			rear--;
		}
	}

	void display(){
		if(isEmpty()){
			cout << "Deque Underflow" << endl;
			return;
		}

		cout << "\nDeque contains: ";

		if(front<rear){
			for( int i = front; i <= rear;i++){
				cout << array[i] << " ";
			}
		}else if(front == rear){
				cout << array[front];
		}
		else{
			for( int i = front; i < size;i++){
				cout << array[i] << " ";
			}
			for( int i = 0; i <= rear;i++){
				cout << array[i] << " ";
			}
		}
	}
};

int main(){
	Deque q;
	q.insertFront(10);
	q.insertFront(16);
	q.insertFront(20);
	q.insertFront(13);
	q.insertRear(30);
	q.insertRear(37);
	q.display();
	q.deleteFront();
	q.deleteFront();
	q.deleteRear();
	q.deleteRear();
	q.deleteRear();
	q.deleteRear();
	q.display();
}
