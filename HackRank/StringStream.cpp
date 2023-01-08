#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    vector <int> vec;
    
    int num =0;
    for(int i =0; i< str.length(); i++){
        
       // int num = (int)str[i];
       if(str[i]==',' || str[i] ==' '){
           i++;
       }
        
        vec.push_back(num);
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