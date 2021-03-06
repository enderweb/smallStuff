
#include <iostream>
using namespace std;
int main() {
int convert, intCel, intFah, finCel, finFah = 0; 
cout << "Do you want to convert Celsius to Fahrenheit or Fahrenheit to Celsius? Type (1) to convert to Fahrenheit and (2) to convert to Celsius" << endl;
cin >> convert;
switch (convert) 
	case 1:
{
	cout << "What tempature Celsius do you want to convert?" << endl;
	cin >> intCel;
	finFah = intCel * 9/5 + 32;
	cout << "Your tempature is " << finFah << "°F" << endl;
	break;
	case 2:

	cout << "What tempature Fahrenheit do you want to convert?" << endl;
	cin >> intFah;
	finCel = (intFah - 32) * 5/9;
	cout << "Your tempature is " << finCel << "°C" << endl;
	break;

	default: 
	cout << "There has been an error. Please read the top bit before putting in a number because that is probably the thing that went wrong" << endl;
}
}
