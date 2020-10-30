# @File    : dubbo_params
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/9 9:59

# pom.xml 文件增加
<dependency>
  <groupId>com.ztjy</groupId>
  <artifactId>ztjy-sales-openservice-facade</artifactId>
  <version>1.3.6-SNAPSHOT</version>
</dependency>
#maven引入
java_maven_init()
print(DubboClient('zookeeper://zookeeper.szy.com:2181').object2Json('com.ztjy.sales.model.order.PayOrderRequest'))
#枚举不是常规的类，不是json，无法使用
print(DubboClient('zookeeper://zookeeper.szy.com:2181').object2Json('com.ztjy.sales.enums.PayChannel'))


def generator_set_params(self, *args):
    dataSet = []
    for i in args:
        dataSet.append({"type": "java.lang.String", "data": i})
    return dataSet

def generator_params(self, **kwargs):
    params = []
    for k, v in kwargs.items():
        if isinstance(v, list):
            if k == 'classIdSet':
                params.append({"type": "java.util.Set", "data": v})
            else:
                params.append({"type": "java.util.List", "data": v})
        elif k == 'isFlag':
            params.append({"type": "java.lang.Byte", "data": v})
        elif k == 'lastDate':
            params.append({"type": "java.util.Date", "data": {"format": "yyyy-MM-dd HH:mm:ss", "datetime": "%s"}})
        else:
            params.append({"type": "java.lang.String", "data": v})
    return params

def generator_params(self, **kwargs):
    params = []
    for k,v in kwargs.items():
        if isinstance(v, list):
            if k == 'classIdSet':
                if v is None:
                    params.append({"type": "java.util.Set", "data": []})
                if v == '':
                    params.append({"type": "java.util.Set", "data": ['']})
                else:
                    params.append({"type": "java.util.Set", "data": v})
            else:
                params.append({"type": "java.util.List", "data": v})
        elif k == 'isFlag':
            if v is None:
                params.append({"type": "java.lang.Byte", "data": "null"})
            if v == '':
                params.append({"type": "java.lang.Byte", "data": ''})
            else:
                params.append({"type": "java.lang.Byte", "data": v})
        elif k == 'lastDate':
            params.append({"type":"java.util.Date","data":{"format":"yyyy-MM-dd HH:mm:ss","datetime":"%s"}})
        else:
            if v is None:
                params.append({"type": "java.lang.String", "data": "null"})
            if v == '':
                params.append({"type": "java.lang.String", "data": ''})
            else:
                params.append({"type": "java.lang.String", "data": v})
    return params

def generator_params(self, **kwargs):
    params = []
    for k, v in kwargs.items():
        if v == "null":
            params.append({"type": "java.lang.String", "data": None})
        elif v == "":
            params.append({"type": "java.lang.String", "data": ''})
        else:
            params.append({"type": "java.lang.String", "data": v})
    return params

def generator_params1(self, *args):
    params = []
    for arg in args:
        if isinstance(arg, int):
            params.append({"type": "java.lang.Long", "data": arg})
        if isinstance(arg, str):
            params.append({"type": "java.lang.String", "data": arg})
    return params


def generator_dto_params(self, **kwargs):
    params = {}
    params.update(**kwargs)
    return params


def generator_params(self, **kwargs):
    params = []
    for k, v in kwargs.items():
        if k == 'SchoolPasswordDTO':
            params.append({'type': 'com.ztjy.hms.server.model.dto.SchoolPasswordDTO', 'data': v})
        elif v == "null":
            params.append({"type": "java.lang.String", "data": None})
        elif v == "":
            params.append({"type": "java.lang.String", "data": ''})
        else:
            params.append({"type": "java.lang.String", "data": v})
    return params


def test_ignore_schoolId_growth_share_to_notice_machine(self):
    msgId = self.randomValue
    contentType = 100

    params = self.iNoticeFacade.generator_params1(growthId=msgId, contentType=contentType)
    try:
        result = self.iNoticeFacade.growthShareToNoticeMachine(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains('NoSuchMethodException')
    else:
        assert_that(result).is_not_none()