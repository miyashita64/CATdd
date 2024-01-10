#ifndef TRIANGLE_CLASS_H
#define TRIANGLE_CLASS_H

#include <string>
#include "Triangle.h"

class Triangle
{
    public:
        static std::string determine_type(int side1, int side2, int side3);
};

#endif
