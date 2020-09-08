# @File    : sales_order_derector
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/2 8:50
from functools import wraps


def update_sales_order_hms_info(**kwargs):
    '''
    更新订单状态装饰器
    :return:
    '''

    # 传入func

    def outter(func):
        # 类实例,需要获取到实例属性orderNo
        @wraps(func)
        def wrapper(self, *args, **kwargs2):
            print('This is a decrator!')
            if not self.orderNo:
                print('orderNo不存在，进行插入')
                self.salesOrderDB.insert_sales_order_sql()
                self.salesOrderDetailDB.insert_sales_order_detail_sql()
            updateData = kwargs2
            print(updateData)
            self.salesOrderDB.update_sales_order_sql(self.selectField, updateData)  # 更新订单状态
            self.salesDetailOrderDB.update_sales_order_detail_sql(self.selectField, updateData)

            if self.orderInfo[0]['pay_status'] != self.orderDetailInfo[0]['pay_status']:
                print('主单或子单pay_status =1 已支付')
                updatePayStatus = {"pay_status": 1}
                self.salesOrderDB.update_sales_order_sql(self.selectField, updatePayStatus)  # 更新订单支付状态
                self.salesDetailOrderDB.update_sales_order_detail_sql(self.selectField, updatePayStatus)
            fun = func(*args, **kwargs2)
            return fun

        return wrapper

    return outter