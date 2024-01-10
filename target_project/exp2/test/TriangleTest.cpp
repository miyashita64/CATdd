#include "Triangle.h"
#include <gtest/gtest.h>

namespace tdd_sample_test
{
    // 正三角形であることを判別できるか
    TEST(TriangleTest, determineTypeEquilateralTest){
        EXPECT_STREQ(Triangle::determine_type(2, 2, 2).c_str(), "正三角形");
    }

    // 二等辺三角形であることを判別できるか
    TEST(TriangleTest, determineTypeScaleneTest){
        EXPECT_STREQ(Triangle::determine_type(3, 2, 2).c_str(), "二等辺三角形");
    }

} // namespace tdd_sample_test