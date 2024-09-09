#ifndef Transform_h_DEFINED
#define Transform_h_DEFINED

#include <math.h>
#include <stdio.h>
#include <vector>

class Transform {
public:
  Transform();
  virtual ~Transform() {}

  void clear();
  Transform &translate(double x, double y, double z);
  Transform &translate(const double *p);

  Transform &translateX(double x = 0);
  Transform &translateY(double y = 0);
  Transform &translateZ(double z = 0);
  Transform &rotateX(double a = 0);
  Transform &rotateY(double a = 0);
  Transform &rotateZ(double a = 0);
  Transform &rotateDotX(double a = 0);
  Transform &rotateDotY(double a = 0);
  Transform &rotateDotZ(double a = 0);

  Transform &translateNeg(const double *p);
  Transform &rotateDotXNeg(double a = 0);
  Transform &rotateDotYNeg(double a = 0);
  Transform &rotateDotZNeg(double a = 0);

  double getVal(int i, int j);
  void setVal(int i, int j,double value);


  Transform &mDH(double alpha, double a, double theta, double d);
  void apply(double x[3]);
  void apply0(double* x);


  double getZ();
  const void getXYZ(double* ret) const;
  const double getZ() const;


  double& operator() (int i, int j);
  const double operator() (int i, int j) const;

 private:
  double t[4][4];
};

Transform operator* (const Transform &t1, const Transform &t2);
Transform inv (const Transform &t1);
Transform trcopy (const Transform &t1);
Transform transform6D(const double p[6]);
Transform transformQuatP(const double q[7]);
std::vector<double> position6D(const Transform &t1);
std::vector<double> to_quatp(const Transform &t1);
 
void getAngularVelocityTensor(const Transform &adot, const Transform &ainv, double *av);


void printTransform(Transform tr);
void printVector(std::vector<double> v);


#endif