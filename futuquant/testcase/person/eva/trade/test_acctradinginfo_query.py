#-*-coding:utf-8-*-

from futuquant import *
import pandas

class AccTradeInfoQuery(object):
    #acctradinginfo_query 获取最大可买可卖

    def __init__(self):
        pandas.set_option('max_columns', 1000)
        pandas.set_option('display.width', 1000)

    def test1(self):
        trade_us = OpenUSTradeContext(host='127.0.0.1', port=11112)
        print(trade_us.unlock_trade('123123'))
        print(trade_us.acctradinginfo_query(order_type=OrderType.NORMAL, code='US.AAPL180817C190000', price=23.8,
                                            order_id=0, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=281756460277401516))

    def test2(self):
        host = '127.0.0.1'
        port = 11111

        trade_hk = OpenHKTradeContext(host, port)
        trade_us = OpenUSTradeContext(host, port)
        trade_sh_m = OpenCNTradeContext(host, port)

        print(trade_hk.acctradinginfo_query(order_type = OrderType.NORMAL, code= 'HK.00700', price = 378.2, order_id = None,
                                            adjust_limit=0, trd_env=TrdEnv.SIMULATE, acc_id=0))
        print(trade_us.acctradinginfo_query(order_type=OrderType.NORMAL, code='US.BABA', price=187.34, order_id=None,
                                            adjust_limit=0, trd_env=TrdEnv.SIMULATE, acc_id=281756460277401516))
        print(trade_sh_m.acctradinginfo_query(order_type=OrderType.NORMAL, code='SZ.000428', price=2.9, order_id=None,
                                            adjust_limit=0, trd_env=TrdEnv.SIMULATE, acc_id=0))

if __name__ == '__main__':
    atiq = AccTradeInfoQuery()
    atiq.test1()