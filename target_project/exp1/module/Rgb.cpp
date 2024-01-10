#include "Rgb.h"

Rgb::Rgb(int _r, int _g, int _b) : r(_r), g(_g), b(_b){
    if (r > 255){
        r = 255;
    };

    if (r < 0){
        r = 0;
    };

    if (g > 255){
        g = 255;
    };

    if (g < 0){
        g = 0;
    }

    if (b > 255){
        b = 255;
    };

    if (b < 0){
        b = 0;
    }

};
