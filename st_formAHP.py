import  streamlit as st
import pandas as pd
import ahpy

DATA_URL = "https://hellobucketbucket.s3.ap-northeast-1.amazonaws.com/%E5%AF%B5%E7%89%A9%E7%8A%AC%E8%B3%87%E6%96%99%E5%BA%AB.csv"

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis = "columns", inplace = True)
#     data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data()

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

def main():
    menu = ["Home", "About"]
    st.title("以AHP法協助飼主做寵物犬體型最佳配適選擇 :dog2:")
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("尋找最適合之寵物犬大小 :dog:")
        # information


        # 基本資料
        with st.form(key='基本資料問卷'):
            with st.container():
                st.markdown("#### 基本資料")

                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    gender = st.selectbox(
                        "您的性別",
                        ("男性", "女性"))

                with col2:
                    age = st.selectbox(
                        "您的年齡",
                        ("20歲以下", "20歲~30歲", "30歲~40歲", "40歲~50歲", "50歲~60歲", "60歲以上"))

                with col3:
                    monthly_income = st.selectbox(
                        "您的月收入",
                        ("3萬元以下", "3萬~4萬", "4萬~5萬", "5萬~6萬", "6萬元以上"))

                with col4:
                    character = st.selectbox(
                        "您的性格",
                        ("獨立型", "敏感型", "自信型", "樂天型", "適應型"))

                with col5:
                    homeSpace = st.selectbox(
                        "您的家裡空間",
                        ("10坪以下", "10坪~20坪", "20坪~30坪", "30坪~40坪", "40坪以上"))


                # st.markdown("###### 狗狗")
                col6, col7 = st.columns(2)
                with col6:
                    activityRange = st.selectbox(
                        "您家裡附近狗狗可活動範圍",
                        ("1公頃", "1公頃~2公頃", "2公頃~3公頃", "3公頃~4公頃", "4公頃以上"))

                with col7:
                    walk = st.selectbox(
                        "您一次願意帶狗狗散步時間",
                        ("15分鐘以內", "15分鐘~30分鐘", "30分鐘~60分鐘", "60分鐘~90分鐘", "90分鐘以上"))

                col8, col9 = st.columns(2)
                with col8:
                    food = st.selectbox(
                        "您一年願意花費在狗狗的伙食費",
                        ("1.2萬以下", "1.2萬~1.8萬", "1.8萬~2.4萬", "2.4萬~3萬", "3萬元以上"))

                with col9:
                    medical = st.selectbox(
                        "您一年願意花費在狗狗的醫療費",
                        ("6400以下", "6400~6800", "6800~7200", "7200~7600", "7600以上"))

                col10, col11 = st.columns(2)
                with col10:
                    dog_character = st.selectbox(
                        "您喜好狗狗之性格",
                        ("獨立型", "敏感型", "自信型", "樂天型", "適應型"))

                with col11:
                    variety = st.selectbox(
                        "選擇一種您喜愛的寵物狗",
                        ("拉布拉多", "德國牧羊犬", "黃金獵犬", "哈士奇",
                         "科基", "博美犬", "柴犬", "薩摩耶",
                         "貴賓犬", "臘腸犬", "吉娃娃", "法鬥"))

            original_title = '<p style="font-family:Courier; color:Red; font-size: 12px;">以上填完後，請按下方送出鍵！</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="送出")

        # 家裡空間權重
        if homeSpace == '10坪以下':
            homeSpace_score = 1
        elif homeSpace == '10坪~20坪':
            homeSpace_score = 2
        elif homeSpace == '20坪~30坪':
            homeSpace_score = 3
        elif homeSpace == '30坪~40坪':
            homeSpace_score = 4
        else:
            homeSpace_score = 5
        homeSpace_Weightscore = 0.223 * homeSpace_score

        # 活動範圍權重
        if activityRange == '1公頃':
            activityRange_score = 1
        elif activityRange == '1公頃~2公頃':
            activityRange_score = 2
        elif activityRange == '2公頃~3公頃':
            activityRange_score = 3
        elif activityRange == '3公頃~4公頃':
            activityRange_score = 4
        else:
            activityRange_score = 5
        activityRange_Weightscore = 0.182 * activityRange_score

        # 散步時間權重
        if walk == '15分鐘以內':
            walk_score = 1
        elif walk == '15分鐘~30分鐘':
            walk_score = 2
        elif walk == '30分鐘~60分鐘':
            walk_score = 3
        elif walk == '60分鐘~90分鐘':
            walk_score = 4
        else:
            walk_score = 5
        walk_Weightscore = 0.198 * walk_score

        # 伙食費權重
        if food == '1.2萬以下':
            food_score = 1
        elif food == '1.2萬~1.8萬':
            food_score = 2
        elif food == '1.8萬~2.4萬':
            food_score = 3
        elif food == '2.4萬~3萬':
            food_score = 4
        else:
            food_score = 5
        food_Weightscore = 0.039 * food_score

        # 醫療費權重
        if medical == '6400以下':
            medical_score = 1
        elif medical == '6400~6800':
            medical_score = 2
        elif medical == '6800~7200':
            medical_score = 3
        elif medical == '7200~7600':
            medical_score = 4
        else:
            medical_score = 5
        medical_Weightscore = 0.062 * medical_score

        # 性格權重
        if dog_character == '獨立型':
            dog_character_score = 5
        elif dog_character == '敏感型':
            dog_character_score = 5
        elif dog_character == '自信型':
            dog_character_score = 5
        elif dog_character == '樂天型':
            dog_character_score = 5
        else:
            dog_character_score = 5
        dog_character_Weightscore = 0.296 * dog_character_score

        ## 六項屬性數值相加 ##
        attri_score = round(homeSpace_Weightscore + activityRange_Weightscore +
                       walk_Weightscore + food_Weightscore +
                       medical_Weightscore + dog_character_Weightscore, 2)

        ## 大中小型犬評分表 ##
        if attri_score <= 2.5:
            MLS_test = '小型犬'
        elif attri_score <= 3.8:
            MLS_test = '中型犬'
        else:
            MLS_test = '大型犬'

        # st.write("總分：", attri_score)
        st.write("您適合飼養的寵物犬大小為：", MLS_test)

        # data["犬種"] == variety
        # st.write(data.loc[(data['犬種'].str.contains(variety))])
        df_T = data.loc[(data['犬種'].str.contains(variety))]
        df_F = (data.loc[(data['犬隻大小'].str.contains(MLS_test)) & (data['性格'].str.contains(dog_character))])

        # st.write(df.iat[0,2])
        if (df_T.iat[0,2] == MLS_test):
            st.write("恭喜與您非常了解自己的喜好")
            st.write("適合飼養的品種犬為", variety)
        else:
            st.write("抱歉與您欲飼養之寵物犬體型大小不合")
            st.write("本系統推薦以下為您適合飼養的寵物犬大小與品種狗種類")
            st.write(df_F)



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
