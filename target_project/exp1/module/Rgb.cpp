// SampleClass.cpp
#include "Rgb.h"

Rgb::Rgb(int _r, int _g, int _b){
    r = _r > 255 ? 255 : _r;
    g = _g > 255 ? 255 : _g;
    b = _b > 255 ? 255 : _b;
}
