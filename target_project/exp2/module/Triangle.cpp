#include "Triangle.h"

std::string Triangle::determine_type(int side1, int side2, int side3)
{
    if (side1 == side2 && side2 == side3)
    {
        return "正三角形";
    }
    else if (side1 == side2 || side2 == side3 || side1 == side3)
    {
        return "二等辺三角形";
    }
}
