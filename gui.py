import streamlit as st
import pickle
import numpy as np

import warnings

# Importing library
import csv
# pipe = pickle.load(open('/Users/amanjain/Downloads/Heart-Disease-Prediction-using-Machine-Learning-master/heart.csv', 'rb'))


with open('model_rf', 'rb') as f:
    rf = pickle.load(f)

# with open('model_nb' , 'rb') as f:
#     nb = pickle.load(f)

# with open('model_sv' , 'rb') as f:
#     sv = pickle.load(f)


inp_val = []

chestpain = [
    'typical angina',
    'atypical angina',
    'non-anginal pain',
    'asymptomatic'
]
sex = [
    'Male',
    'Female',
    'Trans'
]
ca = [
    '0',
    '1',
    '2'
]

response = [
    'yes',
    'no'
]

thal_response = [
    'normal',
    'fixed defect',
    'reversable defect'
]

slope_response = [
    'upsloping',
    'flat',
    'downsloping'
]


col1, col2 = st.columns(2)


age = 0
col_sex = 0
chest_pain = 0
rest_bp = 0
chol = 0
fasting_sugar = 0
elect_crd = 0
max_heart = 0
exp_angina = 0
ST_dep = 0
slope = 0
Ca = 0
thal = 0


inp_val = []

# with col1:
#     chest_pain = st.selectbox('Chest Pain', sorted(chestpain))
#     if(chest_pain=="typical angina"):
#         chest_pain=1
#     elif(chest_pain=="atypical angina"):
#         chest_pain=2
#     elif(chest_pain=="non-anginal pain"):
#         chest_pain=3
#     else:
#         chest_pain=4
#     #chol = st.text_input('cholestoral in mg/dl')

# with col2:
#     chol = st.text_input('cholestoral in mg/dl')


col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)
col9, col10, col11 = st.columns(3)
col12, col13 = st.columns(2)


# global a
# a="0"
lst = []

a = 0

if "page" not in st.session_state:
    st.session_state.page = 0


def nextpage():
    st.session_state.page += 1
    file = open('input.csv', 'w+', newline='')
    inp_val = [[int(age)], [1 if col_sex == "Male" else 0], [chest_pain], [int(rest_bp)], [int(chol)], [int(fasting_sugar)], [
        int(elect_crd)], [int(max_heart)], [1 if exp_angina == "yes" else 0], [int(ST_dep)], [slope], [int(Ca)], [thal]]
    # file.write(inp_val)
    with file:
        write = csv.writer(file)
        write.writerows(inp_val)


def restart(): st.session_state.page = 0


placeholder = st.empty()
placeholder.button("Predict", on_click=nextpage,
                   disabled=(st.session_state.page > 0))

a = 0

if st.session_state.page == 0:
    st.title('Heart Disease Predictor')

    a = a+3
    print(a)

    # lst.append(a)
    with col1:
        chest_pain = st.selectbox('Chest Pain', sorted(chestpain))
        if (chest_pain == "typical angina"):
            chest_pain = 0
        elif (chest_pain == "atypical angina"):
            chest_pain = 2
        elif (chest_pain == "non-anginal pain"):
            chest_pain = 3
        else:
            chest_pain = 4
    #chol = st.text_input('cholestoral in mg/dl')

    with col2:
        chol = st.text_input('cholestoral in mg/dl')

    with col3:
        col_sex = st.selectbox('Sex', sorted(sex))

    with col4:
        age = st.text_input('Age')

    with col5:
        Ca = st.selectbox('number of major vessels (0-3)', sorted(ca))

    with col6:
        fasting_sugar = st.text_input("fasting blood sugar in mg/dl")

    with col7:
        elect_crd = st.text_input("resting electrocardiographic results")

    with col8:
        rest_bp = st.text_input("resting blood pressure in mm Hg")

    with col9:
        max_heart = st.text_input("maximum heart rate achieved")

    with col10:
        exp_angina = st.selectbox("Do you exercise induced angina?", response)

    with col11:
        ST_dep = st.text_input("ST depression")

    with col12:
        thal = st.selectbox("thalassemia", thal_response)
        if (thal == "normal"):
            thal = 0
        elif (thal == "fixed defect"):
            thal = 1
        elif (thal == "reversable defect"):
            thal = 2

    with col13:
        slope = st.selectbox("slope", slope_response)
        if (slope == "upsloping"):
            slope = 1
        elif (slope == "flat"):
            slope = 2
        elif (slope == "downsloping"):
            slope = 0

    # st.checkbox()
    # a="8"
    # print(a)

    #inp_val=[int(age),1 if col_sex=="Male" else 0,chest_pain,int(rest_bp),int(chol),int(fasting_sugar),int(elect_crd),int(max_heart),1 if exp_angina=="yes" else 0,int(ST_dep),slope,int(Ca),thal]


elif st.session_state.page == 1:
    # inp_val=[int(age),1 if col_sex=="Male" else 0,chest_pain,int(rest_bp),int(chol),int(fasting_sugar),int(elect_crd),int(max_heart),1 if exp_angina=="yes" else 0,int(ST_dep),slope,int(Ca),thal]
    print(a)
    print('hello1')
    # print(lst)
    warnings.filterwarnings('ignore')

    # placeholder.empty()
    lst = []
    lst2 = []
    with open("input.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            lst.append(row)

        for i in range(13):

            lst2.append(int(lst[i][0]))
        print(lst2)
        st.title('Prediction based on your data')
        if (rf.predict([lst2])[0] == 0):
            st.write("There is 90 percent chance that you don't have heart disease")
        else:
            st.write("There is 90 percent chance that you have heart disease")
        # st.write("RESULT",nb.predict([lst2])[0])
        # st.write("RESULT",sv.predict([lst2])[0])
        #st.write("RESULT", rf.predict([[56, 1, 1, 120, 240, 0, 1, 169, 0, 0, 0, 0, 2]])[0])

        placeholder.empty()
        st.button("Restart", on_click=restart)


# if st.button('Predict'):


# pipe = pickle.load(open('D:\sanchit\programming shit\python shit\model_rf .pkl', 'rb'))
# pipe.predict()
