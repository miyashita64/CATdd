#include "Triangle.h"
#include <gtest/gtest.h>

namespace tdd_sample_test
{
    // 正三角形であることを判別できるか
    TEST(TriangleTest, determineTypeEquilateralTest){
        EXPECT_STREQ(Triangle::determine_type(2, 2, 2).c_str(), "正三角形");
    }

} // namespace tdd_sample_test