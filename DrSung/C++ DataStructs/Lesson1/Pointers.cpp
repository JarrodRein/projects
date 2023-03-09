#include <iostream>

using namespace std;

extern int add(int, int);
extern int mul(int, int);

int main()
{
    int n = add(10, 20);
    cout << n << endl;
    n = mul(10, 20);
    cout << n << endl;
}

