
#include "Triangle.h"

std::string Triangle::determine_type(int a, int b, int c) {
    if (a == b && b == c) {
        return "正三角形";
    }
    return "不明";
}
