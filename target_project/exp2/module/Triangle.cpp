#include "Triangle.h"

std::string Triangle::determine_type(int a, int b, int c) {
    if (a == b && b == c) {
        return "正三角形";
    } else if (a == b || b == c || a == c) {
        return "二等辺三角形";
    }
}