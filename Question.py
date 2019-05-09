class Question:
    def __init__(self, prompt, answer):

        self.prompt = prompt
        self.answer = answer

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False