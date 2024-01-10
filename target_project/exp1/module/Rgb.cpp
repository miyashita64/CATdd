#include "Rgb.h"

Rgb::Rgb(int _r, int _g, int _b) : r(_r), g(_g), b(_b){
    if (r > 255){
        r = 255;
    };

    if (g > 255){
        g = 255;
    };

    if (b > 255){
        b = 255;
    };

};
