#include "Rgb.h"
#include <gtest/gtest.h>

namespace tdd_sample_test
{
    // RGBクラスをインスタンス化できるか
    TEST(RgbTest, rgbConstructorTest){
        Rgb rgb(13, 45, 164);
        EXPECT_EQ(rgb.r, 13);
        EXPECT_EQ(rgb.g, 45);
        EXPECT_EQ(rgb.b, 164);
    }

    // 上限値を超える輝度を処理できるか
    TEST(RgbTest, rgbConstructorOverTest){
        Rgb rgb(256, 1024, 4);
        EXPECT_EQ(rgb.r, 255);
        EXPECT_EQ(rgb.g, 255);
        EXPECT_EQ(rgb.b, 4);
    }

} // namespace tdd_sample_test