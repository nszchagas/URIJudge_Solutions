#include <stdio.h>
#include <stdlib.h>

int max_prime = 0;
int *prime_numbers;

#define max(a, b) ((a > b) ? a : b)
#define min(a, b) ((a > b) ? b : a)
#define abs(x) ((x < 0) ? -x : x);

int euclidian_gcd(int x, int y)
{
    x = abs(x);
    y = abs(y);

    if (x == y)
        return x;
    if (x == 1 || y == 1)
        return 1;

    int dividend, divisor, quotient, remainder;
    divisor = min(x, y);
    dividend = max(x, y);
    int gcd = divisor;

    if (dividend % divisor == 0)
        return divisor;

    remainder = 1, quotient = 0;

    while (remainder != 0)
    {
        quotient = dividend / divisor;
        remainder = dividend % divisor;
        if (remainder != 0)
            gcd = remainder;
        dividend = divisor;
        divisor = remainder;
    }
    return gcd;
}

int *operate(int a, int b, int c, int d, char operation, int *num, int *den)
{

    switch (operation)
    {
    case '*':
        *num = a * c;
        *den = b * d;
        break;
    case '+':
        *num = a * d + c * b;
        *den = b * d;
        break;
    case '/':
        *num = a * d;
        *den = b * c;
        break;
    case '-':
        *num = a * d - c * b;
        *den = b * d;
        break;
    default:
        break;
    }
}

int main()
{
    int test_cases;
    int a, b, c, d; // a/b (op) c/d
    char operation;
    int num, den;
    scanf("%d", &test_cases);

    while (test_cases-- > 0)
    {
        scanf("%d / %d %c %d / %d", &a, &b, &operation, &c, &d);
        operate(a, b, c, d, operation, &num, &den);
        printf("%d/%d", num, den);
        int gcd = euclidian_gcd(num, den);
        printf(" = %d/%d\n", num / gcd, den / gcd);
    }

    return 0;
}