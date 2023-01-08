#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//seperate function

//seperate method
string sM(string line){
    
    string word = line.substr(4);
    
    cout << word << endl;
    return word;
}

//seperate class
string sC(string line){
    
     string word = line.substr(4);
    
    cout << word << endl;
    
    return word;
}
//seperate variable
string sV(string line){
    
   string word = line.substr(4);
   int temp = 0;
   string firstH, secondH = " ";
    int j=0;
     char c;
     while (j<=word.length())
    {
        c=word[j];
      
      
        if(isupper(c)){
            c = tolower(c);
            temp = j;
            
           word[j] = c;
           j +=1;
        }
       
                   j++;

    }
    
    //word[temp-1] += ' ';
    cout << word << endl;
    return word;
}

//combine functions
//combine method
string cM(string line){
    
    string word = line.substr(4);
    
 
    cout << word << endl;
    return word;
}
//combine class
string cC(string line){
    
   string word = line.substr(4);
    cout << word << endl;
    return word;
}
//combine variable
string cV(string line){
    
    string word = line.substr(4);
    cout << word << endl;
    return word;
}




int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string line;
    string res ="";
    
    
    
    //cin >> line;
    //cout << line ;
    int i =0;
    //cout << line[i+2] << endl;
    
    while (getline(cin, line)) {
    
    
   
        if(line[i]=='S'){
           if(line[i+2]=='M'){
           res = sM(line);
        } else if ( line[i+2]=='C'){
            res = sC(line);
        }   else if ( line[i+2]=='V'){
            res = sV(line);
        }   
        } //if 
        else if ( line[i]=='C'){
            if(line[i+2]=='M'){
           res = cM(line);
        } else if ( line[i+2]=='C'){
          res = cC(line);
        }   else if ( line[i+2]=='V'){
           res = cV(line);
        } 
        } 
    }
    
    return 0;
}
