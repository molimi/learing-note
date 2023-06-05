#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    string sentence;
    getline(cin, sentence);

    vector<string> words;
    string delimiter = " ";
    size_t pos = 0;
    while ((pos = sentence.find(delimiter)) != string::npos) {
        string word = sentence.substr(0, pos);
        transform(word.begin(), word.end(), word.begin(), ::tolower);
        words.push_back(word);
        sentence.erase(0, pos + delimiter.length());
    }
    transform(sentence.begin(), sentence.end(), sentence.begin(), ::tolower);
    words.push_back(sentence);
    int len = words.size();
    for (int i = 0; i < len - 1; i++) {
        if (words[i] == words[i + 1]) {
            words.erase(words.begin() + i + 1);
            i--;
            len--;
        }
    }

    for (int i = 0; i<words.size(); ++i) {
            cout << words[i] << " ";
    }
    cout << endl;

    return 0;
}