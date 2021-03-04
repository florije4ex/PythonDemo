# @File    : pairs_datas
# @Description:
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/17 17:55
import pytest
from allpairspy import AllPairs


def pairs_datas():
    """
    采取 pairwise ( 结对测试 ) 的测试策略进行用例设计，减少测试组合的同时最大化用例性价比
    :return: 符合正交分析结果的测试数据集
    """
    param_data = [
        [None, '', 'A' * 25, 1000, 99 * 1000],  # verifyId
        [None, '', 'A' * 25, '64a84ab4dd4a9404085d', '48734923e22c435b8afa'],  # studentId
        [None, '', 'A' * 25, '819e250a696846b39d35', '455361a46b2a837e3861'],  # childId
    ]
    return AllPairs(param_data)

class Test_1:
    def setup_class(self):
        pass
    @pytest.mark.parametrize('verifyId, studentId, childId', pairs_datas())
    def test_1(childId, studentId, verifyId):
        print(childId)
        print(studentId)
        print(verifyId)