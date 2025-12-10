class Chatbot:
     WEATHER_URL = "https://www.timeanddate.com/weather/france/auxerre"
    
     def __init__(self):
        self.positive_words = {
            'bien', 'super', 'genial', 'excellent', 'magnifique', 'fantastique', 'sympa', 'splendide'
        }

        self.negative_words = {
            'mal', 'nul', 'mauvais', 'eclaté', 'pourri', 'horrible', 'terrible', 'je suis triste'
        }

        self.expressions_negative = [
            "je suis triste"
        ]

        self.words = ''

     def get_score(self, list_words, check_words):
        return sum(1 for word in check_words if word in list_words)

     def analyze(self):
        words = self.words.lower().split()

        sentiments_count = {
            'positive': self.get_score(self.positive_words, words),
            'negative': self.get_score(self.negative_words, words),
        }

        total = sum(sentiments_count.values())

        if total == 0:
            return {'dominant': 'neutre', 'scores': sentiments_count}

        dominant = max(sentiments_count, key=sentiments_count.get)
        return {'dominant': dominant, 'scores': sentiments_count}
     
     def respond(self, sentiment):
        if sentiment == 'positive':
            return "super je suis content que tu aille bien  ! "
        elif sentiment == 'negative':
            return "ah oui raconte ce qui ne vas pas ."
        else:
            return "la plui c est comme mes emotion ça tombe sans prevenir mais au moin sa arrose quelque chose "
        
        
        




     def run(self):
        self.words = input("Bonjour ! Comment tu vas aujourd’hui en ce temps pluvieux sur Auxerre ? ")

        result = self.analyze()
        reply = self.respond(result["dominant"])
        print(reply)

        message = input("> ")
        special_reply = Chatbot.repondre(message)
        if special_reply:
            print(special_reply)
     @staticmethod
     def repondre(message):
        if message == "je suis triste":
               return " La pluie, c est comme mes emotions, ça tombe sans prevenir, mais au moins ça arrose quelque chose "
        if message == "je suis fatigué":
               return  "la vie c est durrrrrrr "
        print("https://www.timeanddate.com/weather/france/auxerre")
        

bot = Chatbot()
bot.run()
