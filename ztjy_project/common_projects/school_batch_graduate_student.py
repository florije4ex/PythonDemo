# @File    : school_batch_graduate_student
# @Description: 园丁端学生管理批量毕业学生
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/22 16:31

# http://api.szy.net/index.do#/ffff-1525939408316-1011079-0006/front/interfaceDetail/ffff-1527146478032-1011079-0207
import ujson

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class SchoolBatchGraduate:
    def __init__(self):
        self.get_config_path = '/school/student/batchgraduate/v1.0'
        self.get_config_content_type = {'Content-Type': 'application/json'}
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.teacher_login = self.ztjy_client.teacher_login
        self.teacher_login.updateHeaders(self.get_config_content_type)

    def generator_set_params(self, *args):
        dataSet = []
        dataSet.append(*args)
        if args == 'ignore':
            dataSet.pop(args)
        if args == 'ignoreSet':
            dataSet == None
        return dataSet

    def generator_params(self,classIds,studentIds,**kwargs):
        """
        :param classIds: 班级ids（全部选中）
        :param studentIds: 学生ids
        :return:
        """
        params = {}
        if not classIds is None:
            params.update({'classIds': classIds})
        if not studentIds is None:
            params.update({'studentIds': studentIds})
        params.update(**kwargs)
        return ujson.dumps(params)

    def school_batch_graduate_student(self, params: dict = None):
        print('%s【school_batch_graduate_student】【请求path】:%s' % (DateTimeTool.getNowTime(), self.get_config_path))
        print('%s【school_batch_graduate_student】【请求头】:%s' % (
            DateTimeTool.getNowTime(), ujson.dumps(self.teacher_login.getHeaders())))
        print('%s【school_batch_graduate_student】【请求参数】:%s' % (DateTimeTool.getNowTime(), params))
        httpResponseResult = self.teacher_login.post_with_form(path=self.get_config_path, params=params)
        print('%s【school_batch_graduate_student】【响应信息】:%s' % (DateTimeTool.getNowTime(), httpResponseResult.body))
        print('%s【school_batch_graduate_student】【当前cookies】:%s' % (
            DateTimeTool.getNowTime(), ujson.dumps(self.teacher_login.getCookies())))
        return httpResponseResult

