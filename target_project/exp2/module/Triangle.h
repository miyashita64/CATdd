#ifndef TRIANGLE_H
#define TRIANGLE_H
#include <stdio.h>
#include <string>
#include <math.h>

class Triangle{
    public:

    Triangle();

    static std::string determine_type(int a, int b, int c);
};
#endif