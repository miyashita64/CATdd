#ifndef TRIANGLE_H
#define TRIANGLE_H

#include <string>

class Triangle{
    public:
        int a;
        int b;
        int c;
        static std::string determine_type(int a, int b, int c);
};

#endif