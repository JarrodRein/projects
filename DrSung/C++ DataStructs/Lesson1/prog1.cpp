#include <iostream>
using namespace std;

int add(int a, int b)
{
    int r = a + b;
    return r;
}

void pointer_concept(){
    cout << "the concept of the pointers" << endl;
    int n =5;
    double d = 3.14;
    char c ='B';
    bool b = false;

    n=20;
    //how to get the address of a variable
    int *p1 = &n;

    double *p2 = &d;

    char* p3 = &c;

    bool* p4 = &b;

    int**  p5;
    p5 = &p1;
        cout << "referencing" << endl;

    cout << p5 << endl;

     cout << "referencing" << endl;

    cout << p1 << endl;

     cout << "dereferencing" << endl;

    cout << &p1 << endl;
}