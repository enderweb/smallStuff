#include <iostream>
using namespace std;
int main()
{
	int cents = 0;
	cout << "How many cents do you have? " << endl;
	cin >> cents;

	int dollarAmount = cents/100;
	if (dollarAmount > 1  || dollarAmount < 1) {
	cout << "You have " << dollarAmount << " dollars\n"; 
	} else {
	cout << "You have " << dollarAmount << " dollar\n";
	}
}
