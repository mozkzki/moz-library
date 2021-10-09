from typing import List, Union

from moz_library import search_rental, search_reserve

# from dotenv import load_dotenv
from moz_library.user_book_info import UserBookInfo


def main():
    mode = "rental"

    params = {
        # 検索モード
        "mode": mode,  # choice [rental, expire, reserve, prepare
        # ユーザー指定
        "all_user": True,
        # "users": "USER1",
        # 結果0件の場合の表示モード
        "zero": "always",  # choice [always, message, none]
        # 結果をユーザごとに個別表示するならTrue
        "separate": True,
        # 取得する結果の形式
        "result_type": "message",  # choice [message, info]
    }

    if mode == "rental" or mode == "expire":
        # 借りてる系
        result = search_rental(params)
        _print_result(result)
    elif mode == "reserve" or mode == "prepare":
        # 予約系
        result = search_reserve(params)
        _print_result(result)


def _print_result(result_list: Union[List[str], List[UserBookInfo]]):
    if len(result_list) > 0:
        print("=====================================")
    for result in result_list:
        print(result)
        print("=====================================")


if __name__ == "__main__":
    main()
