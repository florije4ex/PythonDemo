# @File    : school_batch_remove_student
# @Description: 园丁端学生管理批量移出学校
# @Author  : yangbaihua
# @Time    : 2020/6/24 16:24

#  http://api.szy.net/index.do#/ffff-1525939408316-1011079-0006/front/interfaceDetail/ffff-1527145391741-1011079-0202
import ujson

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class SchoolBatchRemoveStudent():
    def __init__(self):
        self.get_config_path = '/school/student/batchremove/v1.0'
        self.get_config_content_type = {'Content-Type': 'application/json'}
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.teacher_login = self.ztjy_client.teacher_login
        self.teacher_login.updateHeaders(self.get_config_content_type)

    def generator_school_batch_remove_student_params(self, classIds, students, **kwargs):
        """
        :param classIds:
        :param students:
        :return:
        """
        params = {}
        if not classIds is None:
            params.update({'classIds': classIds})
        if not students is None:
            params.update({'studentIds': students})
        params.update(**kwargs)
        return ujson.dumps(params)

    def school_batch_remove_student(self, params: dict = None):
        print('%s【school_batch_remove_student】【请求path】:%s' % (DateTimeTool.getNowTime(), self.get_config_path))
        print('%s【school_batch_remove_student】【请求头】:%s' % (
            DateTimeTool.getNowTime(), ujson.dumps(self.teacher_login.getHeaders())))
        print('%s【school_batch_remove_student】【请求参数】:%s' % (DateTimeTool.getNowTime(), params))
        httpResponseResult = self.teacher_login.post_with_form(path=self.get_config_path, params=params)
        print('%s【school_batch_remove_student】【响应信息】:%s' % (DateTimeTool.getNowTime(), httpResponseResult.body))
        print('%s【school_batch_remove_student】【当前cookies】:%s' % (
            DateTimeTool.getNowTime(), ujson.dumps(self.teacher_login.getCookies())))
        return httpResponseResult
