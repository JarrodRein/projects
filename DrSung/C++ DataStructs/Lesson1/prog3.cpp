
#include <iostream>
#include <cassert>

using namespace std;




void pointer_arithmetic(){
    cout << "pointer arithmetic" << endl;

    // int n = 15;

    // int* p =&n;

    // assert(n == *p);

    // cout << *p << " " << n << endl;

    // n = 20;

    // assert(n == *p);
    // *p = 30;
    // assert(n == *p);
    
    int a[5]= {0, 1, 2, 3, 4};

    //the name of the array == the address of the first element
    assert(a ==&a[0]);
    
    int* p1 = a;
    int* p2 = &a[0];
    assert(p1 ==p2);

    p1 += 1;
    assert(p1 ==&a[1]);

      p1++;
    assert(p1 ==&a[2]);

    for(int i=0; i<5; i++){
        assert(*p2 ==a[i]);
        ++p2;
        
    }
    

}