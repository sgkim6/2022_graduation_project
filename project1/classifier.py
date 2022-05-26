import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from transformers import TextClassificationPipeline
from transformers import BertTokenizerFast
from transformers import TFBertForSequenceClassification


# 모델 로드하기
def load_model():    
    loaded_tokenizer = BertTokenizerFast.from_pretrained('nsmc_model/bert-base')
    loaded_model = TFBertForSequenceClassification.from_pretrained('nsmc_model/bert-base')
    text_classifier = TextClassificationPipeline(
        tokenizer=loaded_tokenizer, 
        model=loaded_model, 
        framework='tf',
        return_all_scores=True
    )
    return text_classifier

#텍스트 분류기 정의


model_name = "tf_model.h5"

#텍스트 분류기
def classifier(sentence):
    text_classifier = load_model()
    score = text_classifier(sentence)[0][1]['score']
    senti = ''
    if score >= 0.5:
        senti='긍정'
    else:
        senti='부정'

    if senti=='부정':
        score = 1-score
    score = round(score,4)
    score = score*100

    # print(f"입력된 문장 : {sentence}")
    # print(f"문장 길이 : {len(sentence)}")
    # print(f"{score}% 확률로 {senti} 문장입니다.")

    return {'senti' : senti, 'score' : score}