// SampleClass.cpp
#include "Rgb.h"

Rgb::Rgb(int _r, int _g, int _b){
    r = _r > 255 ? 255 : (_r < 0) ? 0 : _r;
    g = _g > 255 ? 255 : (_g < 0) ? 0 : _g;
    b = _b > 255 ? 255 : (_b < 0) ? 0 : _b;
}
