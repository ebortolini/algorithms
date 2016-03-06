#include <iostream>
#include "GcdFinder.h"
#include <assert.h>

using namespace std;

#define assert_equal(value_1, value_2, in_1, in_2, message) \
	do { \
		if(value_1 != value_2) \
			cout << message << " in line:" << __LINE__ << "\n"; \
		else \
			cout << "Test Passed: GCD(" << in_1 << "," << in_2 << ") = " << value_2 << "\n"; \
	}while(0)


int main(){
	GcdFinder gcd;

	long result;

	result =  gcd.gcd_otimized(10,10);
	assert_equal(10,result,10,10, "Expected: 10, Actual: "<< result );

	result =  gcd.gcd_otimized(80770010,12005);
	assert_equal(5,result,80770010,12005, "Expected: 10, Actual: "<< result );

	result =  gcd.gcd_otimized(12005,80770010);
	assert_equal(5,result,12005,80770010, "Expected: 10, Actual: "<< result );

	result =  gcd.gcd_otimized(9851248,99587412);
	assert_equal(4,result,9851248,99587412, "Expected: 10, Actual: "<< result );

	return 0;
}
