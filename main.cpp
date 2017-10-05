#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

struct LL{
  int value;
  LL *next;
}*head;


void insrt(int pos, int val){
  
  LL *n1 = new LL;
  n1->value = val;
  n1->next = NULL;
  
  if(pos == 0){
    
    if(head == NULL){
      head = n1;
      head->next = NULL;
    }
    else{
      LL *p;
      p = head;
      p->next = head->next;
      head = n1;
      head->next = p;
    }
    
  }
  
  else if(pos == -1){
    LL *p = head;
    while(p->next != NULL){
      p = p->next;
    }
    p->next = n1;
    n1->next = NULL;
  }
  
  else{
    int ii = 0;
    LL *p = head;
    while(ii+1 < pos){
      
      ii++;
      p = p->next;
    }
    
    n1->next = p->next;
    p->next = n1;
    
  }
  
  
}

void dlt(int pos){
  
  if(pos == 0){
    LL *p = head;
    head = head->next;
    delete(p);
  }
  else if(pos == -1){
    LL *p = head;
    while(p->next->next != NULL){
      p = p->next;
    }
    LL *dd = p->next;
    p->next = NULL;
    delete(dd);
  }
  else{
    int ii = 0;
    LL *p = head;
    while(ii+1 < pos){
      
      ii++;
      p = p->next;
    }
    LL *dd = p->next;
    p->next = dd->next;
    delete(dd);
  }
  
}

void display(){
  
  LL *p = head;
  cout<<"\nList:\n";
  while(p != NULL){
    
    cout<<p->value<<" ";
    p = p->next;
  }
  cout<<"\n\n";
}

int sizee(){
  
  LL *p = head; int cc=0;
  while(p != NULL){
    cc++;
    p = p->next;
  }
  return cc;
  
}

void isempty(){
  
  if(sizee()==0)cout<<"List empty\n";
  else cout<<"Length: "<<sizee()<<"\n";
}

int search(int val){
  
  LL *p = head;int cc = 0;
  while(p != NULL){
    if(p->value == val){
      
      return cc;
    }
    p = p->next;
    cc++;
  }
  return -1;
}

void rev(){
  
  LL *p = head;
  
  LL *tmp = new LL;
  tmp->value = p->value;
  tmp->next = NULL;
  p = p->next;
  
  while(p != NULL){
    
    LL *j = new LL;
    j->value = p->value;
    j->next = tmp;
    
    tmp = j;

    p = p->next;
  
  }
  
  head = tmp;
  display();
}


int main(){
  
  int option,val,in;
  head = NULL;
  
  while(1){
    
    printf("Enter you option:\n");
    printf("1 - insert\n2 - delete\n3 - search\n4 - size\n5 - is empty?\n6 - display\n7 - reverse\n8 - exit\n");
  
    cin>>option;
  
    if(option == 1){
    
      cout<<"Enter value:\n";
      cin>>val;
      cout<<"Press 1 to insert at begin, press 2 to insert at the end, press 3 to insert in any other position\n";
      cin>>in;
      
      if(in == 1)insrt(0,val);
      else if(in == 2)insrt(-1,val);
      else{
        cout<<"Enter the position where you want to insert the new node:\n";
        cin>>in;
        insrt(in,val);
      }
    }
    
    else if(option == 2){
    
      cout<<"Press 1 to delete at begin, press 2 to delete at the end, press 3 to delete in any other position\n";
      cin>>in;
      
      if(in == 1)dlt(0);
      else if(in == 2)dlt(-1);
      else{
        cout<<"Enter the position where you want to delete a node:\n";
        cin>>in;
        dlt(in);
      }
    }
    
    else if(option == 3){
      cout<<"Enter value to search:\n";
      cin >> in;
      int rr = search(in);
      if(rr == -1)cout<<"Not found\n";
      else cout<<"Found at position "<<rr<<"\n";
    }
    
    else if(option == 4){
      cout<<"Size of the list: "<<sizee()<<"\n";
    }
    
    else if(option == 5)isempty();
    else if(option == 6)display();
    else if(option == 7)rev();
    else{
      cout<<"Exiting\n";
      break;
    }
  
  }
}