#ifndef PID_H
#define PID_H

// PIDゲインを保持する構造体
class PidGain {
 public:
  double kp;  // Pゲイン
  double ki;  // Iゲイン
  double kd;  // Dゲイン

  PidGain(double _kp, double _ki, double _kd);
};

class Pid {
 public:
  /** コンストラクタ
   * @param _targetValue 目標値
   */
  Pid(double _kp, double _ki, double _kd, double _targetValue);

  /**
   * @brief PIDゲインを設定する
   */
  void setPidGain(double _kp, double _ki, double _kd);

 private:
  PidGain gain;
  double preDeviation;  //前回の偏差
  double integral;      //偏差の累積
  double targetValue;   //目標値
};

#endif