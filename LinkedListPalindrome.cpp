// I have figured out two approaches
// for checking if linked list is palindrome or not







// First Approach: Extracting the Linked List Node's data into array
// and check if palindrome on array

// Approach 1

// #include <iostream>
// #include <vector>

// using namespace std;

// class Node
// {
// public:
//     int data;
//     Node *next;

//     Node(int data)
//     {
//         this->data = data;
//         this->next = NULL;
//     }
// };

// bool checkPalindrome(Node *head)
// {
//     vector<int> arr;

//     Node *ptr = head;

//     while (ptr != NULL)
//     {
//         arr.push_back(ptr->data);
//         ptr = ptr->next;
//     }

//     int k = 0;
//     while (k < arr.size())
//     {
//         cout << arr[k] << " ";
//         k++;
//     }

//     int i = 0;
//     int j = arr.size() - 1;

//     while (i <= j)
//     {
//         if (arr[i] == arr[j])
//         {
//             i++;
//             j--;
//         }
//         else
//         {
//             cout << "Not Palindrome" << endl;
//             return false;
//         }
//     }
//     cout<<"Palindrome"<<endl;
//     return true;
// }

// int main()
// {
//     Node *newNode1 = new Node(1);
//     Node *newNode2 = new Node(2);
//     Node *newNode3 = new Node(1);

//     Node *head = newNode1;
//     newNode1->next = newNode2;
//     newNode2->next = newNode3;
//     newNode3->next = NULL;

//     checkPalindrome(head);
// }

















// Second Approach: Reversing the second half and pointing one pointer to it
// and checking if two element the actual first node of the linked list
// and the head of the reversed list is equal until the mid.

#include <iostream>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};
Node* reverseLinkedList(Node* head) {
    // Code to reverse the linked list
    Node* prev = nullptr;
    Node* current = head;
    Node* nextNode = nullptr;

    while (current != nullptr) {
        nextNode = current->next;
        current->next = prev;
        prev = current;
        current = nextNode;
    }

    return prev;
}

bool checkPalindrome(Node* head) {
    if (head == nullptr || head->next == nullptr) {
        cout << "Palindrome" << endl;
        return true;
    }

    // Calculate the length of the linked list
    int count = 0;
    Node* ptr1 = head;
    while (ptr1 != nullptr) {
        count++;
        ptr1 = ptr1->next;
    }

    // Reset ptr1 to the head
    ptr1 = head;

    // Move ptr2 to the middle of the linked list
    Node* ptr2 = head;
    Node* temp = head;
    int i = 1;
    while (i <= count / 2) {
        temp = temp->next;
        i++;
    }

    // Reverse the second half
    Node* second_half = reverseLinkedList(temp);

    // Compare the first and second halves
    int k = 0;
    while (k < count / 2) {
        if (ptr1->data != second_half->data) {
            cout << "Not Palindrome" << endl;
            return false;
        }
        ptr1 = ptr1->next;
        second_half = second_half->next;
        k++;
    }
    cout << "Palindrome" << endl;
    return true;
}
int main()
{
    Node *newNode1 = new Node(5);
    Node *newNode2 = new Node(2);
    Node *newNode3 = new Node(1);
    Node *newNode4 = new Node(2);
    Node *newNode5 = new Node(3);

    Node *head = newNode1;
    newNode1->next = newNode2;
    newNode2->next = newNode3;
    newNode3->next = newNode4;
    newNode4->next = newNode5;
    newNode5->next = NULL;

    checkPalindrome(head);

    while (head != nullptr)
    {
        Node *temp = head;
        head = head->next;
        delete temp;
    }
}