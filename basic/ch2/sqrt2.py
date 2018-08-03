"""
Description
Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

Notice
You do not care about the accuracy of the result, we will help you to output results.

Example
Given n = 2 return 1.41421356
"""

from __future__ import division

def sqrt(x):
	if x == 0.:
		return 0.
	elif x == 1.:
		return 1.

	threshold = 1e-12

	# check if x > 1 (ex. 2) or < 1 (ex. 0.25)
	start = 1.
	end = x

	if x < 1:
		start = x
		end = 1

	while end - start > threshold:
		mid = start + (end - start) / 2.
		mid_2 = mid * mid
		if mid_2 == x:
			return mid_2
		elif mid_2 < x:
			start = mid
		else:
			end = mid

	return (start + end) / 2

print sqrt(4.)
print sqrt(2.)
print sqrt(0.25)
print sqrt(0.5)
			


