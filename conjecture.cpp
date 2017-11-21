//Calculates different paths to 2 of a conjecture I devised (Use python version as it supports infinite precision...)
#include <iostream>
#include <cmath>
#include <unistd.h>	
#include <cmath>

using namespace std;

bool isNumPrime(long num);

int main()
{
	bool status = false;
	bool firstRun = true;
	long num;
	long  totalCounter = 0, touchedPrimes = 0, touchedComposites = 0; 
	cout << "Enter number: ";
	cin >> num;
	long numCheck = num;
	do
	{
		cout << num;
		if(isNumPrime(num))
		{
			cout << " (prime)" << endl;
			num = (num*num)-1;
			touchedPrimes++;
		} else
		{
			cout << " (composite) " << endl;
			if(num % 2 == 0)
			{
				num/=2;
			} else 
			{
				num++;
			}
			touchedComposites++;
		}
		if(num == 2)
			status = true;
		if(numCheck == num && firstRun == false)
			status = true;
		usleep(50000);
		totalCounter++;
		firstRun = false;
	} while(status == false);
	cout << 2 << " (prime)" << endl;
	cout << "Took " << totalCounter << " steps" << "| Touched " << touchedPrimes << " primes" << " | Touched " << touchedComposites << " composites" << endl;
}

bool isNumPrime(long num) 
{
    if (num%2 == 0 && num != 2) 
    {
        return false;
    }

    for (long i = 3; i <= sqrt(num); i = i+2) 
    {
        if (num%i == 0) 
        {
            return false;
        }
    }
    return true;
}