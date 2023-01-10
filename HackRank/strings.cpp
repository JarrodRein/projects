#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,  b, tempa, tempb;
    int num1, num2;

  cin >> a >> b;
  
  num1= a.length();
  num2 = b.length();
  
  cout << num1 << " " << num2<< endl;
  cout << a+b<< endl;
  
  tempa = a;
  tempb = b;
  
  tempa[0]= b[0];
  tempb[0]= a[0];
  
  cout << tempa << " " << tempb << endl;
  
  
  
    return 0;
}