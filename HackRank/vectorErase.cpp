#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    int long num1, num2, num3, num4, num5;
    cin >> num1;
    vector <int> vec;
    for(int i=0; i< num1; i++){
        cin >> num2;
        vec.push_back(num2);
        
        
    }  
    
    cin >> num3;
    
    vec.erase(vec.begin()+num3-1);
    
    cin >> num4 >> num5;
    
    num4 -=1;
    num5 -=1;
    vec.erase(vec.begin()+num4, vec.begin()+num5);
    
    int long num7 = vec.size();
    cout << num7 << endl;
    
    for(int j=0; j<num7; j++){
            cout << vec[j] << " ";

    }
    return 0;
}
