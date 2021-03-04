# @File    : school_batch_rest_student
# @Author  : yangbaihua
# @Time    : 2020/6/24 16:50
# 园丁端学生管理毕业/移出批量还原学生 API没有录入 #Todo
import ujson

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class SchoolBatchRestStudent():
    def __init__(self):
        self.get_config_path = '/school/student/batchrest/v2.0'
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

    def geneartor_params(self,type, classIds, students, targetClassId, targetGradeId, **kwargs):
        """
                :param type:类型 1-毕业还原 2-移出还原
                :param classIds:
                :param students:
                :param targetClassId:
                :param targetGradeId:
                :param kwargs:
                :return:
                """
        params = {}
        if not type is None:
            params.update({'type': type})
        if not classIds is None:
            params.update({'classIds': classIds})
        if not students is None:
            params.update({'studentIds': students})
        if not targetClassId is None:
            params.update({'targetClassId': targetClassId})
        if not targetGradeId is None:
            params.update({'targetGradeId': targetGradeId})
        params.update(**kwargs)
        return ujson.dumps(params)

    def generator_school_batch_rest_student_params(self, type, classIds, students, targetClassId, targetGradeId,
                                                   **kwargs):
        """
        :param type:类型 1-毕业还原 2-移出还原
        :param classIds:
        :param students:
        :param targetClassId:
        :param targetGradeId:
        :param kwargs:
        :return:
        """
        params = {}
        if not type is None:
            params.update({'type': type})
        if not classIds is None:
            params.update({'classIds': classIds})
        if not students is None:
            params.update({'studentIds': students})
        if not targetClassId is None:
            params.update({'targetClassId': targetClassId})
        if not targetGradeId is None:
            params.update({'targetGradeId': targetGradeId})
        params.update(**kwargs)
        return ujson.dumps(params)

    def school_batch_rest_student(self, params: dict = None):
        print('%s【school_batch_rest_student】【请求path】:%s' % (DateTimeTool.getNowTime(), self.get_config_path))
        print('%s【school_batch_rest_student】【请求头】:%s' % (
            DateTimeTool.getNowTime(), ujson.dumps(self.teacher_login.getHeaders())))
        print('%s【school_batch_rest_student】【请求参数】:%s' % (DateTimeTool.getNowTime(), params))
        httpResponseResult = self.teacher_login.post_with_form(path=self.get_config_path, params=params)
        print('%s【school_batch_rest_student】【响应信息】:%s' % (DateTimeTool.getNowTime(), httpResponseResult.body))
        print('%s【school_batch_rest_student】【当前cookies】:%s' % (
            DateTimeTool.getNowTime(), ujson.dumps(self.teacher_login.getCookies())))
        return httpResponseResult
