
#include <iostream>
#include <cassert>

using namespace std;

int mul(int a, int b){
    int r = a *b;
    return r;
};


void deref_demo(){
    cout << "dereference demo" << endl;

    int n = 15;

    int* p =&n;

    assert(n == *p);

    cout << *p << " " << n << endl;

    n = 20;

    assert(n == *p);
    *p = 30;
    assert(n == *p);

}