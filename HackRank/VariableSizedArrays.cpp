#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    int num1, num2, num3, num4, num5, num6, count = 0;
    string input;
    char num1c, num2c;
    vector <int> vec;
    vector <vector<int>> mainvec;
    
    cin >> num1 >> num2;
           //  cout << num1 << "input"<< num2<<  endl;

    
  for(int i =0; i< num1; i++){
      cin >> num3;
      cout << num3 << " num3 " << endl;
      
      for(int j =0; j< num3; j++){
      cin >> num4;
      
      vec.push_back(num4);
  }
  mainvec.push_back(vec);
  }
      
       for(int i =0; i< num2; i++){
      cin >> num5;
      cout << num5 << " num5 "<< endl;
      
      
      
  }
   for(int i =0; i< num2; i++){
      cin >> num6;
      cout << num6 << " num6 " << endl;
      
     
      
  }
  
  
//   for(int j =0; j< vec.size(); j++){
//     //  cin >> num3;
      
//       cout << vec.at(j);
//   }


 for (int i = 0; i < mainvec.size(); i++) {
        for (int j = 0; j < mainvec[i].size(); j++)
          cout << mainvec[i][j] << " ";
           cout << endl;
 }
      
    return 0;
}