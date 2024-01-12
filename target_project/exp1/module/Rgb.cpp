// Rgb.cpp
#include "Rgb.h"

Rgb::Rgb(int red, int green, int blue) : r(clamp(red, 0, 255)), g(clamp(green, 0, 255)), b(clamp(blue, 0, 255)) {}

int Rgb::clamp(int value, int min, int max) {
    return (value < min) ? min : (value > max) ? max : value;
}
