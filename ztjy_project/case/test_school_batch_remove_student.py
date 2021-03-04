# @File    : test_school_batch_remove_student
# @Author  : yangbaihua
# @Time    : 2020/6/24 16:33
import allure
import pytest
import ujson
from assertpy import assert_that

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common_projects.api.ztjy.http.zthServer.school_batch_remove_student import SchoolBatchRemoveStudent
from common_projects.api.ztjy.http.zthServer.school_batch_rest_student import SchoolBatchRestStudent


@allure.description('负责人:杨百花')
class TestSchoolBatchRemoveStudent:
    def setup_class(self):
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.schoolBatchRemoveStudent = SchoolBatchRemoveStudent()
        self.schoolBatchRestStudent = SchoolBatchRestStudent()

    @pytest.fixture()
    def fixture_init_data(self):
        self.classId = 'a3a6e72514c72a491d95'
        self.studentId = '4a41b584f41b78b77d31'
        self.classIds = self.schoolBatchGraduate.generator_set_params(self.classId)
        self.studentIds = self.schoolBatchGraduate.generator_set_params(self.studentId)

    def test_one_class_and_student_school_batch_remove_student(self):
        classIds = ['228bba4678867a2ad6aa']
        students = ['a1911423b96f06b2b5c9']
        targetGradeId = 'l4EEpp8aVbonrjIn28b'

        params = self.schoolBatchRemoveStudent.generator_school_batch_remove_student_params(classIds, students)
        httpResponseResult = self.schoolBatchRemoveStudent.school_batch_remove_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['returncode']).is_equal_to(10000)
        assert_that(body['message']).is_equal_to("成功")

        restParams = self.schoolBatchRestStudent.generator_school_batch_rest_student_params(2, classIds, None,
                                                                                            classIds[0],
                                                                                            targetGradeId)
        self.schoolBatchRestStudent.school_batch_rest_student(params=restParams)  # 还原
