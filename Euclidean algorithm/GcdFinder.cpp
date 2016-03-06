/*
 * GcdFinder.cpp
 *
 *  Created on: Mar 5, 2016
 *      Author: eduardo
 */

#include "GcdFinder.h"

long GcdFinder::gcd_otimized(long a, long b){
	if (b == 0)
		return a;

	return gcd_otimized(b, a%b);

}

