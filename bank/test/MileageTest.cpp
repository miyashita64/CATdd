#include "Mileage.h"
#include <math.h>
#include <gtest/gtest.h>

namespace etrobocon2022_test {
    TEST(calculateMileageTest, calculateMilageZeroTest){
        double radius = 50;         // 車輪の半径
        double rightAngle = 0;      // 右車輪の回転角度
        double leftAngle = 0;       // 左車輪の回転角度
        double expected = 0;
        double actual = Mileage::calculateMileage(rightAngle, leftAngle);
        EXPECT_DOUBLE_EQ(expected, actual);
    }

    TEST(calculateMileageTest, calculateMilageOnlyRightTest){
        double radius = 50;
        double rightAngle = 10;
        double leftAngle = 0;
        double rightWheel = 2 * rightAngle * radius * M_PI / 360;
        double expected = rightWheel / 2;
        double actual = Mileage::calculateMileage(rightAngle, leftAngle);
        EXPECT_DOUBLE_EQ(expected, actual);
    }

    TEST(calculateMileageTest, calculateMilageOnlyLeftTest){
        double radius = 50;
        double rightAngle = 0;
        double leftAngle = 20;
        double leftWheel = 2 * leftAngle * radius * M_PI / 360;
        double expected = leftWheel / 2;
        double actual = Mileage::calculateMileage(rightAngle, leftAngle);
        EXPECT_DOUBLE_EQ(expected, actual);
    }

    TEST(calculateMileageTest, calculateMilageTest){
        double radius = 50;
        double rightAngle = 30;
        double leftAngle = 20;
        double rightWheel = 2 * rightAngle * radius * M_PI / 360;
        double leftWheel = 2 * leftAngle * radius * M_PI / 360;
        double expected = (rightWheel + leftWheel) / 2;
        double actual = Mileage::calculateMileage(rightAngle, leftAngle);
        EXPECT_DOUBLE_EQ(expected, actual);
    }

    TEST(calculateMileageTest, calculateMilageMinusTest){
        double radius = 50;
        double rightAngle = -10;
        double leftAngle = -20;
        double rightWheel = 2 * rightAngle * radius * M_PI / 360;
        double leftWheel = 2 * leftAngle * radius * M_PI / 360;
        double expected = (rightWheel + leftWheel) / 2;
        double actual = Mileage::calculateMileage(rightAngle, leftAngle);
        EXPECT_DOUBLE_EQ(expected, actual);
    }
}  // namespace etrobocon2022_test