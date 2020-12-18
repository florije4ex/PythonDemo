# @File    : login
# @Description: https://www.cnblogs.com/poloyy/p/12675457.html
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/18 12:19
import allure
import pytest

@pytest.fixture()
def login(request):
    """登录"""
    print(request)
    param = request.param
    print(f"账号是：{param['username']}，密码是：{param['pwd']}")
    # 返回
    return {"code": 0, "msg": "success!"}

datas = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
    {"username": "name3", "pwd": "pwd3"}
]

ids = ['用户名:{},密码:{},预期结果:'.format(item['username'],item['pwd']) for item in datas]

@allure.story('登录功能')
@pytest.mark.parametrize('login',datas, indirect=True, ids=ids)
def test_login1(login):
    """
    登录测试用例1
    """
    assert login['code'] == 0


# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# ids
ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]


@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect