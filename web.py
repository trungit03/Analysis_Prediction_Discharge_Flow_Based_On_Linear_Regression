import joblib
import streamlit
import streamlit as st
import pandas as pd

model_tbb = joblib.load("F:/do_an/dacn_nhom12/model/model_tbb.joblib")
model_tn = joblib.load("F:/do_an/dacn_nhom12/model/model_tn.joblib")
model_dh = joblib.load("F:/do_an/dacn_nhom12/model/model_dh.joblib")

scaler_tbb = joblib.load("F:/do_an/dacn_nhom12/scaler/scaler_tbb.joblib")
scaler_tn = joblib.load("F:/do_an/dacn_nhom12/scaler/scaler_tn.joblib")
scaler_dh = joblib.load("F:/do_an/dacn_nhom12/scaler/scaler_dh.joblib")

encoder_tbb = joblib.load("F:/do_an/dacn_nhom12/encoder/encoder_tbb.joblib")
encoder_tn = joblib.load("F:/do_an/dacn_nhom12/encoder/encoder_tn.joblib")
encoder_dh = joblib.load("F:/do_an/dacn_nhom12/encoder/encoder_dh.joblib")

tbb =pd.read_csv("F:/do_an/dacn_nhom12/data/data_train/tbb.csv")
# df.drop(['Thời điểm', 'Qxt', 'Qxm', 'Ncxs', 'Ncxm' ], axis=1, inplace=True)
tn = pd.read_csv('F:/do_an/dacn_nhom12/data/data_train/tn.csv')
dh = pd.read_csv('F:/do_an/dacn_nhom12/data/data_train/dh.csv')

# Tiêu đề ứng dụng
st.title('Ứng Dụng Web dự đoán lưu lượng xả của các hồ thủy điện')

# Tạo hai ô chọn (dropdown)
option1 = st.selectbox(
    'Chọn vùng:',
    ['Tây Bắc Bộ', 'Duyên Hải Nam Trung Bộ', 'Tây Nguyên']
)
if option1 == 'Tây Bắc Bộ':
    tenho = tbb['tên hồ'].unique()
    model = model_tbb
    scaler = scaler_tbb
    encoder = encoder_tbb
elif option1 == 'Duyên Hải Nam Trung Bộ':
    tenho = dh['tên hồ'].unique()
    model = model_dh
    scaler = scaler_dh
    encoder = encoder_dh
else: 
    tenho = tn['tên hồ'].unique()
    model = model_tn
    scaler = scaler_tn
    encoder = encoder_tn
    
option2 = st.selectbox(
    'Chọn hồ thủy điện',
    tenho
)

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


input1 = st.text_input('Nhập lưu lượng đến hồ(Qve):')
input2 = st.text_input('Nhập tổng lượng xả qua đập tràn(Qxm):')
input3 = st.text_input('Nhập tổng lượng xả qua nhà máy(Qxt):')

if is_float(input1)== False and input1 != '':
    st.write('Ô 1dữ liệu phải là số')

if is_float(input2) == False and input2 != '':
    st.write('Ô 2 dữ liệu phải là số')

if is_float(input3)== False and input3 != '':
    st.write('Ô 3 dữ liệu phải là số.')
    
if st.button("Dự đoán"):
    if input2 == '' and input1 == '' and input3 == '':
        st.write("Nhập đầy đủ thông tin trước khi dự đoán")
    else:
        df = {
        'tên hồ': [option2],
        'Qve': [input1],
        'Qxt': [input3],
        'Qxm': [input2]
        }
        df = pd.DataFrame(df)
        # print("Danh mục của encoder:", encoder.categories_)
        df['tên hồ'] = encoder.transform(df[['tên hồ']])
        # data = pd.concat([df, pd.DataFrame(station_encoded, columns=encoder.get_feature_names_out(['tên hồ']))], axis=1)
        X_train = scaler.transform(df)
        st.write("Tổng lượng nước xả dự báo: ", model.predict(X_train))
        
