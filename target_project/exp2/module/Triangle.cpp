// Triangle.cpp
#include "Triangle.h"
#include <cmath>
#include <algorithm>

std::string Triangle::determine_type(int side1, int side2, int side3) {
    // 辺の長さをソート
    int sides[] = {side1, side2, side3};
    std::sort(sides, sides + 3);

    if (sides[0] + sides[1] > sides[2]) {
        if (sides[0] == sides[1] && sides[1] == sides[2]) {
            return "正三角形";
        } else if (sides[0] == sides[1] || sides[1] == sides[2]) {
            return "二等辺三角形";
        } else if (std::pow(sides[0], 2) + std::pow(sides[1], 2) == std::pow(sides[2], 2)) {
            return "直角三角形";
        } else {
            return "その他";
        }
    } else {
        return "三角形ではありません";
    }
}