#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

const vector<string> kToPrint = {
  "#include <iostream>",
  "#include <string>",
  "#include <vector>",
  "#include <iomanip>",
  "using namespace std;",
  "",
  "const vector<string> kToPrint = {",
  "@",
  "};",
  "",
  "void printProgramInQuotes() {",
  "  for (string line: kToPrint) {",
  "    cout << \"  \" << quoted(line) << \",\" << endl;",
  "  }",
  "}",
  "",
  "int main() {",
  "  for (string line: kToPrint) {",
  "    if (line == \"@\") {",
  "      printProgramInQuotes();",
  "    } else {",
  "      cout << line << endl;",
  "    }",
  "  }",
  "}",
};

void printProgramInQuotes() {
  for (string line: kToPrint) {
    cout << "  " << quoted(line) << "," << endl;
  }
}

int main() {
  for (string line: kToPrint) {
    if (line == "@") {
      printProgramInQuotes();
    } else {
      cout << line << endl;
    }
  }
}
