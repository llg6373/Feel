from cnsenti import Sentiment
from cnsenti import Emotion

senti = Sentiment()
emotion = Emotion()
test_text = '今天上海天气真差,非常讨厌下雨,把我冻坏了,心情太不高兴了,不高兴,我真的很生气！'
result1 = senti.sentiment_count(test_text)
result2 = senti.sentiment_calculate(test_text)
result3 = emotion.emotion_count(test_text)
print('sentiment_count', result1)
print('sentiment_calculate', result2)
print('emotion_count',result3)
