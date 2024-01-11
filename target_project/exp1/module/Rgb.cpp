#include "Rgb.h"

Rgb::Rgb(int red, int green, int blue) {
    // 上限値を超える輝度を制限
    r = (red > 255) ? 255 : (red < 0) ? 0 : red;
    g = (green > 255) ? 255 : (green < 0) ? 0 : green;
    b = (blue > 255) ? 255 : (blue < 0) ? 0 : blue;
}