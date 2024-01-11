#include "Rgb.h"

Rgb::Rgb(int _r,int _g,int _b){
if (_r > 255){_r = 255;}
if (_g > 255){_g = 255;}
if (_b > 255){_b = 255;} 
if (_r < 0){_r = 0;}
if (_g < 0){_g = 0;}
if (_b < 0){_b = 0;} 
r = _r ; 
g = _g ;
b = _b ;
}


