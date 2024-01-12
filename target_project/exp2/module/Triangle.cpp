#include "Triangle.h"

Triangle::Triangle(){};

std::string Triangle::determine_type(int a, int b, int c){

    std::string result = "初期値";
    int ap2 = pow(a, 2.0);
    int bp2 = pow(b, 2.0);
    int cp2 = pow(c, 2.0);

    if(a == b && b == c){
        result = "正三角形";
    }else if((a == b && b != c) | (a==c && c!=b) | (b==c && c!=a)){
        result = "二等辺三角形";
    }else if((ap2 == bp2 + cp2) | (bp2 == cp2 + ap2) | (cp2 == bp2 + ap2)){
        result = "直角三角形";
    }else if(a > 0 && b > 0 && c > 0){
        result = "三角形";
    }
    
    return result;
}
