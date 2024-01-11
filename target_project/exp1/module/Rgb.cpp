
#include "Rgb.h"

Rgb::Rgb(int red, int green, int blue) : r(red), g(green), b(blue) {
    // Adjust colors if they exceed the limit
    if (r > 255) r = 255;
    if (g > 255) g = 255;
    if (b > 255) b = 255;
}
