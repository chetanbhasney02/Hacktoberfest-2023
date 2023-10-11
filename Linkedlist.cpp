#include<iostream>
using namespace std;
struct node{ 
    public:
     int data;
     node *next;
};
class SLL{
 node *start;
 public:
 SLL();
 ~SLL();
 void set_start(node*);
 node* get_start();
 void In_Beginnings(int);
 void In_Ends(int);
 node *Search(int);
 void In_Specific(int,int);
 void del_Beginnings();
 void del_Ends();
 void del_Specific(int);
 void Print();
 void operator=(SLL&);
};
void SLL::operator=(SLL &s1)
{
node* ptr2=s1.get_start();
while(ptr2!=NULL)
{
    In_Ends(ptr2->data);
    ptr2=ptr2->next;
}
}
void SLL::set_start(node* t)
{
start=t;
}
node* SLL::get_start() { return start; }
SLL::~SLL()
{
node *ptr;
node *temp;
ptr=start;
while (ptr !=NULL)
{
temp=ptr;
ptr=ptr->next;
delete temp;
}
delete ptr;
//cout<<"Deletion Complete!"<<endl;
}
void SLL::del_Specific(int Value)
{
    node *ptr;
    node *temp;
ptr=start;
if(start==NULL)
{
    cout<<"List Is Empty!"<<endl;
    return;
}
if(start->data==Value)
{
    del_Beginnings();
    return;
}
while(ptr!=NULL)
{
    if(ptr->data==Value)
    {
temp->next=ptr->next;
delete ptr;
return;
    }
temp=ptr;
ptr=ptr->next;
}
cout<<"Invalid Specifications"<<endl;
}
void SLL::Print()
{node* ptr;
ptr=start;
if(start==NULL)
{
    cout<<"List Is Empty"<<endl;
    return;
}
while(ptr!=NULL)
{
cout<<ptr->data<<" ";
   ptr=ptr->next;
}
cout<<endl;
}
void SLL::del_Ends() 
{
    node *ptr;
    ptr =start;
if(start==NULL)
{
    cout<<"List Is Empty"<<endl;
}
    while((ptr->next)->next!=NULL)
    {ptr =ptr->next;}
    delete (ptr->next);
    ptr->next=NULL;
}
void SLL::del_Beginnings() {
    node *ptr;
    ptr =start;
    if(start==NULL)
{
    cout<<"List Is Empty"<<endl;
}
    start = start->next;
    delete ptr;
}
void SLL::In_Specific(int Value,int Data)
{
node *ptr;
ptr=Search(Value);

if(ptr!=NULL)
{
node *new_node;
new_node = new node;
new_node->data = Data;
new_node->next = ptr->next;
ptr->next = new_node;
return;
}
return;

}
node * SLL::Search(int Value)
{
node *ptr;
ptr=start;
while(ptr!=NULL)
{
if(ptr->data==Value)
{
    return ptr;
}
ptr=ptr->next;
}
return NULL;
}
void SLL::In_Ends(int Value){
    if(start==NULL)
    {
        In_Beginnings(Value);
    }
    else{
         node *ptr;
         node *new_node= new node; 
         new_node->data = Value;
         new_node->next = NULL;
         ptr =start;
         while(ptr->next !=NULL)
         {
            ptr = ptr->next;
         }
         
         ptr->next=new_node;
    }
}
void SLL::In_Beginnings(int Value)
{
node *new_node=new node;
new_node->data = Value;
new_node->next = start;
start = new_node;
}
SLL::SLL(){
start=NULL;
 }
class SLL_E:public SLL{
public:
int count_items();
void reverse();
node* middle_node();
bool is_cycle();
int cycle_length();
void sort();
SLL_E operator+(SLL_E &);
SLL_E ADD(SLL_E &);
};
SLL_E SLL_E::ADD(SLL_E &temp)
{
int carry=0;
SLL_E third;
int sum;
node* first=temp.get_start();
node* second=get_start();
while(second!=NULL&&first!=NULL)
{
    sum=(first->data)+(second->data)+carry;
   if(sum>9)
   {
     carry=(sum)/10;
     sum=sum%10;
   }
   else{carry=0;}
   third.In_Beginnings(sum);
   first=first->next;
   second=second->next;
}
while(second!=NULL)
{
    sum=(second->data)+carry;
   if(sum>9)
   {
     carry=(sum)/10;
     sum=sum%10;
   }
   else{carry=0;}
   third.In_Beginnings(sum);
   second=second->next;
}
while(first!=NULL)
{
    sum=(first->data)+carry;
   if(sum>9)
   {
     carry=(sum)/10;
     sum=sum%10;
   }
   else{carry=0;}
   third.In_Beginnings(sum);
   first=first->next;
}
if(carry!=0)
{
   third.In_Beginnings(carry);
}
return third;
}
SLL_E SLL_E::operator+(SLL_E &Temp)
 {
SLL_E Third;
node* first=get_start();
node* sec=Temp.get_start();
while (first != NULL && sec != NULL) {
        if (first->data <= sec->data) {
            Third.In_Ends(first->data);
            first = first->next;
        } else {
            Third.In_Ends(sec->data);
            sec = sec->next;
        }
    }


while (first != NULL) {
        Third.In_Ends(first->data);
        first = first->next;
    }
    
    while (sec != NULL) {
        Third.In_Ends(sec->data);
        sec = sec->next;
    }
return Third;
 }
void SLL_E::sort() {
   int i=count_items();
   node* nxt=NULL;
   node* cur=NULL;
   node* prev=NULL;
   while(i--)
   {
      prev=NULL;
      cur=get_start();
      nxt=cur->next;
      while(nxt!=NULL)
      {
         if(cur->data>nxt->data)
         {
            if(prev==NULL)
            {
               set_start(nxt);
            }
            else{prev->next=nxt;}
            cur->next=nxt->next;
            nxt->next=cur;
            node* temp=cur;
            cur=nxt;
            nxt=temp;
         }
         prev=cur;
         cur=cur->next;
         nxt=nxt->next;
      }

   }
}
int SLL_E::cycle_length(){
   node* fast=(get_start())->next;
   node* slow=get_start();
   int count=0;
   while(fast!=slow&&is_cycle())
   {
      slow=slow->next;
      fast=(fast->next)->next;
      count++;
   }
   return count;
}
bool SLL_E::is_cycle()
{
   node* temp=get_start();
   int count=count_items();
   while(temp)
   {
      if(count==0&&temp!=NULL)
      {
         return true;
      }
      temp=temp->next;
      count--;
   }
   return false;
}
node* SLL_E::middle_node()
{
   node* end=(get_start()->next)->next;
   node* middle=get_start();
   while(end!=NULL)
   {
      middle=middle->next;
      if(end->next!=NULL)
      {end=(end->next)->next;}
      else
         {break;}
   }
   return middle;
} 
void SLL_E::reverse()
{
     node* prev=NULL;
     node* nex_t=get_start();
     node* current=NULL;
     while(nex_t)
     {
        prev=current;
        current=nex_t;
        nex_t=nex_t->next;
        current->next=prev;
     }
     set_start(current);
}
int SLL_E::count_items()
{int count=0;
node *temp=get_start();
while(temp)
{
count++;
temp=temp->next;
}
return count;
}
// Driver Code 
int main() {
    SLL_E list1, list2;
    
    // Insert elements into the first list
    list1.In_Ends(1);
    list1.In_Ends(3);
    list1.In_Ends(5);
    
    // Insert elements into the second list
    list2.In_Ends(2);
    list2.In_Ends(4);
    list2.In_Ends(6);

    // Display the original lists
    cout << "Original List 1: ";
    list1.Print();
    cout << "Original List 2: ";
    list2.Print();
    
    // Concatenate two lists and display the result
    SLL_E concatenatedList = list1 + list2;
    cout << "Concatenated List: ";
    concatenatedList.Print();

    // Reverse the concatenated list and display the result
    concatenatedList.reverse();
    cout << "Reversed Concatenated List: ";
    concatenatedList.Print();

    // Find middle node of the concatenated list and display its data
    node* middle = concatenatedList.middle_node();
    cout << "Middle Node Data: " << middle->data << endl;

    // Check if the concatenated list has a cycle and display the result
    bool hasCycle = concatenatedList.is_cycle();
    if (hasCycle) {
        cout << "The concatenated list has a cycle." << endl;
    } else {
        cout << "The concatenated list does not have a cycle." << endl;
    }

    // Calculate and display the cycle length of the concatenated list
    int cycleLength = concatenatedList.cycle_length();
    cout << "Cycle Length: " << cycleLength << endl;

    // Sort the concatenated list and display the result
    concatenatedList.sort();
    cout << "Sorted Concatenated List: ";
    concatenatedList.Print();

    return 0;
}
