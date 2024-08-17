#include <iostream>
#include <string>
#include <algorithm> // for size()
#include <numeric> // for gcd()

using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        return (str1 + str2 == str2 + str1) ?
        str1.substr(0, gcd(size(str1), size(str2))) : "";
    }
};

int main() {
    Solution solution;
    string str1 = "ABABAB";
    string str2 = "ABAB";
    cout << "GCD of Strings: " << solution.gcdOfStrings(str1, str2) << endl;
    return 0;
}
