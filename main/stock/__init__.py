class Frequency:
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    ALL = [DAILY, WEEKLY, MONTHLY]
    CHOICES = [
        (DAILY, DAILY),
        (WEEKLY, WEEKLY),
        (MONTHLY, MONTHLY),
    ]


class TradeType:
    TSE = "tse"
    OTC = "otc"
    ALL = [TSE, OTC]
    CHOICES = [
        (TSE, TSE),
        (OTC, OTC),
    ]
    TRADE_TYPE_ZH_ENG_MAP = {"上市": TSE, "上櫃": OTC}


class InfoEndpoint:
    company = "https://isin.twse.com.tw/isin/single_main.jsp?owncode="
    single_day = {
        TradeType.TSE: "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL",
        TradeType.OTC: "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_quotes",
        # The "real_time" endpoint has rate limit: 3 requests per 5 seconds.
        "real_time": "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=",
    }
    multiple_days = "https://query1.finance.yahoo.com/v7/finance/download/"


class UnknownStockIdError(Exception):
    ...
