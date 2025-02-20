import streamlit as st
from multiapp import MultiApp
# ライブラリ追加
from PIL import Image

def three_load():
    # 画像リストを定義（拡張子を .jpg に変更）
    image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg", "image6.jpg", "image7.jpg", "image8.jpg", "image9.jpg"]

    # セッションステートの初期化
    if "image_index" not in st.session_state:
        st.session_state.image_index = 0

    # 現在の画像を表示（ボタンの上に配置）
    st.image(image_paths[st.session_state.image_index], use_container_width=True)

    # ボタンの配置（上部に移動）
    col1, col2, col3 = st.columns([12, 1, 2])  # 右側をさらに広くする

    # 左側（戻るボタン）
    with col1:
        if st.button("👈戻る"):
            st.session_state.image_index = (st.session_state.image_index - 1) % len(image_paths)
            st.rerun()

    # 右側（次へボタン）
    with col3:
        if st.button("次へ👉"):
            st.session_state.image_index = (st.session_state.image_index + 1) % len(image_paths)
            st.rerun()

    # 現在の画像パスを取得
    image_path = image_paths[st.session_state.image_index]

    # もし、image5.jpgの場合のみ「クリックしてアクセス」を表示する
    if image_path == "image8.jpg":
        link_url = "https://promo.kadokawa.co.jp/9types/biz9type/"  # リンク先のURLを指定
        st.markdown(f'<a href="{link_url}" target="_blank">クリックして診断する</a>', unsafe_allow_html=True)