// Rgb.h
#pragma once

class Rgb {
public:
    Rgb(int red, int green, int blue);
    int r;
    int g;
    int b;

private:
    // 上限値を超える輝度を修正するためのプライベートユーティリティ関数
    int clamp(int value, int min, int max);
};

