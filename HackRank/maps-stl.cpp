#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    map<string, int> map;
    int num1, num2, num3;
    string word;
    
    cin >> num1;
    
    for(int i=0; i<num1; i++){
        cin >> num2; 
        
        if(num2 == 2 || num2 ==3){
             cin >> word;
        } else{
            cin >> word >> num3;
        }
        
        
        cout << num2 <<" "<<  word  <<" "<< num3 << endl;
        
        num2=0;
        num3 =0;
        word ="";
    }
    
    map.insert(make_pair("hello", 9));
    
    for(auto it = map.cbegin(); it != map.cend(); ++it)
{
    std::cout << it->first << " " << it->second  << "\n";
}

    
     
    return 0;
}



