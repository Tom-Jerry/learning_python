#-*- coding: utf-8 -*- 
class AnonymousSurvey():
    def __init__(self,question):
        self.question = question
        self.responses = []
    
    def show_questions(self):
        print(question)

    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_result(self):
        print("Survry results:")
        for response in responses:
            print('-' + response)