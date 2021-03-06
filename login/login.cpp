
#include <iostream>
using namespace std;
string usrUsr;
string usr = "farm";
string usrPas;
string pas = "tractor";
int times;
int incorrect = 0;
int main() {
        do {
        cout << "Enter username" << endl;
        cin >> usrUsr;
        cout << "Enter password" << endl;
        cin >> usrPas;
        if (usrUsr == usr && usrPas != pas) {
                cout << "Incorrect password" << endl;
                incorrect++;
                times = 3 - incorrect;
                if (times == 1) {
                cout << times << " attempt left" << endl;
                } else {
                cout << times << " attempts left" << endl;
                }
        } else if (usrUsr != usr && usrPas == pas) {
                cout << "Incorrect username" << endl;
                incorrect++;
                times = 3 - incorrect;
                if (times == 1) {
                cout << times << " attempt left" << endl;
                } else {
                cout << times << " attempts left" << endl;
                }

        } else if (usrUsr != usr && usrPas != pas) {
                cout << "Both username and password are incorrect" << endl;
                incorrect++;
                times = 3 - incorrect;
                if (times == 1) {
                cout << times << " attempt left" << endl;
                } else {
                cout << times << " attempts left" << endl;
                }
        }
        else {
                cout << "Correct. You have gained access" << endl;
                return 0;
        }

        } while (incorrect < 3);

        if (incorrect >= 3) {
                cout << "Too many failed login attempts. Data wiped" << endl;
        }

}
