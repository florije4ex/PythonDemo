# @File    : generate_test_data
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/8/20 15:29

class Generator_Test_Data:
    '''
    组合测试数据
    '''

    def get_session_school_id(self, sessionId, schoolId):
        '''
        获取到session和schoolId
        :param sessionId:
        :param schoolId:
        :return:
        '''
        pass

    def get_date_count_range_data_code(self, date, countRange, dataCodes):
        '''

        :param date:日期，为空默认昨天
        :param countRange:统计周期（0-日；1-周；2-历史）
        :param dataCodes:统计数据列表，枚举建wiki
        :return:
        '''
        date = [None,'2020-08-17', '2020-08-18','2020-08-19','2020-08-20',]  #None = 昨天，
        countRange = [0, 1, 2]
        dataCodes = ['STU_PARENT_ACT_RATE','STU_PARENT_ACT_COUNT','STU_COUNT_REALTIME','MONTH_STU_PARENT_ACT_RATE','STU_ACT_PARENT_AVG']
