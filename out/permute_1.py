def permute(self, nums):
	if len(nums) < 2:
		return [nums]
	if len(nums) == 2:
		return [[nums[0], nums[1]], [nums[1], nums[0]]]

	res = []

	for i in range(len(nums)):
		short_list = nums.copy()
		deleted_val = short_list[i]
		del short_list[i]
		perms = self.permute(short_list)
		for j in range(len(perms)):
			perms[j].append(deleted_val)
		res += perms

	return res