import streamlit as st
from multiapp import MultiApp
import zero
import one
import two
import three

# import const
# from streamlit_option_menu import option_menu

# st.set_page_config(**const.SET_PAGE_CONFIG)
# st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
# selected = option_menu(**const.OPTION_MENU_CONFIG)

app = MultiApp()
app.add_app("こちらよりお選び下さい", zero.zero0_load)
app.add_app("👦🏻 自己紹介シート 📜", three.three_load)
app.add_app("☯️ 独断と偏見のエニアグラム 🙏", one.one_load)
app.add_app("📧 障害受付 🪛", two.two_load)
app.run()
