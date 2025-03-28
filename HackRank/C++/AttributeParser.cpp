#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <map>
#include <stack>
#include <sstream>
using namespace std;


int main() {
  
    int n, q;
    cin >> n >> q;
    cin.ignore();

    map<string, string> attrMap;
    string line, tagPath = "";

    for (int i = 0; i < n; ++i) {
        getline(cin, line);

        // Remove angle brackets
        if (line[1] == '/') {
            // Closing tag
            int pos = tagPath.rfind('.');
            if (pos != string::npos)
                tagPath = tagPath.substr(0, pos);
            else
                tagPath = "";
        } else {
            // Opening tag
            stringstream ss(line);
            string temp, tagName;
            ss >> temp; // '<tag'
            tagName = temp.substr(1);

            if (tagPath.empty())
                tagPath = tagName;
            else
                tagPath += "." + tagName;

            string attrName, eq, attrValue;
            while (ss >> attrName >> eq >> attrValue) {
                // Remove quotes from value
                attrValue = attrValue.substr(1, attrValue.length() - 2);
                attrMap[tagPath + "~" + attrName] = attrValue;
            }
        }
    }

    for (int i = 0; i < q; ++i) {
        string query;
        getline(cin, query);
        if (attrMap.find(query) != attrMap.end()) {
            cout << attrMap[query] << endl;
        } else {
            cout << "Not Found!" << endl;
        }
    }

    return 0;
}

