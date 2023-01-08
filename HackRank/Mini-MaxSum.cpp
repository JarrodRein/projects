#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

void miniMaxSum(vector<int> arr) {
    
   long int num1 =0, num2=0, num3=0, num4=0, num5=0, num6=0;
  long  int num7 =0, num8=0, num9=0, num10=0, num11=0, num12=0, num13=0;
    
    
         sort(arr.begin(), arr.end());
         
         num1 = arr[0];
         num2=arr[1];
          num3 = arr[2];
         num4=arr[3];
          num5 = arr[4];
          
          num7 = num1 + num2 + num3 +num4;
             num8 = num1 + num2 + num3 +num5;
                num9 = num1 + num2 + num5 +num4;
                   num10 = num1 + num5 + num3 +num4;
                      num11 = num5 + num2 + num3 +num4;
                     
                 //     cout << num7 << num8 << num9 << num10 << num11 << endl;
          vector<long int> arr1;      
          
          arr1.push_back(num7);
                    arr1.push_back(num8);
          arr1.push_back(num9);
                    arr1.push_back(num10);
          arr1.push_back(num11);


         sort(arr1.begin(), arr1.end());
         
         num12 = arr1[0];
         num13 = arr1[4];

     
         
         cout<<num12 << " "<< num13 << endl;
     
    
    
    
    

}

int main()
{

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(5);

    for (int i = 0; i < 5; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    miniMaxSum(arr);

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
