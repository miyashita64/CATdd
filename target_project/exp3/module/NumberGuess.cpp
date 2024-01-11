
#include "NumberGuess.h"
#include <iostream>

void NumberGuess::setAnswer(int answer) {
    this->answer = answer;
}

bool NumberGuess::checkGuess() {
    int guess;
    std::cin >> guess; // ユーザーの予想を受け取る
    return (guess == answer); // ユーザーの予想が答えと一致しているかどうかを返す
}
