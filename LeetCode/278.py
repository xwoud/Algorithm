class Solution:
    def firstBadVersion(self, n):
        mi, ni = 1, n

        while mi < ni:
            mid = (mi + ni) // 2
            if isBadVersion(mid):
                ni = mid
            else:
                mi = mid + 1

        return mi