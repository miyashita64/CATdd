
#include "Rgb.h"

Rgb::Rgb(int r, int g, int b) : r(r), g(g), b(b) {
    // コンストラクタの実装
    if (this->r > 255) {
        this->r = 255;
    }
    if (this->g > 255) {
        this->g = 255;
    }
    if (this->b > 255) {
        this->b = 255;
    }
}
