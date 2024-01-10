#include "Triangle.h"
#include <algorithm>

std::string Triangle::determine_type(int side1, int side2, int side3)
{
    if (is_right_triangle(side1, side2, side3))
    {
        return "直角三角形";
    }
    else if (side1 == side2 && side2 == side3)
    {
        return "正三角形";
    }
    else if (side1 == side2 || side2 == side3 || side1 == side3)
    {
        return "二等辺三角形";
    }
}

bool Triangle::is_right_triangle(int side1, int side2, int side3)
{
    // ピタゴラスの定理を用いて直角三角形かどうか判定
    int sides[3] = {side1, side2, side3};
    std::sort(sides, sides + 3);

    return sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2];
}
