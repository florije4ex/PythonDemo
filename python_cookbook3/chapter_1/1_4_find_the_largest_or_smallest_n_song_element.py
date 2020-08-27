# @File    : 1_4_find_the_largest_or_smallest_n_song_element
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/8/26 12:23
import heapq


class FindTheLargestOrSmallestNElements:
    def heapq_maximum_and_minimum_values_in_the_set(count, numSet):
        # nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 38]
        #一个集合中获得最大或者最小的 N 个元素列表
        largest = heapq.nlargest(count, numSet)
        smallest = heapq.nsmallest(count, numSet)
        return largest,smallest

    #在对每个元素进行对比的时候，会以 price 的值进行比较
    def heapq_accept_keyword_parameters(listSet, count, keyValue):
        # portfolio = [
        #     {'name': 'IBM', 'shares': 100, 'price': 91.1},
        #     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        #     {'name': 'FB', 'shares': 200, 'price': 21.09},
        #     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        #     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        #     {'name': 'ACME', 'shares': 75, 'price': 115.65}
        # ]
        #两个函数都能接受一个关键字参数，用于更复杂的数据结构中
        largest = heapq.nsmallest(count, listSet, key=lambda s: s[keyValue])
        smallest = heapq.nlargest(count, listSet, key=lambda s: s[keyValue])
        return largest, smallest

    #一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，
    # 那么这些函数提供了很好的性能。 因为在底层实现里面，
    # 首先会先将集合数据进行堆排序后放入一个列表中
    #堆数据结构最重要的特征是 heap[0] 永远是最小的元素
    def heapq_high_performance_query_function(numSet):
        heap = list(numSet)
        heapq.heapify(heap)
        return heap


if __name__ == '__main__':
    cls = FindTheLargestOrSmallestNElements
    count = 3
    #First
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 38,2]
    largest,smallest = cls.heapq_maximum_and_minimum_values_in_the_set(count,nums)
    print('打印集合最大值3个：', largest)
    print('打印集合最小值3个：', smallest)

    #Second
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    smallest,largest = cls.heapq_accept_keyword_parameters(portfolio,count,'price')
    print("价格最高的三组数：",largest)
    print("价格最低的三组数：",smallest)

    #Third
    numHeapq = cls.heapq_high_performance_query_function(nums)
    for a in numHeapq:
        print("打印出来优化后的set：",heapq.heappop(numHeapq))
