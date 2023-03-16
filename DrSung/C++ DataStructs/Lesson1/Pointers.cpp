#include <iostream>

using namespace std;

extern int add(int, int);
extern int mul(int, int);
extern void pointer_concept();
extern void deref_demo();
extern void pointer_arithmetic();

int main()
{
//     int n = add(10, 20);
//     cout << n << endl;
//     n = mul(10, 20);
//     cout << n << endl;

pointer_concept();
deref_demo();
pointer_arithmetic();
}

