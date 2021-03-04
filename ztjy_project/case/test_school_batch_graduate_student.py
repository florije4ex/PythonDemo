# @File    : test_school_batch_graduate_student
# @Description: 园丁端学生管理批量毕业学生
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/22 16:38
import pytest
import ujson
from assertpy import assert_that

from common_projects.api.ztjy.http.zthServer.school_batch_graduate_student import SchoolBatchGraduate


class TestSchoolBatchGraduate:
    def setup_class(self):
        self.schoolBatchGraduate = SchoolBatchGraduate()

    @pytest.fixture()
    def fixture_init_data(self):
        self.classId = 'a3a6e72514c72a491d95'
        self.studentId = '4a41b584f41b78b77d31'
        self.classIds = self.schoolBatchGraduate.generator_set_params(self.classId)
        self.studentIds = self.schoolBatchGraduate.generator_set_params(self.studentId)

    def test_school_batch_graduate_student(self,fixture_init_data):
        params = self.schoolBatchGraduate.generator_params(classIds=self.classIds,studentIds=self.studentIds)
        httpResponseResult = self.schoolBatchGraduate.school_batch_graduate_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['code']).is_equal_to(10000)