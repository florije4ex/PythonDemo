# @File    : Test_SalesOrderFacade_getOrderInfo4HMS
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/8/31 15:22

import allure
import pytest
import ujson
from assertpy import assert_that

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool
from common_projects.api.ztjy.dubbo.ztjy_sales.ztjy_sales_server.SalesOrderFacade import SalesOrderFacade
from common_projects.mysqlOpt.ztjy_mysql.db_sales.t_sales_order_db import Sales_Order_DB

@allure.description('负责人:杨百花')
class Test_SalesOrderFacade_getOrderInfo4HMS:
    def setup_class(self):
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.salesOrderDB = Sales_Order_DB()
        self.salesOrderFacade = SalesOrderFacade()

    @pytest.fixture()
    def fixture_generator_specify_order_status_params(self):
        school_info = self.ztjy_config.parent_user_babys_info
        schoolid = school_info[0].schools[0].id
        order_info_sql = self.salesOrderDB.get_the_latest_orderNo_by_schoolId_sql(schoolid)
        orderStatusList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 30]
        for i in range(len(orderStatusList)):
            # 构建orderInfo_params
            orderInfo_params = {}
            orderNo = order_info_sql[0][0]
            if order_info_sql is None:
                self.salesOrderDB.insert_sales_order_sql
            else:
                for orderStatus in orderStatusList:
                    try:
                        self.salesOrderDB.update_sales_order_order_status_sql(orderStatus,orderNo)
                    except:
                        print('%s更新订单状态失败%s'%(DateTimeTool.getNowTime(),orderNo))
                    if orderStatus == 0:
                        orderStatusStr = '待支付'
                    elif orderStatus == 1:
                        orderStatusStr = '待打印'
                    elif orderStatus == 2:
                        orderStatusStr = '打印中'
                    elif orderStatus == 3:
                        orderStatusStr = '待收货'
                    elif orderStatus == 4:
                        orderStatusStr = '已完成'
                    elif orderStatus == 5:
                        orderStatusStr = '退款中'
                    elif orderStatus == 6:
                        orderStatusStr = '拼团中'
                    elif orderStatus == 7:
                        orderStatusStr = '部分退款'
                    elif orderStatus == 8:
                        orderStatusStr = '已退款'
                    elif orderStatus == 9:
                        orderStatusStr = '已关闭'
                    elif orderStatus == 30:
                        orderStatusStr = '签收订单，自动完成订单，订单'
                    else:
                        print('%s订单状态不存在' % DateTimeTool.getNowTime())
                        break
                if not orderNo is None:
                    orderInfo_params.update({'orderNo':orderNo})
                if not orderStatus is None:
                    orderInfo_params.update({'orderStatus':orderStatus})
                if not orderStatusStr is None:
                    orderInfo_params.update({'orderStatusStr':orderStatusStr})
                fixture_params = orderInfo_params
                yield fixture_params

    def test_get_order_info_for_hms_with_order_status(self,fixture_generator_specify_order_status_params):
        order_info = fixture_generator_specify_order_status_params
        orderNo = order_info['orderNo']
        params = self.salesOrderFacade.generator_params(orderNo)
        result = self.salesOrderFacade.get_order_info_by_hms(params=params)
        body = ujson.loads(result)
        assert_that(body['orderNo']).is_equal_to(orderNo)
        assert_that(body['orderStatus']).is_equal_to(order_info['orderStatus'])
        assert_that(body['orderStatusStr']).is_equal_to(order_info['orderStatusStr'])
