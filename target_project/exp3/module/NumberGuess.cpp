#include "NumberGuess.h"

// コンストラクタ
NumberGuess::NumberGuess() : answer(0) {}

// 正解の数を設定するメソッド
void NumberGuess::setAnswer(int value) {
    answer = value;
}

// ユーザーの予想が正しいかどうかを確認するメソッド
bool NumberGuess::checkGuess() {
    int userGuess;
    std::cin >> userGuess;
    return userGuess == answer;
}
