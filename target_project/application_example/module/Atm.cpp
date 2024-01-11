#include "Atm.h"

// コンストラクタ
Atm::Atm(int initialBalance){
    if (initialBalance < 0){
        balance = 0;
    } else {
        balance = initialBalance;
    }
}

// 残高(balance)のゲッター
int Atm::getBalance() const {
    return balance;
}

// 振込
void Atm::transfer(int amount) {
    if (amount >= 0 && amount <= MAX_AMOUNT && amount <= balance) {
        balance -= amount;
    }
}

// 入金
void Atm::deposit(int amount) {
    if (amount >= 0 && amount <= MAX_AMOUNT) {
        balance += amount;
    }
}