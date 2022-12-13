pip install ahpy

import  streamlit as st
import pandas as pd
import ahpy

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

def main():
    menu = ["Home", "About"]
    st.title("以AHP法協助飼主做寵物犬體型最佳配適選擇 :dog2:")
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("尋找最適合之寵物犬大小 :dog:")
        # information

        # Change font size and font color
        # https://discuss.streamlit.io/t/change-font-size-and-font-color/12377/2
        # original_title = '<p style="font-family:Courier; color:White; font-size: 22px;">環境</p>'
        # st.markdown(original_title, unsafe_allow_html=True)

        # 環境
        with st.form(key='環境問卷'):
            with st.container():
                st.markdown("#### A.環境")

                col1, col2 = st.columns([2, 3])

                with col1:
                    A1_A2 = st.radio(
                        "選擇 A1.家裡空間 或 A2.活動範圍",
                        ('A1.家裡空間', 'A2.活動範圍'), horizontal=True)

                with col2:
                    A1_A2_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)


            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    A1_A3 = st.radio(
                        "選擇 A1.家裡空間 或 A3.居住人數",
                        ('A1.家裡空間', 'A3.居住人數'), horizontal=True)

                with col2:
                    A1_A3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！） ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            with st.container():
                # st.markdown("##### A - wrt 環境 - or B")
                col1, col2 = st.columns([2, 3])

                with col1:
                    A2_A3 = st.radio(
                        "選擇 A2.活動範圍 或 A3.居住人數",
                        ('A2.活動範圍', 'A3.居住人數'), horizontal=True)

                with col2:
                    A2_A3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）  ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            original_title = '<p style="font-family:Courier; color:Red; font-size: 12px;">以上填完後，請按下方送出鍵！</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="送出")
        # 1_2
        # st.write("您選擇了:", A1_A2)
        if A1_A2 == 'A1.家裡空間':
            A1_A2_scores = int(A1_A2_scores)
            # st.write("分數:", A1_A2_scores)
        else:
            A1_A2_scores = round((1 / int(A1_A2_scores)), 3)
            # st.write("分數:", A1_A2_scores)
        # 1_3
        # st.write("您選擇了:", A1_A3)
        if A1_A3 == 'A1.家裡空間':
            A1_A3_scores = int(A1_A3_scores)
            # st.write("分數:", A1_A3_scores)
        else:
            A1_A3_scores = round((1 / int(A1_A3_scores)), 3)
            # st.write("分數:", A1_A3_scores)
        # 2_3
        # st.write("您選擇了:", A2_A3)
        if A2_A3 == 'A2.活動範圍':
            A2_A3_scores = int(A2_A3_scores)
            # st.write("分數:", A2_A3_scores)
        else:
            A2_A3_scores = round((1 / int(A2_A3_scores)), 3)
            # st.write("分數:", A2_A3_scores)

        # AHPy
        env_comparisons = {('A1.家裡空間', 'A2.活動範圍'): A1_A2_scores,
                             ('A1.家裡空間', 'A3.居住人數'): A1_A3_scores,
                             ('A2.活動範圍', 'A3.居住人數'): A2_A3_scores}
        # st.text(env_comparisons)

        #
        envs = ahpy.Compare(name='Envs', comparisons=env_comparisons, precision=3, random_index='saaty')
        st.write("各屬性權重 :", envs.target_weights)
        st.write("CR :", envs.consistency_ratio)

        # 預算
        with st.form(key='預算問卷'):
            with st.container():
                st.markdown("#### B.預算")

                col1, col2 = st.columns([2, 3])

                with col1:
                    B1_B2 = st.radio(
                        "選擇 B1.配件 或 B2.食物",
                        ('B1.配件', 'B2.食物'), horizontal=True)

                with col2:
                    B1_B2_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)


            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    B1_B3 = st.radio(
                        "選擇 B1.配件 或 B3.醫療",
                        ('B1.配件', 'B3.醫療'), horizontal=True)

                with col2:
                    B1_B3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！） ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    B2_B3 = st.radio(
                        "選擇 B2.食物 或 B3.醫療",
                        ('B2.食物', 'B3.醫療'), horizontal=True)

                with col2:
                    B2_B3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）  ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            original_title = '<p style="font-family:Courier; color:Red; font-size: 12px;">以上填完後，請按下方送出鍵！</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="送出")
        # 1_2
        if B1_B2 == 'B1.配件':
            B1_B2_scores = int(B1_B2_scores)
        else:
            B1_B2_scores = round((1 / int(B1_B2_scores)), 3)
        # 1_3
        if B1_B3 == 'B1.配件':
            B1_B3_scores = int(B1_B3_scores)
        else:
            B1_B3_scores = round((1 / int(B1_B3_scores)), 3)
        # 2_3
        if B2_B3 == 'B2.食物':
            B2_B3_scores = int(B2_B3_scores)
        else:
            B2_B3_scores = round((1 / int(B2_B3_scores)), 3)

        # AHPy
        budget_comparisons = {('B1.配件', 'B2.食物'): B1_B2_scores,
                             ('B1.配件', 'B3.醫療'): B1_B3_scores,
                             ('B2.食物', 'B3.醫療'): B2_B3_scores}
        #
        budget = ahpy.Compare(name='Budgets', comparisons=budget_comparisons, precision=3, random_index='saaty')
        st.write("各屬性權重 :", budget.target_weights)
        st.write("CR :", budget.consistency_ratio)

        # 外觀
        with st.form(key='外觀問卷'):
            with st.container():
                st.markdown("#### C.外觀")

                col1, col2 = st.columns([2, 3])

                with col1:
                    C1_C2 = st.radio(
                        "選擇 C1.體重 或 C2.腿長",
                        ('C1.體重', 'C2.腿長'), horizontal=True)

                with col2:
                    C1_C2_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    C1_C3 = st.radio(
                        "選擇 C1.體重 或 C3.體長",
                        ('C1.體重', 'C3.體長'), horizontal=True)

                with col2:
                    C1_C3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！） ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    C2_C3 = st.radio(
                        "選擇 C2.腿長 或 C3.體長",
                        ('C2.腿長', 'C3.體長'), horizontal=True)

                with col2:
                    C2_C3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）  ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            original_title = '<p style="font-family:Courier; color:Red; font-size: 12px;">以上填完後，請按下方送出鍵！</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="送出")
        # 1_2
        if C1_C2 == 'C1.體重':
            C1_C2_scores = int(C1_C2_scores)
        else:
            C1_C2_scores = round((1 / int(C1_C2_scores)), 3)
        # 1_3
        if C1_C3 == 'C1.體重':
            C1_C3_scores = int(C1_C3_scores)
        else:
            C1_C3_scores = round((1 / int(C1_C3_scores)), 3)
        # 2_3
        if C2_C3 == 'C2.腿長':
            C2_C3_scores = int(C2_C3_scores)
        else:
            C2_C3_scores = round((1 / int(C2_C3_scores)), 3)

        # AHPy
        outside_comparisons = {('C1.體重', 'C2.腿長'): C1_C2_scores,
                              ('C1.體重', 'C3.體長'): C1_C3_scores,
                              ('C2.腿長', 'C3.體長'): C2_C3_scores}
        #
        outside = ahpy.Compare(name='Outsides', comparisons=outside_comparisons, precision=3, random_index='saaty')
        st.write("各屬性權重 :", outside.target_weights)
        st.write("CR :", outside.consistency_ratio)

        # 活動
        with st.form(key='活動問卷'):
            with st.container():
                st.markdown("#### D.活動")

                col1, col2 = st.columns([2, 3])

                with col1:
                    D1_D2 = st.radio(
                        "選擇 D1.散步時間 或 D2.睡覺時間",
                        ('D1.散步時間', 'D2.睡覺時間'), horizontal=True)

                with col2:
                    D1_D2_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    D1_D3 = st.radio(
                        "選擇 D1.散步時間 或 D3.訓練時間",
                        ('D1.散步時間', 'D3.訓練時間'), horizontal=True)

                with col2:
                    D1_D3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！） ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            with st.container():
                col1, col2 = st.columns([2, 3])

                with col1:
                    D2_D3 = st.radio(
                        "選擇 D2.睡覺時間 或 D3.訓練時間",
                        ('D2.睡覺時間', 'D3.訓練時間'), horizontal=True)

                with col2:
                    D2_D3_scores = st.radio(
                        "屬性分數（若選填'1'表示兩屬性同樣重要！）  ",
                        ('1', '2', '3', '4', '5',
                         '6', '7', '8', '9'), horizontal=True)

            original_title = '<p style="font-family:Courier; color:Red; font-size: 12px;">以上填完後，請按下方送出鍵！</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="送出")
        # 1_2
        if D1_D2 == 'D1.散步時間':
            D1_D2_scores = int(D1_D2_scores)
        else:
            D1_D2_scores = round((1 / int(D1_D2_scores)), 3)
        # 1_3
        if D1_D3 == 'D1.散步時間':
            D1_D3_scores = int(D1_D3_scores)
        else:
            D1_D3_scores = round((1 / int(D1_D3_scores)), 3)
        # 2_3
        if D2_D3 == 'D2.睡覺時間':
            D2_D3_scores = int(D2_D3_scores)
        else:
            D2_D3_scores = round((1 / int(D2_D3_scores)), 3)

        # AHPy
        activity_comparisons = {('D1.散步時間', 'D2.睡覺時間'): D1_D2_scores,
                              ('D1.散步時間', 'D3.訓練時間'): D1_D3_scores,
                              ('D2.睡覺時間', 'D3.訓練時間'): D2_D3_scores}
        #
        activity = ahpy.Compare(name='Activities', comparisons=activity_comparisons, precision=3, random_index='saaty')
        st.write("各屬性權重 :", activity.target_weights)
        st.write("CR :", activity.consistency_ratio)

        # 隱藏made with streamlit
        hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    else:
        st.subheader("About")


if __name__ == '__main__':
    main()
