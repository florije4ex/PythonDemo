# @File    : test_school_batch_rest_student
# @Author  : yangbaihua
# @Time    : 2020/6/24 16:54
import allure
import pytest
import ujson
from allpairspy import AllPairs
from assertpy import assert_that

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.strTool import StrTool
from common_projects.api.ztjy.http.zthServer.school_batch_graduate_student import SchoolBatchGraduate
from common_projects.api.ztjy.http.zthServer.school_batch_rest_student import SchoolBatchRestStudent
from common_projects.mysqlOpt.ztjy_mysql.db_school.school_sns_db_operation import School_Sns_DB_Operation


def randomValue(len):
    return 'TestUserId%s' % StrTool.getRandomText(len, 0, 100, 0, 0, 0)


def pairs_datas():
    param_data = [
        [1, 2],  # type
        ['f2ce257f4d7595801adf', '76eaae1cea4b9897e6ba'],  # classId
        ['fb600fba48f4a1462957', '48734923e22c435b8afa'],  # student
        ['ignore', None, '', 'A' * 21, randomValue(10)],  # targetGradeId
        ['ignore', None, '', 'A' * 21, randomValue(10)],  # targetClassId
    ]
    return AllPairs(param_data)


bueness_data = [
    (),
    (),
    (),
]


@allure.description('负责人:杨百花')
class TestSchoolBatchRestStudent:
    type = ['ignore', None, '', 0, 1, 2]  # type
    classId = ['ignore', 'ignoreSet', None, '', 'A' * 21, randomValue(10)]  # classId
    studentId = ['ignore', 'ignoreSet', None, '', 'A' * 21, randomValue(10)]  # studentId
    targetGradeId = ['ignore', None, '', 'A' * 21, randomValue(10)]  # targetGradeId
    targetClassId = ['ignore', None, '', 'A' * 21, randomValue(10)]  # targetClassId

    def setup_class(self):
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.schoolBatchRestStudent = SchoolBatchRestStudent()

    @pytest.fixture()
    def fixture_init_data(self):
        self.type = 1
        self.classId = 'a3a6e72514c72a491d95'
        self.studentId = '4a41b584f41b78b77d31'
        self.targetGradeId = '11YcjPsdT3YxNZwh7gL'
        self.targetClassId = 'a3a6e72514c72a491d95'
        self.classIds = self.schoolBatchRestStudent.generator_set_params(self.classId)
        self.studentIds = self.schoolBatchRestStudent.generator_set_params(self.studentId)

    def test_school_rest_the_graduate_student_success(self, fixture_init_data):
        #学生毕业
        SchoolBatchGraduate().school_batch_graduate_student(
            SchoolBatchGraduate().generator_params(classIds=self.classIds, studentIds=self.studentIds))
        studentInfo1 = School_Sns_DB_Operation().db_get_school_sns_info(studentId=self.studentId)
        # 获取学生状态 不在读
        studentStatus1 = studentInfo1['userState']
        params = self.schoolBatchRestStudent.geneartor_params(self.type, self.classIds, self.studentIds,
                                                              self.targetClassId,
                                                              self.targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        # 学生恢复后，获取学生状态  在读
        studentInfo2 = School_Sns_DB_Operation().db_get_school_sns_info(studentId=self.studentId)
        studentStatus2 = studentInfo2['userState']
        assert_that(body['code']).is_equal_to(10000)
        assert_that(body['message']).is_equal_to('成功')
        assert_that(body['body']).is_equal_to({})
        assert_that(studentStatus1).is_equal_to('NO_READ')
        assert_that(studentStatus2).is_equal_to('IN_READ')

    def test_school_rest_the_removed_student_success(self, fixture_init_data):
        #学生移除
        SchoolBatchGraduate().school_batch_graduate_student(
            SchoolBatchGraduate().generator_params(classIds=self.classIds, studentIds=self.studentIds))
        studentInfo1 = School_Sns_DB_Operation().db_get_school_sns_info(studentId=self.studentId)
        # 获取学生状态 不在读
        studentStatus1 = studentInfo1['userState']
        params = self.schoolBatchRestStudent.geneartor_params(2, self.classIds, self.studentIds,
                                                              self.targetClassId,
                                                              self.targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        # 学生恢复后，获取学生状态  在读
        studentInfo2 = School_Sns_DB_Operation().db_get_school_sns_info(studentId=self.studentId)
        studentStatus2 = studentInfo2['userState']
        assert_that(body['code']).is_equal_to(10000)
        assert_that(body['message']).is_equal_to('成功')
        assert_that(body['body']).is_equal_to({})
        assert_that(studentStatus1).is_equal_to('NO_READ')
        assert_that(studentStatus2).is_equal_to('IN_READ')

    @pytest.mark.parametrize('type', type)
    def test_school_rest_the_removed_student_check_type(self, type, fixture_init_data):
        params = self.schoolBatchRestStudent.geneartor_params(type, self.classIds, self.studentIds, self.targetClassId,
                                                              self.targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        if type == 'ignore' or type is None or type == '':
            assert_that(body['returncode']).is_equal_to('500')
            assert_that(body['message']).is_equal_to('服务器异常')
            assert_that(body['body']).is_equal_to({})
        elif type == 0:
            assert_that(body['code']).is_equal_to(500)
            assert_that(body['message']).is_equal_to('参数错误')
            assert_that(body['body']).is_equal_to({})
        else:
            assert_that(body['code']).is_equal_to(10011)
            assert_that(body['message']).is_equal_to('班级已毕业或删除!')
            assert_that(body['body']).is_equal_to({})

    @pytest.mark.parametrize('classId', classId)
    def test_school_rest_the_removed_student_check_classId(self, classId, fixture_init_data):
        classIds = self.schoolBatchRestStudent.generator_set_params(classId)
        params = self.schoolBatchRestStudent.geneartor_params(self.type, classIds, self.studentIds, self.targetClassId,
                                                              self.targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['code']).is_equal_to(10011)
        assert_that(body['message']).is_equal_to('班级已毕业或删除!')
        assert_that(body['body']).is_equal_to({})

    @pytest.mark.parametrize('studentId', studentId)
    def test_school_rest_the_removed_student_check_studentId(self, studentId, fixture_init_data):
        students = self.schoolBatchRestStudent.generator_set_params(studentId)
        params = self.schoolBatchRestStudent.geneartor_params(self.type, self.classIds, students, self.targetClassId,
                                                              self.targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['code']).is_equal_to(10011)
        assert_that(body['message']).is_equal_to('班级已毕业或删除!')
        assert_that(body['body']).is_equal_to({})

    @pytest.mark.parametrize('targetClassId', targetClassId)
    def test_school_rest_the_removed_student_check_targetClassId(self, targetClassId, fixture_init_data):
        params = self.schoolBatchRestStudent.geneartor_params(self.type, self.classIds, self.studentIds, targetClassId,
                                                              self.targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        if targetClassId is None:
            assert_that(body['returncode']).is_equal_to('500')
            assert_that(body['message']).is_equal_to('服务器异常')
            assert_that(body['body']).is_equal_to({})
        elif targetClassId == 'ignore' or len(targetClassId) >= 20:
            assert_that(body['code']).is_equal_to(10011)
            assert_that(body['message']).is_equal_to('班级已毕业或删除!')
            assert_that(body['body']).is_equal_to({})
        else:
            assert_that(body['code']).is_equal_to(10000)
            assert_that(body['message']).is_equal_to('成功')
            assert_that(body['body']).is_equal_to({})

    @pytest.mark.parametrize('targetGradeId', targetGradeId)
    def test_school_rest_the_removed_student_check_targetGradeId(self, targetGradeId, fixture_init_data):
        params = self.schoolBatchRestStudent.geneartor_params(self.type, self.classIds, self.studentIds,
                                                              self.targetClassId,
                                                              targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['code']).is_equal_to(10011)
        assert_that(body['message']).is_equal_to('班级已毕业或删除!')
        assert_that(body['body']).is_equal_to({})

    def test_school_rest_the_removed_student_with_single_class_by_teacher(self):
        classIds = ['228bba4678867a2ad6aa']
        students = ['a1911423b96f06b2b5c9']
        targetGradeId = 'l4EEpp8aVbonrjIn28b'

        params = self.schoolBatchRestStudent.generator_school_batch_rest_student_params(2, classIds, None, classIds[0],
                                                                                        targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['code']).is_equal_to(10000)
        assert_that(body['message']).is_equal_to("成功")

    def test_school_rest_the_graduated_student_with_single_class_by_teacher(self):
        classIds = ['228bba4678867a2ad6aa']
        students = ['a1911423b96f06b2b5c9']
        targetGradeId = 'l4EEpp8aVbonrjIn28b'
        params = self.schoolBatchRestStudent.generator_school_batch_rest_student_params(1, classIds, None, classIds[0],
                                                                                        targetGradeId)
        httpResponseResult = self.schoolBatchRestStudent.school_batch_rest_student(params=params)
        body = ujson.loads(httpResponseResult.body)
        assert_that(body['code']).is_equal_to(10000)
        assert_that(body['message']).is_equal_to("成功")
