# @File    : test_SalesOrderFacade_appPay
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/30 18:00
import allure
import pytest
from assertpy import assert_that

from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common_projects.api.ztjy.dubbo.ztjy_sales_server.SalesOrderFacade import SalesOrderFacade


@allure.description('负责人:杨百花')
class Test_SalesOrderFacade_appPay:
    def setup_class(self):
        self.ztjy_client = API_ZTJY_Client()
        self.ztjy_config = self.ztjy_client.ztjy_config
        self.salesOrderFacade = SalesOrderFacade()

    @pytest.fixture()
    def fixture_sales_order_params_init(self):
        self.albumId = "27624cf023e34c4c8f40d7734913e3ee"
        self.cityCode = "1120100"
        self.classId = "k4pOpXNCgXxpldgxtEz"
        self.className = "鸭二班"
        self.deliveryAmount = "0"
        self.deliveryId = 330
        self.districtCode = "1120102"
        self.goodsImage = "https=//ztjy-album-server.ztjy61.cn/9600010120190620113940631Ph74pLst"
        self.goodsName = "洛央下的商品"
        self.goodsNo = "SGJ00014"
        self.gradeName = "河蟹"
        self.groupOrderNo = ""
        self.houseAddress = "11的说法"
        self.orderAmount = "0.09"
        self.pcs = 1
        self.price = "0.09"
        self.productDetailList = []
        self.productList = []
        self.provinceCode = "1020000"
        self.quantity = 1
        self.recipient = "洛央下"
        self.recipientPhone = "134****0000"
        self.schoolId = "e338d65437fac34eb471"
        self.specNo = "SGJ00014003"
        self.studentId = "9bd41fc1e8c94ef29a53"
        self.studentName = "任天野"
        self.userId = "7c97d54181a1b9ef2c96"
        self.payChannel = 'WechatPay'

    def fixture_dto_params(self, **kwargs):
        requestDTO = {}
        requestDTO.update(**kwargs)
        return requestDTO

    def test_add_app_pay_sales_order(self, fixture_sales_order_params_init):
        requestDTO = self.fixture_dto_params(albumId=self.albumId, cityCode=self.cityCode, classId=self.classId,
                                             className=self.className, deliveryAmount=self.deliveryAmount,
                                             deliveryId=self.deliveryId, districtCode=self.districtCode,
                                             goodsImage=self.goodsImage, goodsName=self.goodsName, goodsNo=self.goodsNo,
                                             gradeName=self.gradeName, groupOrderNo=self.groupOrderNo,
                                             houseAddress=self.houseAddress, orderAmount=self.orderAmount, pcs=self.pcs,
                                             price=self.price, productDetailList=self.productDetailList,
                                             productList=self.productList, provinceCode=self.provinceCode,
                                             quantity=self.quantity, recipient=self.recipient,
                                             recipientPhone=self.recipientPhone, schoolId=self.schoolId,
                                             specNo=self.specNo, studentId=self.studentId, studentName=self.studentName,
                                             userId=self.userId)

        params = SalesOrderFacade().generator_params(requestDTO=requestDTO, payChannel=self.payChannel)
        result = SalesOrderFacade().get_app_pay(params=params)
        assert_that(result).is_not_one()


    def update_order_status(self, orderStatus, isFlag):
        """

        :param orderStatus:
        :param isFlag:
        :return:
        """
        Sales_Order_DB().update_sql(self.orderNo, order_status=orderStatus, flag=isFlag)

    @pytest.mark.parametrize('order_status,orderStatusStr', [(1, u'待支付'), (2, '待打印'), (3, '待收货'), (4, '已完成'),
                                                             (5, '退款中'), (6, '拼团中'), (7, '部分退款'), (8, '已退款'),
                                                             (9, '已关闭'), (30, '')])
    @pytest.mark.parametrize('flag', (0, 1))
    def test_get_order_info_check_sales_order_status(self, order_status, flag, orderStatusStr):
        """

        :param order_status:
        :param flag:
        :param orderStatusStr:
        :param delFalg:
        :return:
        """
        self.update_order_status(order_status, flag)
        params = self.salesOrderFacade.generator_params(self.orderNo)
        result = self.salesOrderFacade.get_order_info_by_app(params=params)
        assert_that(result['orderStatusStr']).is_equal_to(orderStatusStr)
        assert_that(result).is_none()