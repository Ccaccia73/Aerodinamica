/*
 * vector3d.hpp
 *
 *  Created on: Dec 14, 2017
 *      Author: claudio
 */

#ifndef SRC_VECTOR3D_HPP_
#define SRC_VECTOR3D_HPP_



#ifndef VECTOR3D
#define VECTOR3D

#include <cassert>
#include <cmath>
#include <string>
#include <cmath>

/** @brief vector3d class to represent an array of size 3
 *
 * useful in representing 3d point coordinates, vectors, forces, etc.
 * Also performs some basic operations, helps in reducing equations sizes
 */

class vector3d{
private:
    double _data[3];
public:
    /* empty constructor, initializes vector to zero */
    vector3d();
    /* base constructor, 3 parameters are the coordinates */
    vector3d(double a,double b,double c);
    /* copy constructor */
    vector3d(const vector3d& vec);

    /* index operators */
    double operator [] (int i) const;

    double& operator [] (int i);

    /*assignment operators */
    void operator = (const vector3d& vec);

    const vector3d& operator = (const vector3d& vec) const;

    /* assign scalar to all components */
    void operator = (const double val);

    /* norms and normalization */
    double squared_norm() const;

    double norm() const;

    void normalize();

    /* size: not so useful.... */
    int size() const;

    /* print functions */
    void print ();

    friend std::ostream& operator << (std::ostream& os, const vector3d& vec){
        os << std::scientific << vec[0] << "\t" << vec[1] << "\t" << vec[2];
        return os;
    }


    /* basic operations */
    vector3d operator + (const vector3d& vec) const;

    vector3d operator - (const vector3d& vec) const;

    /* multiply with scalar */
    vector3d operator * (const double& val) const;
    vector3d operator / (const double& val) const;

    /* inversion */
    vector3d operator - () const;

    /* member by member division */
    vector3d operator / (const vector3d& vec) const;

    /* dot product */
    double dot(const vector3d& vec);

    /* cross product */
    vector3d cross(const vector3d& vec) const;

    /* operation and assignment */
    void operator += (const vector3d& vec);
    void operator -= (const vector3d& vec);
    void operator *= (const double& x);

    /* pointer */
    double* begin();

    /* casting */
    operator vector3d      &()       { return static_cast<      vector3d&>(*this); }
    operator vector3d const&() const { return static_cast<const vector3d&>(*this); }
    //operator vector3d      &();
    //operator vector3d const&();





};


#endif // VECTOR3D


#endif /* SRC_VECTOR3D_HPP_ */
