#include <iostream>
#include <algorithm>
using namespace std;

void part1()
{
    int minx, maxx, miny, maxy;
    int input = std::scanf("target area: x=%d..%d, y=%d..%d", &minx, &maxx, &miny, &maxy);
    int ty = miny + 1;
    int vyo = -ty;
    std::cout << vyo * (vyo + 1) / 2 << std::endl;
}

void part2()
{
    int minx, maxx, miny, maxy;
    int input = std::scanf("target area: x=%d..%d, y=%d..%d", &minx, &maxx, &miny, &maxy);
    int counter = 0;
    int maxt = std::max(-2 * miny + 1, maxx); //max namespace from algorithm

    for (int vyo = miny; vyo <= -miny; vyo++)
        for (int vxo = 1; vxo <= maxx; vxo++)
            for (int t = 1; t <= maxt; t++)
            {
                int y = vyo * t - t * (t - 1) / 2;
                int x;
                if (t < vxo)
                    x = vxo * t - t * (t - 1) / 2;
                else
                    x = vxo * (vxo + 1) / 2;
                if (miny <= y && y <= maxy && minx <= x && x <= maxx)
                {
                    counter++;
                    break;
                }
            }

    std::cout << counter << std::endl;
}

int main()
{
    // part1();
    part2();
    return 0;
}