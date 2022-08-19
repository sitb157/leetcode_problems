class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m_l = len(matrix)
        temp_m = [[0 for _ in range(m_l)] for _ in range(m_l)]
        for i in range(m_l):
            for j in range(m_l):
                num = matrix[i][j]
                m_i = j
                m_j = m_l - i - 1
                temp_m[m_i][m_j] = num
        for i in range(m_l):
            for j in range(m_l):
                matrix[i][j] = temp_m[i][j]
                