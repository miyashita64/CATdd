
#ifndef ATM_H
#define ATM_H

class Atm {
public:
    Atm(int initialBalance = 0);
    int getBalance() const;
    void transfer(int amount);
    void deposit(int amount);

private:
    int balance;
    const int MAX_AMOUNT = 500000;
};

#endif  // ATM_H
