#include "Triangle.h"
#include <string>
#include <iostream>
#include <math.h>

std::string Triangle::determine_type(int a, int b, int c){
    if (a == b && b == c){
        return "正三角形";
    }

    if (a == c || a == b || b == c){
        return "二等辺三角形";
    }

    if (sqrt(a*a + b*b) == c || sqrt(b*b + c*c) == a || sqrt(a*a + c*c) == b){
        return "直角三角形";
    }

    if (a + b > c || b + c > a || c + a > b){
        return "三角形";
    }
}
