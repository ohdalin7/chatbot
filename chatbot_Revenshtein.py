import pandas as pd
#import Levenshtein  # pip install python-Levenshtein
# 사용자 정의 레벤슈타인 거리 함수 가져오기
from Levenshtein_Distance import calc_distance   # type: ignore

# 챗봇 클래스 정의
class SimpleChatBot:
    def __init__(self, filepath):
        # 질문과 답변 데이터를 불러옴
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    # 사용자 입력과 학습 질문들 사이의 레벤슈타인 거리 계산
    def find_best_answer(self, input_sentence):
         # 입력 문장과 가장 유사한 질문을 찾아 해당 답변 반환 사
        distances = [calc_distance(input_sentence, q) for q in self.questions]
        best_match_index = distances.index(min(distances))  # 최소 거리의 인덱스
        return self.answers[best_match_index]  # 해당 인덱스의 답변 반환

# 파일 경로 설정
filepath = 'c:/Users/ohdalin/OneDrive/chatbot/ChatbotData.csv'
# 챗봇 객체 생성
chatbot = SimpleChatBot(filepath)

# 사용자 입력 처리 루프
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)