from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote, scheme_chars
import pandas as pd
import time

# 리뷰 정보 dataframe에 넣어서 반환
def get_moive_reviews(datanum):
    
    movie_review_df = pd.DataFrame(columns=("Review", "Score", "Label"))
    idx = 0
    is_positive = 0
    is_negative = 0
    url = "https://movie.naver.com/movie/point/af/list.naver?&page=1"

    i=0
    while True:
        movie_page = urllib.request.urlopen(url).read()
        movie_page_soup = BeautifulSoup(movie_page, 'html.parser')

        review_list = movie_page_soup.find_all('td', {'class' : 'title'})
        
        # 리뷰 정보(리뷰, 별점) + label 구분
        for review in review_list:
            score = review.find('em').get_text()
            # score 0~5: negative, 6~10: positive
            if(int(score) > 5): label = 1
            elif(int(score) <= 5): label = 0
            # 긍/부정 비율 맞추기
            if(is_positive == datanum and label == 1): break;
            review_text = review.find('a', {'class' : 'report'}).get('onclick').split("', '")[2]
            if(review_text == ""): break
            movie_review_df.loc[idx] = [review_text, score, label]
            idx += 1
            if(label == 1): is_positive += 1
            elif(label == 0): is_negative += 1
            
            print(is_positive)
            print(is_negative)
            print(f"idx = {idx}")
            

        if idx>=datanum: break
        # 다음 페이지 넘어가기
        time.sleep(0.2)
        url = "https://movie.naver.com" + movie_page_soup.find('a', {'class' : 'pg_next'}).get('href')

    return movie_review_df

# 원하는 긍/부정 데이터 양 입력
movie_review_df = get_moive_reviews(100)
movie_review_df.to_csv("test.csv", encoding=('utf-8-sig'))