import requests
from bs4 import BeautifulSoup
import random

class Chatbot:
    def __init__(self):
      
        self.positive_words = {
            'bien', 'super', 'genial', 'excellent', 'magnifique', 'fantastique', 'sympa', 'splendide'
        }

        self.negative_words = {
            'mal', 'nul', 'mauvais', 'eclaté', 'pourri', 'horrible', 'terrible', 'triste'
        }

        self.words = ''

       
        self.quotes = self.scrape_quotes()

    def scrape_quotes(self):
        url = "https://quotes.toscrape.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes_list = []

        for div in soup.select("div.quote"):
            genre = div.select_one("span.text").get_text()
            auteur = div.select_one("small.author").get_text()
            tags = [a.get_text() for a in div.select("div.tags a.tag")]

            quotes_list.append({
                "genre": genre,
                "auteur": auteur,
                "tags": tags
            })

        return quotes_list

    def get_random_quote(self):
        return random.choice(self.quotes)

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
            return "Super, je suis content que tu ailles bien !"
        elif sentiment == 'negative':
            return "Ah… raconte-moi ce qui ne va pas."
        else:
            return "D’accord, je t’écoute."

    
    def run(self):
        self.words = input("Salut ! Comment tu vas aujourd’hui ? ")

        result = self.analyze()
        reply = self.respond(result["dominant"])
        print("\n" + reply)

        quote = self.get_random_quote()
        print(f"\n Citation du jour :\n{quote['genre']}\n— {quote['auteur']}")
        print(f"Tags : {', '.join(quote['tags'])}\n")

bot = Chatbot()
bot.run()
