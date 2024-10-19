def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
	m = len(mat)
	n = len(mat[0])

	if m * n != r * c:
		return mat

	res = [[0]*c for _ in range(r)]

	index = 0

	for index in range(m * n):
		i_mat = index // n
		j_mat = index % n
		i_res = index // c
		j_res = index % c

		res[i_res][j_res] = mat[i_mat][j_mat]

	return res