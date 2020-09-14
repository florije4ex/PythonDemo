# @File    : dubbo_params
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/9 9:59

def generator_params1(self, *args):
    params = []
    for arg in args:
        if isinstance(arg, int):
            params.append({"type": "java.lang.Long", "data": arg})
        if isinstance(arg, str):
            params.append({"type": "java.lang.String", "data": arg})
    return params