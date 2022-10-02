#include <stack>
#include <iostream>

using namespace std;

struct frame
{
    int n;
    int r;
    int a;
    int* p;
    bool grow;

    frame(int m, int b, int* q) : n(m), r(0), a(b), p(q), grow(true) {}
};

int fact(int n)
{
    int r = 0;
    stack<frame> W;

    W.push(frame(n, 1, &r));
    while (!W.empty())
    {
        frame& f = W.top();

        cout << "frame " << f.n << endl;
        if (f.grow)
        {
            if (f.n == 0)
            {
                *f.p = 1;
                W.pop();
            } else {
                f.grow = false;
                W.push(frame(f.n - 1, f.n, &f.r));
            }
        } else {
            *f.p = f.r * f.a;
            W.pop();
        }
    }

    return r;
}

int main()
{
    cout << fact(5) << endl;
    return 0;
}

