#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    stringstream ss(str);
char ch;
int a, b, c;
//ss >> a >> ch >> b >> ch >> c;  // a = 23, b = 4, c = 56   
  //  cout << a << b << c << endl;  
    vector <int> vec;
    int num1 =0;
    for(int i =0; i< str.length(); i++){
       // int num = (int)str[i];
       
    ss >> a >> ch;
    vec.push_back(a);
    
    
    
    
    int num = vec.size();
 //  cout << num << endl;
   if( a == num1){
       vec.pop_back();
       return vec;
   }
   
    num1 = a;
       // vec.push_back(a);
    }
    
    
    
    return vec;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}