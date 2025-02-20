import streamlit as st
import streamlit_authenticator as stauth
import sqlite3
import yaml
from yaml.loader import SafeLoader
import time
import mojimoji  # ✅ 全角・半角変換ライブラリ（インストール: `pip install mojimoji`）

## ユーザー設定読み込み
yaml_path = "config.yaml"

def one_load():
    with open(yaml_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        credentials=config['credentials'],
        cookie_name=config['cookie']['name'],
        cookie_key=config['cookie']['key'],
        cookie_expiry_days=config['cookie']['expiry_days'],
    )

    # ✅ ログイン UI を表示
    authenticator.login()

    # ✅ ユーザーが認証済みなら処理を続ける
    if st.session_state["authentication_status"]:
        # 🔹 **ログインユーザーの username（社員番号）を取得**
        raw_employee_id = st.session_state["username"]  # 👈 ここで入力された ID を取得

        # ✅ **全角を半角に統一し、小文字を大文字に変換**
        employee_id = mojimoji.zen_to_han(raw_employee_id).upper()  # 👈 修正ポイント

        with st.sidebar:
            st.markdown(f'## Welcome *{st.session_state["name"]}*')
            authenticator.logout('ログアウト', 'sidebar')
            st.divider()

        st.success(' ログインしました!')

        # ✅ データベース接続
        db_path = "tfc_dupg_mikami1.db"  # データベースファイル名
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # ✅ `employee_id` を使用してデータ取得
        cursor.execute("SELECT TYPE, COMMENT FROM tfc_dupg_mikami1 WHERE NO = ?", (employee_id,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            user_type, user_comment = user_data
            time.sleep(2)
            # 1. 「あなたのタイプは、」を最初に表示
            st.write("### あなたのタイプは・・・")
            time.sleep(2)

            # 2. タイプ名を大きく強調して表示
            st.markdown(f'<h1 style="text-align:center; color:red;">{user_type} です❕</h1>', unsafe_allow_html=True)
            time.sleep(2)

            # 3. タイピング風アニメーションでコメントを表示
            st.write("#### あなたに対する三上からの印象は、こちらです。")
            comment_placeholder = st.empty()
            displayed_text = ""

            for char in user_comment:
                displayed_text += char
                comment_placeholder.write(displayed_text)
                time.sleep(0.05)

            link_url = "https://promo.kadokawa.co.jp/9types/biz9type/"  # リンク先のURLを指定
            st.markdown(f'<a href="{link_url}" target="_blank">クリックして診断する🔮</a>', unsafe_allow_html=True)
            
        else:
            st.error("ユーザー情報が見つかりません。")

    elif st.session_state["authentication_status"] is False:
        st.error("ユーザー名またはパスワードが間違っています")

    elif st.session_state["authentication_status"] is None:
        st.warning("ログインしてください")


    
