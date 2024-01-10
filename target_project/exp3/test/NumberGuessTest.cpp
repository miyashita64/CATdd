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

    // 入力した値が一致しないことを判定できるか
    TEST(NumberGuessTest, checkGuessFalseTest)
    {
        NumberGuess game;
        // 正解の数を9に設定
        int answer = 9;
        game.setAnswer(answer);

        // ユーザーが入力する数を0に設定
        std::istringstream input("0");
        std::streambuf* originalCin = std::cin.rdbuf();
        std::cin.rdbuf(input.rdbuf());

        // ユーザーの予想が正しいかどうかを確認
        EXPECT_FALSE(game.checkGuess());

        // リダイレクトを元に戻す
        std::cin.rdbuf(originalCin);
    }

} // namespace tdd_sample_test