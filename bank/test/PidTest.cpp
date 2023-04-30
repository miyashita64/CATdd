#include "Pid.h"
#include <gtest/gtest.h>

namespace etrobocon2022_test {
    // PIDゲインが全て0の場合のテスト
    TEST(PidTest, calculatePidZeroTest){
        constexpr double DELTA = 0.01;
        double expected_p = 0.0;
        double expected_i = 0.0;
        double expected_d = 0.0;
        double targetValue = 60;
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 40;
        double expected = 0;
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue));
    }

    // Pゲインのみ有効な場合
    TEST(PidTest, calculatePidOnlyPTest){
        constexpr double DELTA = 0.01;
        double expected_p = 0.6;
        double expected_i = 0.0;
        double expected_d = 0.0;
        double targetValue = 70;    // 目標値
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 20;   // 現在値
        // 目標値と現在値との差
        double currentDeviation = (targetValue - currentValue);
        double p = currentDeviation * expected_p;
        double expected = p;
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue));
    }

    // Iゲインのみ有効な場合
    TEST(PidTest, calculatePidOnlyITest){
        constexpr double DELTA = 0.01;
        double expected_p = 0.0;
        double expected_i = 0.1;
        double expected_d = 0.0;
        double targetValue = 70;    // 目標値
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 20;   // 現在値
        // 目標値と現在値との差
        double currentDeviation = (targetValue - currentValue);
        double i = currentDeviation * DELTA * expected_i;
        double expected = i;
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue));
    }

    // Dゲインのみ有効な場合
    TEST(PidTest, calculatePidOnlyDTest){
        constexpr double DELTA = 0.01;
        double expected_p = 0.0;
        double expected_i = 0.0;
        double expected_d = 0.02;
        double targetValue = 70;    // 目標値
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 20;   // 現在値
        double preDeviation = 0;    // 直前の変化量の微分
        // 目標値と現在値との差
        double currentDeviation = (targetValue - currentValue);
        double d = (currentDeviation - preDeviation) * expected_d / DELTA;
        double expected = d;
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue));
    }

    // PID制御ができるかの検証
    TEST(PidTest, calculatePidTest){
        constexpr double DELTA = 0.01;
        double expected_p = 0.6;
        double expected_i = 0.02;
        double expected_d = 0.03;
        double targetValue = 100;   // 目標値
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 0;    // 現在値
        double preDeviation = 0;    // 直前の変化量の微分
        // 目標値と現在値との差
        double currentDeviation = (targetValue - currentValue);
        double p = currentDeviation * expected_p;
        double i = currentDeviation * DELTA * expected_i;
        double d = (currentDeviation - preDeviation) * expected_d / DELTA;
        double expected = p + i + d;
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue));
    }

    // PIDゲインがマイナスの場合
    TEST(PidTest, calculatePidMinusTest){
        constexpr double DELTA = 0.01;
        double expected_p = -0.3;
        double expected_i = -0.02;
        double expected_d = -0.175;
        double targetValue = 100;
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 0;
        double preDeviation = 0;
        double currentDeviation = (targetValue - currentValue);
        double p = currentDeviation * expected_p;
        double i = currentDeviation * DELTA * expected_i;
        double d = (currentDeviation - preDeviation) * expected_d / DELTA;
        double expected = p + i + d;
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue));
    }

    // DELTAの引数に対応できるか
    TEST(PidTest, calculatePidChangeDeltaTest){
        constexpr double DELTA = 0.03;
        double expected_p = 0.6;
        double expected_i = 0.02;
        double expected_d = 0.03;
        double targetValue = 70;
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 55;
        double preDeviation = 0;
        double currentDeviation = (targetValue - currentValue);
        double p = currentDeviation * expected_p;
        double i = currentDeviation * DELTA * expected_i;
        double d = (currentDeviation - preDeviation) * expected_d / DELTA;
        double expected = p + i + d;
        //第2引数に周期を渡し、周期に応じた計算結果を返すことができるかを確認(デフォルトでは0.01が渡される)
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue, DELTA));
    }

    //周期に0を渡したときに、デフォルト周期0.01として計算されるかをテストする
    TEST(PidTest, calculatePidChangeDeltaZeroTest){
        constexpr double DELTA = 0;              //実際に渡す周期
        constexpr double EXPECTED_DELTA = 0.01;  //期待される周期
        double expected_p = 0.6;
        double expected_i = 0.02;
        double expected_d = 0.03;
        double targetValue = 70;
        Pid actualPid(expected_p, expected_i, expected_d, targetValue);
        double currentValue = 55;
        double preDeviation = 0;
        double currentDeviation = (targetValue - currentValue);
        double p = currentDeviation * expected_p;
        double i = currentDeviation * EXPECTED_DELTA * expected_i;
        double d = (currentDeviation - preDeviation) * expected_d / EXPECTED_DELTA;
        double expected = p + i + d;
        //第2引数に周期を渡し、周期に応じた計算結果を返すことができるかを確認(デフォルトでは0.01が渡される)
        EXPECT_DOUBLE_EQ(expected, actualPid.calculatePid(currentValue, DELTA));
    }
}  // namespace etrobocon2022_test
