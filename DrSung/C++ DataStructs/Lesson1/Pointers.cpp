#include <iostream>

using namespace std;

extern int add(int, int);

int main()
{
    int n = add(10, 20);
    cout << n << endl;
}

