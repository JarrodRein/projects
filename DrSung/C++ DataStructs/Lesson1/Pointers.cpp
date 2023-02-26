#include <iostream>

using namespace std;
// prototype

int add(int, int);

int main()
{
    int n = add(10, 20);
    cout << n << endl;
}

int add(int a, int b)
{
    int r = a + b;
    return r;
}