class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def exclude_half_k(self, k, A, a, B, b):
        m = len(A)
        n = len(B)
        a_left = max(m-1-a, 0)
        b_left = max(n-1-b, 0)
        step = min(k/2-1, a_left, b_left)

        a_next = a + step
        b_next = b + step

        if A[a_next] < B[b_next]:
            a = a_next + 1
        else:
            b = b_next + 1

        k = k - (step + 1)

        return k, a, b

    def find_kth(self, k, A, a, B, b):
        m = len(A)
        n = len(B)
        result = None
        index = 0

        while index < k:
            if a < m and b >= n:
                result = A[a]
                a = a + 1
            elif a >= m and b < n:
                result = B[b]
                b = b + 1
            elif A[a] < B[b]:
                result = A[a]
                a = a + 1
            else:
                result = B[b]
                b = b + 1
            index = index + 1

        return result

    def findMedianSortedArrays(self, A, B):
        # write your code here

        # init variables
        m = len(A)
        n = len(B)
        is_odd = (m + n) % 2 == 1
        k = (m + n) / 2
        if is_odd:
            k = k + 1

        # excluse half k
        a = 0
        b = 0
        while k > 1 and a < m and b < n:
            k, a, b = self.exclude_half_k(k, A, a, B, b)

        # find median
        kth = self.find_kth(k, A, a, B, b)
        if is_odd:
            return kth
        
        k_1th = self.find_kth(k+1, A, a, B, b)
        return (kth + k_1th) / 2.


if __name__ == '__main__':
    sol = Solution()

    m = sol.findMedianSortedArrays(
        [1,2,3], 
        [4,5])
    print m, 3.

    m = sol.findMedianSortedArrays(
        [1,2,3,4,5,6], 
        [2,3,4,5])
    print 'result', m, 3.5

    m = sol.findMedianSortedArrays(
        [2,3,5,7], 
        [1,4,6,8])
    print 'result', m, 4.5

    m = sol.findMedianSortedArrays(
        [1,1,1], 
        [2,2])
    print 'result', m, 1.

    m = sol.findMedianSortedArrays(
        [1], 
        [1,1,2,2,2,2])
    print 'result', m, 2.

    m = sol.findMedianSortedArrays(
        [2], 
        [])
    print 'result', m, 2.



    