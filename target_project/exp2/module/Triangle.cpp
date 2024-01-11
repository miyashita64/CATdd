#include "Triangle.h"
#include <string>
#include <iostream>

std::string Triangle::determine_type(int a, int b, int c){
    if (a == b && b == c){
        return "正三角形";
    }

    if (a == c || a == b || b == c){
        return "二等辺三角形";
    }
}
