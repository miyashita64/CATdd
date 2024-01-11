
#pragma once

class NumberGuess {
public:
    void setAnswer(int answer);
    bool checkGuess();

private:
    int answer; // 追加: 答えを保持するためのフィールド
};
