# @File    : school_sns_database_operation
# @Description: 数据库查询学生相关信息
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/11 15:21
from common_projects.mysqlOpt.ztjy_mysql.db_school.t_class_members_db import ClassMembers_DB
from common_projects.mysqlOpt.ztjy_mysql.db_school.t_family_members_db import FamilyMembers_DB
from common_projects.mysqlOpt.ztjy_mysql.db_school.t_register_student_verify_db import Register_Student_Verify_DB
from common_projects.mysqlOpt.ztjy_mysql.db_school.t_student_db import School_Student_DB


class School_Sns_DB_Operation:
    def __init__(self):
        self.family_members_DB = FamilyMembers_DB()
        self.student_DB = School_Student_DB()
        self.classMember_DB = ClassMembers_DB()
        self.register_Student_Verify_DB = Register_Student_Verify_DB()

    def db_get_child_register_verify(self, verifyId: str = None):
        studentVerifyInfo = {}
        schoolInfoResult = self.register_Student_Verify_DB.select_sql(id=verifyId, is_flag=1)
        if schoolInfoResult:
            studentVerifyInfo.update({'schoolId': schoolInfoResult[0]['school_id']})
            studentVerifyInfo.update({'studentId': schoolInfoResult[0]['student_id']})
            studentVerifyInfo.update({'classId': schoolInfoResult[0]['class_id']})
            studentVerifyInfo.update({'childId': schoolInfoResult[0]['baby_id']})
        return studentVerifyInfo

    def db_get_school_sns_info(self, studentId: str = None, userId: str = None):
        studentSnsInfo = {}
        classMemberInfo = {}
        studentSnsInfo.update({'studentId': studentId})
        studentSnsInfo.update({'familyMembersStatus': None})
        studentSnsInfo.update({'StudentStatus': None})  # 表数据为空
        studentInfoResult = self.student_DB.select_sql(studentId=studentId)
        classMemberInfoResult = self.classMember_DB.select_sql(USERID=studentId)
        if classMemberInfoResult:
            classMemberInfo.update({'classId': classMemberInfoResult[0]['CLASSID']})
            classMemberInfo.update({'schoolId': classMemberInfoResult[0]['SCHOOL_ID']})
            classMemberInfo.update({'userType': classMemberInfoResult[0]['USER_TYPE']})
            classMemberInfo.update({'userState': classMemberInfoResult[0]['USER_STATE']})
            classMemberInfo.update({'isFlag': classMemberInfoResult[0]['IS_FLAG']})
            classMemberInfo.update({'features': classMemberInfoResult[0]['FEATURES']})
        if studentInfoResult:
            studentSnsInfo.update({'StudentStatus': True})  # 表数据为空
            studentSnsInfo.update({'childId': studentInfoResult[0]['CHILD_ID']})  # 表数据为空
            studentSnsInfo.update({'schoolId': studentInfoResult[0]['SCHOOL_ID']})  # 表数据为空
            studentSnsInfo.update({'classId': studentInfoResult[0]['CLASS_ID']})  # 表数据为空
            studentSnsInfo.update({'userState': studentInfoResult[0]['USER_STATE']})  # 表数据为空
            studentSnsInfo.update({'isFlag': studentInfoResult[0]['IS_FLAG']})  # 表数据为空
            studentSnsInfo.update({'isConfirm': studentInfoResult[0]['IS_CONFIRM']})  # 表数据为空

        if userId is None:
            studentSqlResult = self.family_members_DB.select_sql(CHILD_ID=studentId, IS_VALIDITY=1)
        else:
            studentSqlResult = self.family_members_DB.select_sql(CHILD_ID=studentId, user_id=userId, IS_VALIDITY=1)
        if studentSqlResult:
            studentSnsInfo.update({'familyMembersStatus': True})  # 表数据查询成功
            studentSnsInfo.update({'membersNum': len(studentSqlResult)})
            members = []
            for i in studentSqlResult:
                member = {}
                member.update({'schoolSnsId': i['ID']})
                member.update({'userId': i['USER_ID']})
                member.update({'familyName': i['RELATION_CODE']})
                members.append(member)
            studentSnsInfo.update({'schoolSnsMembers': members})
        studentSnsInfo.update({'classMemberInfo': classMemberInfo})  # 表数据为空
        print(studentSnsInfo)
        return studentSnsInfo
