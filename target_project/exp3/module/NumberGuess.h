#ifndef NUMBERGUESS_H
#define NUMBERGUESS_H

#include <iostream>

class NumberGuess {
private:
    int answer;

public:
    // コンストラクタ
    NumberGuess();

    // 正解の数を設定するメソッド
    void setAnswer(int value);

    // ユーザーの予想が正しいかどうかを確認するメソッド
    bool checkGuess();
};

#endif // NUMBERGUESS_H