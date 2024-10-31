import requests
import streamlit as st

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "b1e7f320-9779-11ef-8313-8118934c035d6e60b35e-4f21-4a20-bb68-10b43d4013ac"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
while True:
    #qu=input("제주도에서 관심있는 질문을 해주세요(끝내려면 나가기를 입력하세요..)>> ")
    qu=st.text_input("제주도에서 관심있는 질문을 해주세요(끝내려면 나가기를 입력하세요..)>> ",'맛집')
    
    if qu=='나가기':
        break
    demo = classify(qu)

    confidence = demo["confidence"]
    if confidence >= 60:
        break
    #print('질문을 이해하지 못했어요. 다시 질문해 주세요>>')
    st.write('질문을 이해하지 못했어요. 다시 질문해 주세요>>')

if qu != '나가기':
    label = demo["class_name"]
    if label=='food':
        #print('제주도 통돼지 삼겹살 집을 추천합니다.')
        st.write('제주도 통돼지 삼겹살 집을 추천합니다.')
    elif label=='hotplace':
        #print('제주도에는 가볼 장소가 많아요. 풍경,일출,전경을 볼 수 있어요.')
        st.write('제주도에는 가볼 장소가 많아요. 풍경,일출,전경을 볼 수 있어요.')
    elif label=='cafe':
        #print('제주도 커피가 맛있습니다. 커피향이 아주 좋아요...')
        st.write('제주도 커피가 맛있습니다. 커피향이 아주 좋아요...')
    else:
        #print('질문의 분류를 모르겠습니다.')
        st.write('질문의 분류를 모르겠습니다.')
# CHANGE THIS to do something different with the result
#print ("result: '%s' with %d%% confidence" % (label, confidence))