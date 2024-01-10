#include "NumberGuess.h"
#include <iostream>
#include <sstream>
#include <gtest/gtest.h>

namespace tdd_sample_test
{
    // 入力した値が一致したことを判定できるか
    TEST(NumberGuessTest, checkGuessTrueTest)
    {
        NumberGuess game;
        // 正解の数を7に設定
        int answer = 7;
        game.setAnswer(answer);

        // ユーザーが入力する数を7に設定
        std::istringstream input("7");
        std::streambuf* originalCin = std::cin.rdbuf();
        std::cin.rdbuf(input.rdbuf());

        // ユーザーの予想が正しいかどうかを確認
        EXPECT_TRUE(game.checkGuess());

        // リダイレクトを元に戻す
        std::cin.rdbuf(originalCin);
    }

} // namespace tdd_sample_test