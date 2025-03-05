#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <sstream>
using namespace std;

const vector<string> kToPrint = {
  "#include <iostream>",
  "#include <string>",
  "#include <vector>",
  "#include <iomanip>",
  "#include <sstream>",
  "using namespace std;",
  "",
  "const vector<string> kToPrint = {",
  "@",
  "};",
  "",
  "string mySource() {",
  "  ostringstream result;",
  "  for (string line: kToPrint) {",
  "    if (line == \"@\") {",
  "      for (string line: kToPrint) {",
  "        result << \"  \" << quoted(line) << \",\" << endl;",
  "      }",
  "    } else {",
  "      result << line << endl;",
  "    }",
  "  }",
  "  return result.str();",
  "}",
  "",
  "int main() {",
  "  if (mySource().length() % 2 == 0) cout << \"I am an even-length program\" << endl;",
  "  else cout << \"I am an odd-length program\" << endl;",
  "}",
};

string mySource() {
  ostringstream result;
  for (string line: kToPrint) {
    if (line == "@") {
      for (string line: kToPrint) {
        result << "  " << quoted(line) << "," << endl;
      }
    } else {
      result << line << endl;
    }
  }
  return result.str();
}

int main() {
  if (mySource().length() % 2 == 0) cout << "I am an even-length program" << endl;
  else cout << "I am an odd-length program" << endl;
}

