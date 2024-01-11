#include "Triangle.h"

Triangle::Triangle(){};

std::string Triangle::determine_type(int a, int b, int c){

    std::string result = "図形";

    if(a == b && b == c){
        result = "正三角形";
    }
    return result;
}
