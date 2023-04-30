#include "Atm.h"

Atm::Atm(int init_balance) : balance(init_balance){}

int Atm::getbalance(){
    return balance;
}

void Atm::deposit(int amount){
    if(amount > 0){
        balance += amount;
    }
}

void Atm::withdrawal(int amount){
    if(amount > 0){
        if(balance - amount >= 0){
            balance -= amount;
        }
    }
}