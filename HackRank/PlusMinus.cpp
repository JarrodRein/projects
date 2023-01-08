#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

void plusMinus(vector<int> arr) {

double num1, num2=0, num3=0, num4=0, num5=0, num6=0, num7=0, num8=0;

//num1=arr[0];


for(int i =0; i < arr.size(); i++){
    
    num1=arr[i];
    if(num1 == 0){
        
        num2++;
    } else if (num1 >0) {
    num3++;
    }else if (num1<0) {
    num4++;
    }
    
    
    
}

//cout<< num2 <<endl;
//cout<< num3 <<endl;
//cout<< num4 <<endl;


num8 = num2+num3+num4;

num5 = num2/num8;
num6 = num3/num8;
num7 = num4/num8;


cout<< num6 <<endl;
cout<< num7 <<endl;
cout<< num5 <<endl;



}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    plusMinus(arr);

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
