from django.db import models

# 질문 모델(테이블)


class Question(models.Model):
    subject = models.CharField(max_length=200)      #문자필드(최대200자)
    content = models.TextField()                    #텍스트필드
    create_date = models.DateTimeField()            #날짜필드

    def __str__(self):
        return self.subject
# 답변 모델(테이블)



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # on_delete = models.CASCADE : 외래키 제약조건 무시하고 연쇄 삭제
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return str(self.question)