#include "Triangle.h"
#include <cmath>

std::string Triangle::determine_type(int a, int b, int c) {
    if (a == b && b == c) {
        return "正三角形";
    } else if (a == b || b == c || a == c) {
        return "二等辺三角形";
    } else if (a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b) {
        // ピタゴラスの定理を使用して直角三角形を判別
        return "直角三角形";
    } else {
        return "三角形";
    }
}