from datetime import date, timedelta, datetime, timezone
from dateutil.parser import parse


class RentalBook:
    def __init__(
        self,
        name: str,
        expire_date_text: str,
        can_extend_period: bool,
        extend_period_button_name: str,
    ) -> None:
        self.name: str = name
        self.expire_date: date = parse(expire_date_text).date()  # timezone無指定だが図書館サイトから取得した日本時間の日付
        self.expire_date_text: str = expire_date_text
        self.can_extend_period: bool = can_extend_period
        self.extend_period_button_name: str = extend_period_button_name

    def is_expired(self) -> bool:
        return self.is_expire_in_xdays(-1)

    def is_expire_in_xdays(self, xday_before: int) -> bool:
        today = self.get_jst_now_date()
        if self.expire_date - today <= timedelta(days=xday_before):
            return True
        return False

    def get_expire_text_from_today(self) -> str:
        today = self.get_jst_now_date()
        remain_days = (self.expire_date - today).days

        if remain_days == 1:
            text = " (明日ﾏﾃﾞ)"
        elif remain_days == 0:
            text = " (今日ﾏﾃﾞ)"
        elif remain_days < 0:
            text = " (延滞)"
        else:
            text = " (あと{0}日)".format(remain_days)

        return text

    @classmethod
    def get_jst_now_date(cls) -> date:
        # タイムゾーンの生成
        JST = timezone(timedelta(hours=+9), "JST")
        # 現在時刻取得
        return datetime.now(JST).date()

    def get_list_string(self) -> str:
        string = "{},{},extend={},{}".format(
            self.name,
            self.expire_date,
            self.can_extend_period,
            self.extend_period_button_name,
        )
        return string

    def __str__(self) -> str:
        string = (
            """
            name: {}
            expire_date: {}
            expire_date(text): {}
            can_extend_period: {}
            extend_period_button_name: {}"""
        ).format(
            self.name,
            self.expire_date,
            self.expire_date_text,
            self.can_extend_period,
            self.extend_period_button_name,
        )
        return string
