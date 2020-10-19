"""
[分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
逐步分析各个情况
1. 等和子集，和一定是偶数
2. 等和子集，列表中最大元素肯定要小于等于二分之和
3. 等于二分之和，一定可以切割
4. 大于二分之和，一定不能切割
5. 小于二分之和，排序后依据最大元素找寻子集
"""


def partition_equal_subset_sum(nums):
    """
    :param nums: [1, 5, 11, 5, 3, 3]
    :return: bool
    """
    if not nums:
        return False
    he = sum(nums)
    if he % 2 != 0:
        return False

    partition = int(he / 2)
    nums.sort()
    if nums[-1] > partition:
        return False
    if nums[-1] == partition:
        return True
    length = len(nums)
    partition -= nums[-1]
    for i in range(length-1, -1, -1):
        if nums[i] <= partition:
            copy = partition
            copy -= nums[i]
            if copy == 0:
                return True
            for j in range(i-1, -1, -1):
                if nums[j] <= copy:
                    copy -= nums[j]
                if copy == 0:
                    return True
    return False


if __name__ == "__main__":
    print(partition_equal_subset_sum([1, 3, 4, 1]))
