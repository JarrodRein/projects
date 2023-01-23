#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    int num1, num2, num3, num4, num5, num6;
    char word1, word2, word3, word4;
    char word5, word6, word7, word8;
    string words;
    
    word1=s[8];
    word2=s[9];
    
    
    word3 = s[0];
    word4 = s[1];
    
    word5 = s[3];
    word6 = s[4];
    word7 = s[6];
    word8 = s[7];
    
    
    num1 = (int)word3;
     num2 = (int)word4;
      num3 = (int)word5;
       num4 = (int)word6;
        num5 = (int)word7;
         num6 = (int)word8;
              

    if (word1 == 'A'){
        
        if(word3 == '1' && word4 == '2'){
           
    words.push_back('0');
     words.push_back('0');
     words.push_back(':');
     words.push_back(word5);
     words.push_back(word6);
     words.push_back(':');
     words.push_back(word7);
     words.push_back(word8);
       return words;
        }else {
        words.push_back(word3);
     words.push_back(word4);
     words.push_back(':');
     words.push_back(word5);
     words.push_back(word6);
     words.push_back(':');
     words.push_back(word7);
     words.push_back(word8);
     return words;
        }
    }else {
         
        
        if (word3 == '1'&& word4=='2') {
        words.push_back(word3);
     words.push_back(word4);
     words.push_back(':');
     words.push_back(word5);
     words.push_back(word6);
     words.push_back(':');
     words.push_back(word7);
     words.push_back(word8);
     return words;
        }else{
            num1++;
        num2 = num2 +2;
        word3 = static_cast<char>(num1);
        word4 = static_cast<char>(num2);
     words.push_back(word3);
     words.push_back(word4);
     words.push_back(':');
     words.push_back(word5);
     words.push_back(word6);
     words.push_back(':');
     words.push_back(word7);
     words.push_back(word8);
     
         
        return words;
        }
    }
    cout <<word1 << word2 << endl;
    
    return 0;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
