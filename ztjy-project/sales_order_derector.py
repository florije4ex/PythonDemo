# @File    : IRClassFacade
# @Author  : yangbaihua
# @Time    : 2020/6/11 13:59
# 班级信息查询接口 http://api.szy.net/user/dubboapi/apiClassDetail.do?id=ffff-1532514432990-1011079-0650
from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IRClassFacade:
    def __init__(self):
        self.interface = 'com.szy.schoolserver.openservice.facade.IRClassFacade'
        self._method_batchClassInfo = 'batchClassInfo'
        self._method_getStudentIdsByClassIds = 'getStudentIdsByClassIds'
        self._method_batchGetClassStudentByState = 'batchGetClassStudentByState'
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_dubbo_client = self.ztjy_client.dubboClient

    def generator_params(self, **kwargs):
        params = []
        for k, v in kwargs.items():
            if isinstance(v, list):
                if k == 'classIdSet':
                    if v is None:
                        params.append({"type": "java.util.Set", "data": {"type": "java.lang.String", "data": []}})
                    else:
                        dataSet = []
                        for i in v:
                            dataSet.append({"type": "java.lang.String", "data": i})
                        params.append({"type": "java.util.Set", "data": dataSet})
                if k == 'classIdList':
                    if v is None:
                        params.append({"type": "java.util.List", "data": 'null'})
                    else:
                        dataSet = []
                        for i in range(len(v)):
                            dataSet.append({"type": "java.lang.String", "data": v[i]})
                        params.append({"type": "java.util.List", "data": dataSet})
            elif k == 'isFlag':
                if v is None:
                    params.append({"type": "java.lang.Byte", "data": "null"})
                if v == '':
                    params.append({"type": "java.lang.Byte", "data": ''})
                else:
                    params.append({"type": "java.lang.Byte", "data": v})
            elif k == 'lastDate':
                params.append({"type": "java.util.Date", "data": {"format": "yyyy-MM-dd HH:mm:ss", "datetime": v}})
            else:
                if v is None:
                    params.append({"type": "java.lang.String", "data": "null"})
                if v == '':
                    params.append({"type": "java.lang.String", "data": ''})
                else:
                    params.append({"type": "java.lang.String", "data": v})
        return params

    def generator_params_classIdSet(self, classIdList):
        dataValue = '['
        for classId in classIdList:
            dataValue = dataValue + '{"type":"java.lang.String", "data":"%s"},' % classId
        dataValue = dataValue[:-1] + ']'
        return '[{"type":"java.util.Set","data":%s}]' % dataValue

    def batchClassInfo(self, params: list = None):
        """
        批量获取班级信息
        :param params:java.util.Set<java.lang.String> classIds
        :return:
        """
        print('%s【batchClassInfo】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_dubbo_client.request(requestInterfaceClassName=self.interface,
                                                requestMethod=self._method_batchClassInfo
                                                , params=params)
        print('%s【batchClassInfo】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getStudentIdsByClassIds(self, params: str = None):
        """
        根据班级Id集合获取对应每个班级的学生Id集合
        :param params:classIds
        :return:
        """
        print('%s【getStudentIdsByClassIds】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_dubbo_client.request(requestInterfaceClassName=self.interface,
                                                requestMethod=self._method_getStudentIdsByClassIds
                                                , params=params)
        print('%s【getStudentIdsByClassIds】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def batchGetClassStudentByState(self, params: dict = None):
        """java.lang.String schoolId,
        java.util.List<java.lang.String> classIds,
        java.lang.String userState,
        java.lang.Byte isFlag,
        java.util.Date lastDate
        根据学生状态,获得学生ids
        :param params: schoolId:
        :param params: classIdList:
        :param params: userState:状态
        :param params: isFlag:删除标识
        :param params: lastDate:操作最后时间
        :return:
        """
        print('%s【batchGetClassStudentByState】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_dubbo_client.request(requestInterfaceClassName=self.interface,
                                                requestMethod=self._method_batchGetClassStudentByState
                                                , params=params)
        print('%s【batchGetClassStudentByState】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result





# @File    : test_IRClassFacade_batchClassInfo
# @Author  : yangbaihua
# @Time    : 2020/6/11 15:37
import allure
import pytest
from assertpy import assert_that

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common_projects.api.ztjy.dubbo.ztjy_schoolserver_szy.IRClassFacade import IRClassFacade
from common_projects.mysqlOpt.ztjy_mysql.db_school.t_class_db import Class_DB


@allure.description('负责人:杨百花')
class Test_IRClassFacade_batchClassInfo:
    def setup_class(self):
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.iRClassFacade = IRClassFacade()

    @pytest.fixture()
    def fixture_init_data(self):
        self.schoolId = 'e338d65437fac34eb471'
        self.isFlag = 1

        #查询学校下所有的年级
        gradeIdList = []
        gradeIdListSql = Class_DB().select_sql(groupBy='GRADE_ID', isDistinct=True, deduplField="GRADE_ID",
                                               school_id=self.schoolId, IS_FLAG=self.isFlag)
        for gradeId in gradeIdListSql:
            gradeIdList.append(gradeId['GRADE_ID'])
        self.gradeIds = gradeIdList

    def fixture_get_classId_by_gradeId(self, gradeId):
        """
        查询年级下所有班级
        :param gradeId:
        :return:
        """
        classIdList = []
        classIdListSql = Class_DB().select_sql(deduplField="ID", school_id=self.schoolId, grade_id=gradeId,
                                               IS_FLAG=self.isFlag)
        for classId in classIdListSql:
            classIdList.append(classId['ID'])
        return classIdList

    def fixture_get_classInfo_by_classId(self, classId):
        """
        根据班级id查询班级记录
        :param classId:
        :return:
        """
        classInfoSql = Class_DB().select_sql(id=classId)
        return classInfoSql

    def test_batch_get_class_info_check_scene(self, fixture_init_data):
        for gradeId in self.gradeIds:
            classIds = self.fixture_get_classId_by_gradeId(gradeId)

            params = self.iRClassFacade.generator_params(classIdSet=classIds)
            result = self.iRClassFacade.batchClassInfo(params=params)
            for classId in classIds:
                classInfoSql = self.fixture_get_classInfo_by_classId(classId)
                assert_that(result).contains(classId)
                assert_that(result[classId]['gradeId']).is_equal_to(classInfoSql[0]['GRADE_ID'])
                assert_that(result[classId]['classId']).is_equal_to(classInfoSql[0]['ID'])
                assert_that(result[classId]['className']).is_equal_to(classInfoSql[0]['CLASS_NAME'])
                assert_that(result[classId]['isFlag']).is_equal_to(classInfoSql[0]['IS_FLAG'])
                if classInfoSql[0]['ENROLLMENT_YEAR'] == 0:
                    assert_that(result[classId]['enrollmentYear']).is_none()
                else:
                    assert_that(result[classId]['enrollmentYear']).is_equal_to(classInfoSql[0]['ENROLLMENT_YEAR'])
                assert_that(result[classId]['schoolId']).is_equal_to(classInfoSql[0]['SCHOOL_ID'])
                assert_that(result[classId]['schoolId']).is_equal_to(classInfoSql[0]['SCHOOL_ID'])

    def test_batch_get_class_info_with_no_class_list(self):
        classIds = [{"type": "java.util.Set", "data": []}]
        result = self.iRClassFacade.batchClassInfo(params=classIds)
        assert_that(result).is_equal_to(None)

    def test_batch_get_class_info_with_None_class(self):
        classIds = [{"type": "java.util.Set", "data": [{"type": "java.lang.String", "data": ""}]}]
        result = self.iRClassFacade.batchClassInfo(params=classIds)
        assert_that(result).is_equal_to({})

    def test_batch_get_class_info_with_sql_inject(self):
        classIds = [{"type": "java.util.Set", "data": [{"type": "java.lang.String",
                                                        "data": "zzxg1qUz7Ygp85Yg46P'+(if(ord(mid(database(),1,1))=100,'',exp(1111)))+'"}]}]
        result = self.iRClassFacade.batchClassInfo(params=classIds)
        assert_that(result).is_equal_to({})

    def test_batch_get_class_info_with_one_class(self):
        classIdList = Class_DB().get_classId_by_schoolId(None, 1, 1)
        params = self.iRClassFacade.generator_params_classIdSet(classIdList)
        result = self.iRClassFacade.batchClassInfo(params=params)
        classId = classIdList[0][0]
        assert_that(result).contains_key(classId)
        assert_that(len(result)).is_equal_to(len(classIdList))

    def test_batch_get_class_info_with_two_classes(self):
        classIdList = Class_DB().get_classId_by_schoolId(None, 1, 2)
        params = self.iRClassFacade.generator_params_classIdSet(classIdList)
        result = self.iRClassFacade.batchClassInfo(params=params)
        classId = classIdList[0][0]
        assert_that(result).contains_key(classId)
        assert_that(len(result)).is_equal_to(len(classIdList))




# @File    : t_class_DB
# @Author  : yangbaihua
# @Time    : 2020/6/11 15:24
"""
CREATE TABLE `t_class` (
  `ID` varchar(20) COLLATE utf8_bin NOT NULL,
  `GRADE_ID` varchar(20) COLLATE utf8_bin NOT NULL COMMENT '年级ID',
  `CLASS_NAME` varchar(20) COLLATE utf8_bin NOT NULL COMMENT '班级名称',
  `CREATE_TIME` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `UPDATE_TIME` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `remark` varchar(300) COLLATE utf8_bin DEFAULT NULL COMMENT '备注',
  `IS_FLAG` int(2) NOT NULL DEFAULT '1' COMMENT '删除状态：2-已毕业;1-可用;0-删除',
  `SCHOOL_ID` varchar(20) COLLATE utf8_bin NOT NULL COMMENT '学校ID',
  `IS_OPEN` int(4) DEFAULT '1' COMMENT '摄像头是否打开:1:打开;0:关闭',
  `CLASS_UUID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `STU_NUM` int(11) DEFAULT NULL COMMENT '学生数量',
  `CLASS_ROOM_ID` varchar(20) COLLATE utf8_bin DEFAULT '' COMMENT '教室id',
  `OFFICE_ID` bigint(20) DEFAULT NULL COMMENT '组织id',
  `SORT` int(4) NOT NULL DEFAULT '9999' COMMENT '排序',
  `ENROLLMENT_YEAR` int(6) DEFAULT '0' COMMENT '入学年份',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `uni_class_uuid` (`CLASS_UUID`) USING BTREE,
  KEY `FK_T_CLASS_REFERENCE_T_GRADE` (`GRADE_ID`) USING BTREE,
  KEY `index_sid` (`SCHOOL_ID`) USING BTREE,
  KEY `idx_sid_flag_ctime` (`SCHOOL_ID`,`IS_FLAG`,`CREATE_TIME`) USING BTREE,
  KEY `idx_crid` (`CLASS_ROOM_ID`) USING BTREE,
  CONSTRAINT `t_class_ibfk_1` FOREIGN KEY (`GRADE_ID`) REFERENCES `t_grade` (`ID`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=263782 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='班级表';
"""
from base.mysqlOpt.ztjy_mysql.ztjy_mysql_clients import ZTJY_Mysql_Clients


class Class_DB:
    def __init__(self):
        self._db_school_client = ZTJY_Mysql_Clients().db_school_client
        self.table = 't_class'

    def select_sql(self, isDistinct: str = '', deduplField: str = '', groupBy: str = '', orderBy: str = '',
                   sort: str = 'DESC', limitStart: int = '1', limitNum: int = '1', **kwargs):
        sqlSelct = 'SELECT * from {table}'.format(table=self.table)
        if orderBy != '':
            # 排序
            sql = sqlSelct + ' WHERE ' + ' AND '.join(['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in
                                                       kwargs.items()]) + ' ORDER BY {orderBy} {sort}'.format(
                orderBy=orderBy, sort=sort) + ' LIMIT {limit},{num}'.format(limit=limitStart, num=limitNum)
        elif groupBy != '':
            # 根据字段聚合
            sql = sqlSelct.replace('*', groupBy) + ' WHERE ' + ' AND '.join(
                ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in
                 kwargs.items()]) + ' GROUP BY {groupBy} '.format(groupBy=groupBy)
            if isDistinct != '':
                # 去重
                sql = sql.replace(deduplField, 'DISTINCT(%s)' % deduplField, 1)
        elif deduplField != '':
            sql = sqlSelct.replace('*',deduplField) + ' WHERE ' + ' AND '.join(
                ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
        else:
            sql = sqlSelct + ' WHERE ' + ' AND '.join(
                ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
        try:
            result = self._db_school_client.executeSQL(sql)
            print("t_class SQL Select Successful")
            return result
        except:
            print("t_class SQL Select FAIL")

    def get_classId_by_schoolId(self, schoolId, isFlag, count):
        if schoolId is None:
            class_id_list = self._db_school_client.executeSQL(
                'select id from t_class where  is_flag = %s order by id desc limit %d' % (isFlag, count))
        else:
            class_id_list = self._db_school_client.executeSQL(
                'select id from t_class where school_id = "%s" and is_flag = %d order by id desc limit %d' % (
                    schoolId, isFlag, count))
        class_ids = []
        for class_id in class_id_list:
            class_ids.append(class_id['id'])
        return class_ids

    def get_class_info(self, schoolId, isFlag, grade_id):
        class_info = self._db_school_client.executeSQL(
                'select ID,GRADE_ID,CLASS_NAME,SCHOOL_ID,CLASS_UUID,STU_NUM,OFFICE_ID,SORT,ENROLLMENT_YEAR from t_class '
                'where school_id = "%s" and is_flag = %d  and GRADE_ID = "%s"  order by CREATE_TIME' % (
                    schoolId, isFlag, grade_id)
        )
        return class_info

    def get_class_info_by_classId(self, classId):
        class_info = self._db_school_client.executeSQL(
                'select ID,GRADE_ID,CLASS_NAME,SCHOOL_ID from t_class '
                'where ID = "%s" and is_flag = 1 ' % (classId)
        )
        return class_info

    def get_count_class(self, schoolId, isFlag):
        """
        统计学校可用班级数
        :param schoolId:
        :param isFlag:
        :return:
        """
        count_class = self._db_school_client.executeSQL(
                'select count(ID) from t_class where school_id = "%s" and is_flag = %d' % (schoolId, isFlag))
        return count_class[0]['count(ID)']

    def get_classname(self, gradeId,className ):
        sql='SELECT CLASS_NAME,ENROLLMENT_YEAR,STU_NUM FROM t_class WHERE GRADE_ID = "%s" AND IS_FLAG = 1 AND CLASS_NAME = "%s"'%(gradeId,className)
        class_info = self._db_school_client.executeSQL(sql)
        return class_info[0]
