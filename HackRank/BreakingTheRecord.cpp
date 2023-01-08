#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'breakingRecords' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY scores as parameter.
 */

vector<int> breakingRecords(vector<int> scores) {
    
    unsigned long long num1=0, num2=0, num3=0, num4=0, num5=10000000000, num6=0, num7=0;
    vector <int> scored;
    vector<int> scoress;
    int count =0;
    
    
    for(int i =0; i<scores.size(); i++){
        
        if(scores[i]==0 && count ==0){
            num2=scores[i];
                    num1 = scores[i];
                num4=3;
                num6=0;
                scored.push_back(num4);
        scored.push_back(num6);
        return scored;
                
            count ++;
        }
        num1 = scores[i];
        num2 = scores[i+1];
        
        if(num1 > num2 || num2 > num1){
            if(num1 > num3){
                 num3 = num1;
                 num4++;
            scoress.push_back(num1);  
            
               sort(scoress.begin(), scoress.end());
               
               num7= scoress[0];
               
            } else if (num1 > num2 || num2 > num1){
                if (num5 > num1&& num7 > num1 ) {
                
                  //    cout <<"loop1 "<< num1 << " "<< num2 << " "<<num6<< " num5:" << num5<< " num7:" <<num7<< " " << endl;
                      num5 = num1;
                 num6++;
                }
                if(num5 > num2 && num7 > num2){
                     if (num1 != 0 && num2 !=0) {
                //     cout <<"loop2  "<< num1 << " "<< num2 << " "<<num6<< " num5:" << num5<< " num7:"<<num7<< " " << endl;
                      num5 = num2;
                 num6++;
                     }
                //       cout <<"2 "<< num1 << " "<< num2 << " "<<num6<< " " << num5<< " " << endl;
                //       num5 = num2;
                //  num6++;
                     
                }
              }
            
           // cout << "next if 2" << endl; 
        
           //  cout << "next if 1" << endl; 
        } 
     //   cout <<"3 "<< num1 << " "<< num2 << " "<<num6<< " num5:" << num5<< " " << " num7:" <<num7<< " "<< endl;
    }
    
    num4 = num4 -1;
        
    //    cout << num4 << " four " << num5 << endl;
        scored.push_back(num4);
        scored.push_back(num6);
        return scored;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string scores_temp_temp;
    getline(cin, scores_temp_temp);

    vector<string> scores_temp = split(rtrim(scores_temp_temp));

    vector<int> scores(n);

    for (int i = 0; i < n; i++) {
        int scores_item = stoi(scores_temp[i]);

        scores[i] = scores_item;
    }

    vector<int> result = breakingRecords(scores);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << " ";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
