#include "Rgb.h"
#include <gtest/gtest.h>

namespace tdd_sample_test
{
    // RGBクラスをインスタンス化できるか
    TEST(RgbTest, rgbConstructorUnderTest){
        Rgb rgb(4, 125, -1);
        EXPECT_EQ(rgb.r, 4);
        EXPECT_EQ(rgb.g, 125);
        EXPECT_EQ(rgb.b, 0);
    }
} // namespace tdd_sample_test