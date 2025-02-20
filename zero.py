import streamlit as st
import time

## ユーザー設定読み込み
yaml_path = "config.yaml"

def zero0_load():
    st.button("⛄❄")
    st.snow()

    # プレースホルダーの宣言
    place_holder = st.empty()

    # 表示するメッセージリスト
    messages = [
        "データ利活用推進グループの皆様、初めまして！",
        "ご縁があり配属となりました、",
        "三上 司（34） と申します！",
        "至らぬ点も多々あるかと思いますが、",
        "ご指導ご鞭撻の程、宜しくお願い致します🙇🏻"
    ]

    # 3 回ループさせる
    for _ in range(3):  # 3 回繰り返す
        time.sleep(1.5)  # 1.5 秒待機
        for message in messages:  # メッセージを順番に表示
            place_holder.title(message)  # メッセージを表示
            time.sleep(2.5)  # 2.5 秒待機
            place_holder.text('')  # 表示をクリア
    
    st.write("↑↑↑ 上のボタンを押すと雪を降らせます")
