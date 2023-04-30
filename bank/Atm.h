class Atm{
  private:
    int balance; // 残高

  public:
    // コンストラクタ
    Atm(int init_balance);
    // balanceのゲッタ―
    int getbalance();
    // 入金
    void deposit(int amount);
    // 引出
    void withdrawal(int amount);
};