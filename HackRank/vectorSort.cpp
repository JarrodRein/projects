#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int num1, num2;
    cin  >> num1;
    vector<int> vec;
    
    for(int i=0; i<num1; i++){
        cin >> num2;
        vec.push_back(num2);
}
    sort(vec.begin(), vec.end());
    
    for(int j=0; j<vec.size(); j++){
        cout<< vec[j] <<' ';
    }
    return 0;
}
