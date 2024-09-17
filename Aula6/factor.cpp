#include <bits/stdc++.h>
using namespace std;
 
void primeFactors(int n) 
{ 
    int exit = 0;
    while (n % 2 == 0) 
    { 
        exit += 2;
        n = n/2; 
    } 
 
    for (int i = 3; i <= std::sqrt(n); i = i + 2) 
    { 
        while (n % i == 0) 
        { 
            exit += i;
            n = n/i; 
        } 
    } 
 
    if (n > 2) 
        exit += n; 
    
    cout << exit << endl;
}

int main() {
    int number;

    while (std::cin >> number) {
        primeFactors(number);
    }
    
    return 0;
}

