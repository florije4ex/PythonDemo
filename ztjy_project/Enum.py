# @File    : Enum
# @Description:
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/17 16:51

def fixture_userType_enum():
    """
    用户类型枚举
    :return:
    """
    code_lookup = {'STUDENT': 0, 'PARENT': 1, 'TEACHER': 2, 'DRIVER': 3, 'INSTITUTION': 4, 'CONSOLE': 5,
                   'FICTITIOUS': 6, 'SCHOOL_SNS': 7}
    return code_lookup

def fixture_officeType_enum():
    """
    组织类型枚举
    :return:
    """
    code_lookup = {'HEAD': 1, 'AGENT': 2, 'AGENT_INSIDE': 3, 'SCHOOL': 4, 'SCHOOL_INSIDE': 5,
                   'EDUCATION': 6, 'EDUCATION_INSIDE': 7,'FAMILY':8}
    return code_lookup

if __name__ == '__main__':
    userType = fixture_userType_enum()['STUDENT']
    print(userType)