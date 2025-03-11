#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

/*
 https://web.stanford.edu/class/archive/cs/cs103/cs103.1254/lectures/25/Condensed%20Lecture%20Slides.pdf
 */

vector<int> longestIncreasedSubsequence(int * array, int len){
    vector<vector<pair<int, int> > > piles;
    for(int i = 0; i < len ; i++){
        int item = array[i];
        bool found = false;
        for (vector<pair<int, int>> & vt : piles) {
            if (item < vt[vt.size() - 1].first) {
                vt.push_back(pair<int, int>(item, i));
                found = true;
                break;
            }
        }
        if (found == false) {
            vector<pair<int, int>> tmp;
            tmp.push_back(pair<int, int>(item, i));
            piles.push_back(tmp);
        }
        
    }
    
    for (int j = 0; j < piles.size(); j++) {
        for (int i = 0; i < piles[j].size(); i++) {
            cout << piles[j][i].first << " ";
        }
        cout << "\n";
    }
    cout << "--------\n";
    
    vector<int> result;
    vector<pair<int, int>> store;
    for (int i = int(piles.size()) - 1; i >= 0; i--) {
        vector<pair<int, int>> tmp = piles[i];
        if (result.empty()) {
            result.push_back(tmp[tmp.size() - 1].first);
            store.push_back(tmp[tmp.size() - 1]);
        } else {
            int item = result[result.size() - 1];
            int index = store[result.size() - 1].second;
            int id = 0;
            if (tmp.size() > 1) {
                for (int j = 0; j < tmp.size(); j++) {
                    if (tmp[j].first < item && tmp[j].second < index) {
                        id = j;
                    }
                }
            }
            
            result.push_back(tmp[id].first);
            store.push_back(tmp[id]);
        }
    }
    return result;
}

int main() {
    int array[] = { 4, 3, 11, 9, 7, 13, 5, 6, 1, 12, 2, 8, 0, 10};
    
    vector<int> result = longestIncreasedSubsequence(array, sizeof(array) / sizeof(int));
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}

