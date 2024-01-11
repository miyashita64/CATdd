
#include "Triangle.h"

std::string Triangle::determine_type(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        return "非三角形";
    }
    if (a + b <= c || b + c <= a || a + c <= b) {
        return "非三角形";
    }
    if (a == b && b == c) {
        return "正三角形";
    }
    else if (a == b || b == c || a == c) {
        return "二等辺三角形";
    }
    else if (a * a + b * b == c * c || b * b + c * c == a * a || a * a + c * c == b * b) {
        return "直角三角形";
    }
    return "三角形";
}
