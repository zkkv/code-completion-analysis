def mySqrt(x: int) -> int:
	left, right = 1, x
	while right:
		mid = (right - left) // 2 + left
		if mid * mid == x:
			return mid
		elif mid * mid < x:
			left = mid + 1
		else:
			right = mid
	return left - 1