# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: zhangjf
# * Date: 2020/11/20 21:46

import os
import re

import requests


class RPCGeter(object):
    """
    根据过滤参数，从DubboAdmin上获取RPC接口信息：项目名、接口名、方法名
    :param : 过滤关键字，字符串类型，以逗号分隔
    :return : RPC接口信息：项目名，接口名，方法名
    """

    def __init__(self, filter_keyword=None):
        # 按关键字进行过滤的能力。不过滤的话，可以放个*，如['*']，但不建议，Facade里基本上没有接口文档，无法解析。
        # 建议在DubboAdmin上先试着过滤，确认范围是正确的后再来这里使用
        if filter_keyword is None:
            filter_keyword = ['ICleanCacheFacade']
        self.filter_keyword = filter_keyword
        # 连接DubboAdmin的Session对象初始化
        self.rpc_session = requests.session()

    def get_rpc(self):
        """
        获取RPC接口列表。直接从DubboAdmin上获取（默认方法）
        :return: 以List方式返回
        """
        # 初始化返回数据对象
        rpc_datas = []
        for filter_obj in self.filter_keyword:
            # 组装过滤查询参数
            request_uri = 'services?keyword={filter_obj}'.format(filter_obj=filter_obj)
            # 获取接口列表。每行记录里，包含接口名、接口服务地址。接口服务地址用于获取方法列表
            interface_list = self.get_interface_list(
                datas=self.get_datas_from_dubboadmin(uri=request_uri))
            # 获取接口的方法列表
            for interface in interface_list:
                method_list = self.get_method_list(
                    datas=self.get_datas_from_dubboadmin(uri=interface[1]))
                project_name = self.get_project_name(datas=self.get_datas_from_dubboadmin(uri=interface[1]))
                # 填充返回数据。
                rpc_datas.append('{project_name},{interface_name},{method_name_list}'.format(project_name=project_name,
                                                                                             interface_name=interface[
                                                                                                 0],
                                                                                             method_name_list=method_list))
        return rpc_datas

    def get_datas_from_dubboadmin(self, uri: str = None):
        """
        从DubboAdmin上Get数据
        :param uri: 请求的具体URI
        :return: 文本数据，字符串
        """
        # 初始化连接信息
        server_url = 'http://dubbo.szy.com:8081/governance/'
        headers = {'Host': 'dubbo.szy.com:8081',
                   'Authorization': 'Basic cm9vdDpyb290',
                   'User-Agent': 'Chrome/77.0.3865.90',
                   'Accept': 'text/html'}
        # 获取数据
        get_datas = self.rpc_session.get(server_url + uri, headers=headers).text
        return get_datas

    def get_interface_list(self, datas: str = None):
        """
        解析从DubboAdmin上获取的Interface相关信息，返回接口名称及接口服务器的地址
        TODO 目前仅实现com开头的接口，其它开头的，需要另行处理优化，如BusServer的org开头
        :param datas: 从服务器返回的字符串
        :return: 以列表方式，返回接口信息。含接口名称、接口对应的服务地址
        """
        # 提取接口的正则表达式
        regex_interface = re.compile(r'services/test/[a-zA-Z0-9-.]*')
        interfaces_data = list(set(regex_interface.findall(datas)))
        # 数据提取处理
        interface_list = []
        for interface in interfaces_data:
            server_id = self.get_server_id(datas=self.get_datas_from_dubboadmin(uri=interface + '/providers'))
            interface_list.append(
                [interface[interface.find('com'):], interface + '/providers/' + server_id])
        return interface_list

    def get_server_id(self, datas: str = None):
        """
        解析从DubboAdmin上获取的接口服务地址，返回服务ID
        :param datas: 从服务器返回的字符串
        :return: 解析出来的接口服务ID
        """
        # 提取服务器ID的正则表达式
        regex_server_id = re.compile(r'ids" value=".*?"')
        server_id_list = regex_server_id.findall(datas)
        # 数据提取处理
        server_id = ''
        if len(server_id_list) > 0:
            server_id = server_id_list[0].split('="')[1]
            server_id = server_id.split('"')[0].strip()
        else:
            print("No consumers or providers, I can't get the methods~~~~")
        return server_id

    def get_method_list(self, datas: str = None):
        """
        解析从DubboAdmin上获取的方法列表信息，返回方法列表
        :param datas: 从服务器返回的字符串
        :return: 解析出来的方法列表。以字符串方式返回，各个方法之间以"/"分隔
        """
        # 提取方法列表的正则表达式
        regex_method_list = re.compile(r'methods=[a-zA-Z0-9,]*')
        method_list_datas = regex_method_list.findall(datas)
        # 数据提取处理
        method_list = ''
        if len(method_list_datas) > 0:
            method_list = method_list_datas[0].split('=')[1].replace(",", "/")
        else:
            print("未匹配到方法名列表。")
        return method_list

    def get_project_name(self, datas: str = None):
        """
        解析从DubboAdmin上获取接口的工程名，用于目录创建
        :param datas: 从服务器返回的字符串
        :return: 解析出来的方法列表。以字符串方式返回，各个方法之间以"/"分隔
        """
        # 提取方法列表的正则表达式
        regex_project_name = re.compile(r'application=[a-zA-Z0-9-]*')
        project_name_datas = regex_project_name.findall(datas)
        # 数据提取处理
        project_name = ''
        if len(project_name_datas) > 0:
            project_name = project_name_datas[0].split('=')[1]
        else:
            print("未匹配到工程名~")
        return project_name


def space(num: int = 0):
    """
    python编码要求，控制缩进空格数
    :param num: 需要缩进的空格数
    :return: 缩进的空格串
    """
    return " " * num


class RPCCreater(object):
    """
    根据过滤关键字，过滤出来的接口列表，生成common_project下的RPC接口文档。
    """

    def __init__(self, filter_keyword=None):
        # 按关键字进行过滤的能力。不过滤的话，可以放个*，如['*']，但不建议，Facade里基本上没有接口文档，无法解析。
        # 建议在DubboAdmin上先试着过滤，确认范围是正确的后再来这里使用
        if filter_keyword is None:
            filter_keyword = ['ICleanCacheFacade']
        self.filter_keyword = filter_keyword
        # 生成的接口文件存放根目录。因接口名里的信息与common_project的命名规范不一致，建议生成后再移动到正确的目录下。
        self.root_path = 'output/rpc_created/'

    def rpc_creater(self):
        """
        创建RPC位于common_project下的接口文档。
        先获取RPC列表，再逐个接口生成接口文档
        :return:
        """
        rpc_list = RPCGeter(self.filter_keyword).get_rpc()
        for rpc in rpc_list:
            # 创建PY文件
            self.create_rpc_file(rpc)

    def create_rpc_file(self, rpc_data: str = None):
        """
        根据规范，使用接口名创建PY文件.分为2步，先加上文件头及Import部分内容，再加Class定义
        :param rpc_data: 接口信息
        :return:
        """
        project_name = rpc_data.split(",")[0]
        interface_name = rpc_data.split(',')[1]
        file_name = interface_name.split('.')[-1]
        method_list = rpc_data.split(",")[-1].split('/')
        method_list.sort()
        # 判断项目目录，若不存在则创建
        if self.check_dir(self.root_path + 'common_projects/' + project_name.replace('-', '_')):
            # 创建文件，并写入数据
            with open(self.root_path + 'common_projects/' + project_name.replace('-', '_') + '/' + file_name + '.py',
                      mode='w+',
                      encoding='utf-8') as file_handle:
                self.add_header(file_handle)
                self.add_class(file_handle, project_name=project_name, interface_name=interface_name,
                               method_list=method_list)
        else:
            print("RPC——common_project，文件创建失败！")

    def check_dir(self, path_dir: str = None):
        """
        检查指定路径下的目录是否存在，不存在则创建
        :param path_dir: 目录名
        :return: True-存在；False-异常
        """
        if os.path.exists(path_dir) and os.path.isdir(path_dir):
            return True
        else:
            try:
                os.makedirs(path_dir)
                return True
            except Exception as e:
                print('目录创建失败，%s', e.__str__())
                return False

    def add_header(self, file_handle):
        """
        为脚本文件添加文件头，以及标准的Import内容
        :param file_handle: 文件操作对象
        :return: 无
        """
        file_handle.writelines(['# -\\*- coding:utf8 -\\*-\n',
                                '# * Created by IntelliJ IDEA.\n',
                                '# * User: RPCCreater\n',
                                '\n',
                                '\n',
                                'from base.api.ztjy.api_ztjy_client import API_ZTJY_Client\n',
                                'from common.dateTimeTool import DateTimeTool\n',
                                '\n',
                                '\n'])

    def add_class(self, file_handle, project_name: str = None, interface_name: str = None, method_list: list = None):
        """
        在文件中创建类，并遵照规范进行命名。添加init方法，再逐个地添加方法
        :param project_name: 接口的工程名
        :param file_handle: 文件操作对象
        :param interface_name: 接口名
        :param method_list: 方法列表
        :return: 无
        """
        # 类定义
        file_handle.write("class {class_name}(object):\n".format(class_name=interface_name.split('.')[-1]))
        # 初始化方法
        file_handle.writelines([space(4) + "def __init__(self):\n",
                                space(8) + "self.ztjy_client = API_ZTJY_Client()\n",
                                space(8) + "self._interface = '{interface_name}'\n".format(
                                    interface_name=interface_name)])
        # 将方法添加上
        file_handle.writelines(
            [space(8) + "self._method_{method_name} = '{method_name}'\n".format(method_name=method_name) for
             method_name
             in method_list])
        # 补上空行
        file_handle.writelines(["\n"])
        # 生成整个接口共用的入参构造方法
        self.add_generator_params_fun(file_handle, project_name=project_name, interface_name=interface_name)

        # 为每个Method生成入参构造方法，以及接口请求方法
        for method in method_list:
            print(interface_name + '>>>' + method)
            self.add_request_fun(file_handle, project_name=project_name, interface_name=interface_name, method=method)

    def add_generator_params_fun(self, file_handle, project_name: str = None, interface_name: str = None):
        """
        根据接口名和方法名，构造方法的入参生成方法。聚合整个接口的入参类型，生成接口下通用参数构造方法。
        :param file_handle: 文件操作对象
        :param project_name: 接口的工程名
        :param interface_name: 接口信息
        :return: 在文件中添加入参生成方法
        """
        # 确定方法相应的入参信息
        params_dict = ParamAnalysiser().get_params(project_name=project_name, interface_name=interface_name)
        # 有包含dto入参
        for params in params_dict.keys():
            if 'DTO' not in params:
                pass
            else:
                file_handle.writelines([space(4) + "def generator_dto_params(self, **kwargs):\n",
                                        space(8) + "dataDto = {}\n",
                                        space(8) + "dataDto.update(**kwargs)\n",
                                        space(8) + "for k, v in kwargs.items():\n",
                                        space(12) + "if v == 'ignore':\n",
                                        space(16) + "dataDto.pop(k)\n",
                                        space(8) + "return dataDto\n\n"])
                break

        # 定义方法名及初始化参数
        file_handle.writelines([space(4) + "def generator_params(self, **kwargs):\n",
                                space(8) + "params = []\n"])
        # 根据参数类型构造参数生成方法
        if not params_dict:  # 空入参的，直接返回
            pass
        else:
            file_handle.writelines([space(8) + "for key, value in kwargs.items():\n",
                                    space(12) + "if value != 'ignore':\n"])
            # 获取同接口下全部的入参类型
            param_types = list(params_dict.keys())
            # 将非空标识类型从参数类型列表里去除，不需要处理
            if '@NonNull' in param_types:
                param_types.remove('@NonNull')
            # 合并同前缀的类型，再次减少类型分类.
            for param_type in param_types:
                if param_type.find('<') > 0:  # 以第1个<为界，左边的为类型名称
                    if param_type.split('<')[0] in params_dict.keys():  # 类型已经存在类型列表中，则在参数字典中，汇总同类型的参数名，到同一个类型的Value里
                        params_dict[param_type.split('<')[0]] = params_dict[param_type.split('<')[0]] + '/' + \
                                                                params_dict[
                                                                    param_type]
                    else:
                        params_dict.update({param_type.split('<')[0]: params_dict[param_type]})  # 类型不在列表中，直接添加进参数字典
                    if param_type.split('<')[0] not in param_types:  # 更新类型列表
                        param_types.append(param_type.split('<')[0])
                    param_types.remove(param_type)
            # 将String类型放到列表的最后去，以便构造里落到Else分支里
            if 'String' in param_types:
                param_types.remove('String')
                param_types.append('String')
            # 逐类型地添加
            if len(param_types) > 1:
                for i in range(len(param_types)):
                    if i == 0:
                        file_handle.writelines([space(16) + "if key in {param_name}:".format(
                            param_name=params_dict[param_types[i]].split('/')) + '\n',
                                                space(20) + ParamAnalysiser().formate_params(project_name=project_name,
                                                                                             param_type=param_types[i],
                                                                                             interface_name=interface_name) + '\n'])
                    elif i < len(param_types) - 1:
                        file_handle.writelines([space(16) + "elif key in {param_name}:".format(
                            param_name=params_dict[param_types[i]].split('/')) + '\n',
                                                space(20) + ParamAnalysiser().formate_params(project_name=project_name,
                                                                                             param_type=param_types[i],
                                                                                             interface_name=interface_name) + '\n'])
                    else:
                        file_handle.writelines([space(16) + "else:\n",
                                                space(20) + ParamAnalysiser().formate_params(project_name=project_name,
                                                                                             param_type=param_types[i],
                                                                                             interface_name=interface_name) + '\n'])
            else:
                file_handle.write(
                    space(16) + ParamAnalysiser().formate_params(project_name=project_name,
                                                                 param_type=param_types[0],
                                                                 interface_name=interface_name) + '\n')
        # 写入return语句
        file_handle.write(space(8) + "return params\n")
        # 补上空行
        file_handle.write("\n")

    def add_request_fun(self, file_handle, project_name: str = None, interface_name: str = None, method: str = None):
        """
        根据模板生成接口的请求方法
        :param project_name: 接口的工程名
        :param interface_name: 接口名称，为解析接口文件做准备
        :param file_handle: 文件操作对象
        :param method:  方法名
        :return:
        """
        # 注释方法需要的参数信息，以便在实现用例过程中，可以脱离API文档
        params_dict = ParamAnalysiser().get_params(project_name=project_name, interface_name=interface_name,
                                                   method_name=method)
        # 定义
        file_handle.writelines(
            [space(4) + "def {method_name}(self, params: str = None):\n".format(method_name=method),
             space(8) + '"""\n',
             space(8) + "# TODO 相应的测试用例待调试\n"])
        # 根据方法的参数列表，添加参数注释
        for param_type, param_names in params_dict.items():
            if param_type != '@NonNull':
                for param_name in list(param_names.split('/')):
                    if '@NonNull' in params_dict.keys() and param_name in params_dict['@NonNull'].split('/'):
                        file_handle.write(
                            space(8) + ":param: {param_type} {param_name} @NonNull(非空)\n".format(
                                param_type=param_type,
                                param_name=param_name))
                    else:
                        file_handle.write(
                            space(8) + ":param: {param_type} {param_name}\n".format(param_type=param_type,
                                                                                    param_name=param_name))
        # 请求发起的方法体
        file_handle.writelines(
            [space(8) + '"""\n',
             space(8) + "print('\\n%s【{method}】【请求参数】%s' % (DateTimeTool.getNowTime(), params))\n".format(
                 method=method),
             space(
                 8) + "result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,\n",
             space(
                 8) + "                                              requestMethod=self._method_{method},\n".format(
                 method=method),
             space(8) + "                                              params=params)\n",
             space(8) + "print('%s【{method}】【响应信息】%s' % (DateTimeTool.getNowTime(), result))\n".format(
                 method=method),
             space(8) + "return result\n"])
        # 补上空行
        file_handle.writelines(["\n"])

        # 生成用例脚本文件
        self.add_case_file(project_name=project_name, interface_name=interface_name, method=method,
                           params_dict=params_dict)

    def add_case_file(self, project_name: str = None, interface_name: str = None, method: str = None,
                      params_dict=None):
        """
        按规范生成用例脚本文件
        :param project_name: 项目名称
        :param interface_name: 接口名称
        :param method: 方法名称
        :param params_dict: 参数列表
        :return:
        """
        if params_dict is None:
            params_dict = {}
        file_name = 'test_' + interface_name.split('.')[-1] + '_' + method
        # 检查文件是否已经存在，不存在则创建
        if self.check_dir(self.root_path + 'case/' + project_name.replace('-', '_')):
            with open(self.root_path + 'case/' + project_name.replace('-', '_') + '/' + file_name + '.py', mode='w+',
                      encoding='utf-8') as file_handle:
                # 写入标准文件头
                self.add_case_file_header(file_handle)
                self.add_case_file_datas(file_handle, project_name=project_name.replace('-', '_').replace('-', '_'),
                                         interface_name=interface_name.split('.')[-1],
                                         method=method, params_dict=params_dict)

    def add_case_file_datas(self, file_handle, project_name: str = None, interface_name: str = None, method: str = None,
                            params_dict=None):
        """
        填写用例文件内容
        :param file_handle: 文件操作句柄
        :param project_name: 项目名
        :param interface_name: 接口名
        :param method: 方法名
        :param params_dict: 参数字典（类型 参数名1/参数名2）
        :return: 无
        """
        if params_dict is None:
            params_dict = {}
        # 构造过程需要参数名列表
        params_names = []
        for param_name in params_dict.values():
            if param_name.find('/') < 0:
                params_names.append(param_name)
            else:
                for p_name in param_name.split('/'):
                    params_names.append(p_name)
        tmp = params_names
        params_names = list(set(params_names))
        params_names.sort(key=tmp.index)
        # 引入接口定义
        file_handle.writelines(
            ['from common_projects.api.ztjy.dubbo.{project_name}.{interface_name} import {interface_name}\n'.format(
                project_name=project_name, interface_name=interface_name),
                '\n\n'])
        # 初始化测试数据
        if len(params_names) == 1:
            file_handle.write("{params} = ''\n\n".format(params="= ''\n".join([p for p in params_names])))
        if len(params_names) >= 2:
            # 写入结对法参数构造方法
            # self.add_allpaire_fun(file_handle, params_dict=params_dict)
            file_handle.writelines(['from common.paramListTool import ParamListTool\n\n'])
            file_handle.write("{params} = ''\n\n".format(params="= ''\n".join([p for p in params_names])))
            file_handle.write("param_data=[\n")
            file_handle.write(space(8) + "['ignore', None, ''] , #%s\n" % params_names[0])
            for i in range(len(params_names[1:])):
                file_handle.write(space(8) + "['ignore', None, ''], #%s\n" % params_names[i + 1])
            file_handle.write(space(4) + "]\n")
            file_handle.write("defalut_data_list=[{params}]\n\n".format(params=', '.join([p for p in params_names])))
        # 写入用例负责人
        file_handle.write("@allure.description('负责人：杨百花')\n")
        # 写入测试类定义
        file_handle.writelines(
            ['class Test_{interface_name}_{method}(object):\n'.format(interface_name=interface_name, method=method),
             space(4) + 'def setup_class(self):\n',
             space(8) + 'self._{interface_name1} = {interface_name2}()\n'.format(
                 interface_name1=interface_name.lower(), interface_name2=interface_name),
             '\n'])
        # 写入测试用例主体
        caller_params = []
        for param_name in params_names:
            caller_params.append(param_name + '=' + param_name)
        try:
            if params_names and len(params_names) < 2:
                file_handle.write(space(4) + "@pytest.mark.parametrize('{param_name}', ('ignore', None, '',))\n".format(
                    param_name=params_names[0]))
            elif len(params_names) > 1:
                file_handle.write(space(
                    4) + "@pytest.mark.parametrize('{param_name}', [test_datas for test_datas in ParamListTool.generator_input_params(defalut_data_list, param_data)])\n".format(
                    param_name=', '.join(params_names)))
            else:
                1
        except Exception as e:
            print("*" * 80)
            print(e.__str__())
            print('方法参数异常 %s - %s' % (interface_name, method))
            print("*" * 80)
        if len(params_names) == 0:
            file_handle.writelines([space(4) + 'def test_{interface_name}_{method}_success(self):\n'.format(
                interface_name=interface_name, method=method),
                                    space(8) + 'result = self._{interface_name}.{method}()\n'.format(
                                        interface_name=interface_name.lower(), method=method),
                                    space(8) + '# TODO 断言逻辑待完善\n',
                                    space(8) + 'assert_that(result).is_not_none()\n',
                                    '\n'])
        else:
            file_handle.writelines(
                [space(4) + 'def test_{interface_name}_{method}_check_params(self, {param_name}):\n'.format(
                    interface_name=interface_name, method=method, param_name=', '.join(params_names)),
                 space(8) + 'params = self._{interface_name}.generator_params({params})\n'.format(
                     interface_name=interface_name.lower(), params=', '.join([p + '=' + p for p in params_names])),
                 space(8) + 'try:\n',
                 space(12) + 'result = self._{interface_name}.{method}(params=params)\n'.format(
                     interface_name=interface_name.lower(), method=method),
                 space(8) + 'except Exception as e:\n',
                 space(12) + 'print("*" * 80)\n',
                 space(12) + 'print(e.__str__())\n',
                 space(12) + 'print("*" * 80)\n',
                 space(12) + '# TODO 断言逻辑待完善\n',
                 space(12) + 'if {param_name} '.format(
                     param_name=' == "ignore" or '.join(p for p in params_names)) + '== "ignore":\n',
                 space(16) + 'assert_that(e.__str__()).contains("NoSuchMethodException")\n',
                 space(12) + 'else:\n',
                 space(16) + 'assert_that(e.__str__()).contains("NullPointerException")\n',
                 space(8) + 'else:\n',
                 space(12) + '# TODO 断言逻辑待完善\n',
                 space(12) + 'assert_that(result).is_not_none()\n',
                 '\n'])

            file_handle.writelines(
                [space(4) + 'def test_{interface_name}_{method}_success(self):\n'.format(
                    interface_name=interface_name, method=method),
                 space(8) + 'params = self._{interface_name}.generator_params({params})\n'.format(
                     interface_name=interface_name.lower(), params=', '.join([p + '=' + p for p in params_names])),
                 space(8) + 'result = self._{interface_name}.{method}(params=params)\n'.format(
                     interface_name=interface_name.lower(), method=method),
                 space(8) + '# TODO 断言逻辑待完善\n',
                 space(8) + 'assert_that(result).is_not_none()\n',
                 '\n'])

    def add_allpaire_fun(self, file_handle, params_dict):
        """
        根据参数字典，构造结对测试参数构造方法
        :param file_handle: 文件操作句柄
        :param params_dict: 参数字典
        :return: 无
        """
        file_handle.writelines(["param_data = [\n"])
        # 逐个参数写入
        for param_type, param_names in params_dict.items():
            if param_type != '@NonNull':
                for param_name in list(param_names.split('/')):
                    file_handle.write(
                        space(8) + "['ignore', None, '', '{param_name}', '{p}' * 11],  # {param_name}\n".format(
                            param_name=param_name.upper(), p=param_name[0:2].upper()))
        file_handle.writelines([space(4) + "]\n"])

    def add_case_file_header(self, file_handle):
        """
        填写用例文件的文件头
        :param file_handle: 文件操作句柄
        :return: 无
        """
        file_handle.writelines(['# -\\*- coding:utf8 -\\*-\n',
                                '# * @Description:.\n',
                                '# * @Author  :yangbh.\n',
                                '# * @Department:研发-测试.\n',
                                '# * CreateUser: RPCCreater\n',
                                '# TODO 用例模板生成后，需要人工调试，直到用例达到足够的覆盖率，并能全部测试通过\n',
                                '\n',
                                'import allure\n',
                                'import pytest\n',
                                'from assertpy import assert_that\n',
                                '\n'])


class ParamAnalysiser(object):
    def __init__(self):
        # 定义解析的JAVA接口定义文档根目录。找开发索取：facade目录下的接口定义文档，在该目录下建文件夹放
        self.facade_root = 'test_data/tools/rpc_creater/'

    def get_params(self, project_name: str = None, interface_name: str = None, method_name: str = None):
        """
        解析开发提供的JAVA类定义文件，确定入参类型及字段名
        :param project_name: 接口的工程名
        :param interface_name: 接口名
        :param method_name: 方法名
        :return: 以字典的方式，返回方法的入参列表  类型：参数名1/参数名2/参数名3
        """
        # 定义正则匹配表达式，Method_name为空时，提取出全部的方法名（参数名）列表；指定Method_name时，返回指定方法的参数列表
        if method_name is None:
            regex_expression = r'[a-zA-Z0-9]+\([a-zA-Z<> ,@].*?\)'
        else:
            regex_expression = r'{method_name}\([a-zA-Z<> ,@].*?\)'.format(method_name=method_name)
        regex_params = re.compile(regex_expression)
        # 接收聚合参数列表的集合
        params_dict = {}
        # 解析接口文档
        with open(file=self.facade_root + '{project_name}/{interface_name}.java'.format(
                project_name=project_name,
                interface_name=interface_name.split('.')[-1]), mode='r', encoding='utf-8') as ff:
            method_params_list = regex_params.findall(ff.read())  # 遍历接口文档里的全部参数，进行聚合
            for method_params in method_params_list:
                if method_params.find('(') - method_params.find(')') != -1:  # 如果只有括号，则表示为空入参，进行特殊处理
                    params = method_params[method_params.find('(') + 1:method_params.find(')')]  # 截取（）内的信息
                    params = params.split(',')  # 多个参数拆分成List
                    for param in params:
                        param = param.strip()  # 去除参数前后的空格
                        param = param.split(' ')  # 按空格拆分参数的各个字段  拆分成列表后，[非空标识，参数类型，参数名]
                        if param[0] == '@NonNull':  # 非空字段处理。汇总登记到参数字典中的非空字段里
                            if '@NonNull' not in params_dict.keys():
                                params_dict.update(
                                    {'@NonNull': param[2].strip()})  # 在返回字典中，添加非空的参数信息。{'@NonNull': 参数名称}
                            else:
                                params_dict.update(
                                    {'@NonNull': params_dict['@NonNull'] + '/' + param[2].strip()})  # 汇总非空字段
                            param = [param[1], param[2]]  # 去除非空标记，进行后续统一处理
                        param[0] = param[0].strip()  # 参数类型，去除前后空格
                        param[1] = param[1].strip()  # 参数名称，去除前后空格
                        if param[0] in params_dict.keys():
                            if param[1] not in params_dict[param[0]].split('/'):
                                params_dict[param[0]] = params_dict[param[0]] + '/' + param[1]
                        else:
                            params_dict.update({param[0]: param[1]})
        return params_dict

    def get_special_type_full_name(self, project_name: str = None, interface_name: str = None, param_type: str = None):
        # 构造正则匹配表达式
        regex_expression = 'com[a-zA-Z.]+?{type_name}'.format(type_name=param_type)
        regex_special_type = re.compile(regex_expression)
        # 解析接口文档
        with open(file=self.facade_root + '{project_name}/{interface_name}.java'.format(
                project_name=project_name,
                interface_name=interface_name.split('.')[-1]),
                  mode='r', encoding='utf-8') as ff:
            type_full_name = regex_special_type.findall(ff.read())
            if len(type_full_name) == 0:
                # 构造正则匹配表达式
                regex_special_type = re.compile(r'com[a-zA-Z.]+?model\.\*')
                # 重新解析接口文档
                with open(
                        file=self.facade_root + '{project_name}/{interface_name}.java'.format(
                            project_name=project_name,
                            interface_name=interface_name.split('.')[-1]),
                        mode='r', encoding='utf-8') as fff:
                    type_full_name = regex_special_type.findall(fff.read())
                    if len(type_full_name) == 0:  # 易出错的地方，打个日志便于排查
                        print("自定义参数类型未找到>>" + interface_name + '>>' + param_type)
                    type_full_name[0] = type_full_name[0][:-1] + param_type
            elif len(type_full_name) > 1:
                remove_name = None
                for i in type_full_name:
                    if i.split('.')[-1] != param_type:
                        remove_name = i
                if remove_name:
                    type_full_name.remove(remove_name)
                # print(type_full_name[0])
                # print("接口文档里，异常>>" + interface_name + ">>" + param_type)
            else:
                pass
        return type_full_name[0]

    def formate_params(self, project_name: str = None, interface_name: str = None, param_type: str = None):
        """
        格式化参数，基础类型的，直接在IF里处理，DTO、枚举等自定义类型，通过特殊类型处理进行返回
        :param project_name: 接口所在项目名
        :param interface_name: 接口名
        :param param_type: 参数类型
        :return:
        """
        if param_type == 'String':
            param = "params.append({\"type\": \"java.lang.String\", \"data\": value})"
        elif param_type == 'String...':
            param = "params.append({\"type\": \"java.lang.String\", \"data\": value})  # String...类型"
        elif param_type == 'Byte':
            param = "params.append({\"type\": \"java.lang.Byte\", \"data\": value})"
        elif param_type == 'Long':
            param = "params.append({\"type\": \"java.lang.Long\", \"data\": value})"
        elif param_type == 'int':
            param = "params.append({\"type\": \"java.lang.int\", \"data\": value})"
        elif param_type == 'Integer':
            param = "params.append({\"type\": \"java.lang.Integer\", \"data\": value})"
        elif param_type == 'BigInteger':
            param = "params.append({\"type\": \"java.math.BigInteger\", \"data\": value})"
        elif param_type == 'Short':
            param = "params.append({\"type\": \"java.lang.Short\", \"data\": value})"
        elif param_type in ['Boolean', 'boolean']:
            param = "params.append({\"type\": \"boolean\", \"data\": value})"
        elif param_type.startswith('Page'):
            param = "params.append({\"type\": \"com.ztjy.common.model.Page\", \"data\": value})"
        elif param_type.startswith('List'):
            param = "params.append({\"type\": \"java.util.List\", \"data\": value})"
        elif param_type.startswith('Set'):
            param = "params.append({\"type\": \"java.util.Set\", \"data\": value})"
        elif param_type.startswith('Map'):
            param = "params.append({\"type\": \"java.util.Map\", \"data\": value})"
        elif param_type.startswith('Collection'):
            param = "params.append({\"type\": \"java.util.Collection\", \"data\": value})"
        elif param_type.startswith('Date'):
            param = "params.append({\"type\": \"java.util.Date\", \"data\": value})"
        else:
            full_type = self.get_special_type_full_name(project_name=project_name, interface_name=interface_name,
                                                        param_type=param_type)
            param = "params.append({\"type\": \"" + full_type + "\", \"data\": value})"
        return param
