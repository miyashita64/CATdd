// Triangle.h
#ifndef SAMPLE_CLASS_H
#define SAMPLE_CLASS_H

#include <string>

class Triangle {
public:
    static std::string determine_type(int side1, int side2, int side3);
};

#endif