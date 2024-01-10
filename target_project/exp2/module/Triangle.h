#ifndef TRIANGLE_CLASS_H
#define TRIANGLE_CLASS_H

#include <string>

class Triangle
{
public:
    static std::string determine_type(int side1, int side2, int side3);
    static bool is_right_triangle(int side1, int side2, int side3);
};

#endif
