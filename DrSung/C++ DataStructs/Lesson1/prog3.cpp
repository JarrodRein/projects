
#include <iostream>
#include <cassert>

using namespace std;




void pointer_arithmetic(){
    cout << "pointer arithmetic" << endl;

    int n = 15;

    int* p =&n;

    assert(n == *p);

    cout << *p << " " << n << endl;

    n = 20;

    assert(n == *p);
    *p = 30;
    assert(n == *p);
    
    
}