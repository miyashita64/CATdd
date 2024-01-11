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

    // 直角三角形であることを判別できるか
    TEST(TriangleTest, determineTypeRightTest){
        EXPECT_STREQ(Triangle::determine_type(3, 4, 5).c_str(), "直角三角形");
    }

    // 三角形であることを判別できるか
    TEST(TriangleTest, determineTypeTest){
        EXPECT_STREQ(Triangle::determine_type(2, 3, 4).c_str(), "三角形");
    }

    // 三角形でないことを判別できるか
    TEST(TriangleTest, determineTypeNonTest){
        EXPECT_STREQ(Triangle::determine_type(200, 3, 4).c_str(), "非三角形");
    }
} // namespace tdd_sample_test