
#include "Rgb.h"

Rgb::Rgb(int r, int g, int b) : r(r), g(g), b(b) {
    if (this->r > 255) {
        this->r = 255;
    } else if (this->r < 0) {
        this->r = 0;
    }

    if (this->g > 255) {
        this->g = 255;
    } else if (this->g < 0) {
        this->g = 0;
    }

    if (this->b > 255) {
        this->b = 255;
    } else if (this->b < 0) {
        this->b = 0;
    }
}
