import requests
from flask import Flask, render_template, request #importerar flask, render_template kopplar phytonlogiken med html mallar, 
#request ändrar inehållet, seatch och language

app = Flask(__name__) #det blir en flask instans och en app skapas

API_KEY = "28dfe787a4f70e337d24d4f4dc09fcfd" #api koden

# Hämta nyheter baserat på språk och sökterm
def fetch_news(query, language="sv"): #skapar funktionen fetch_news och parametrarna 
    url = f"https://gnews.io/api/v4/search?q={query}&lang={language}&apikey={API_KEY}"# f stringen kommer ändra sökningen kommer ändras beroende på requesten.
    try: #felhantering
        response = requests.get(url, timeout=5)#om apin inte fungerar efter 5 sekunder så avbryts det. annars sparas svaret
        response.raise_for_status()  # tittar så att svaret är ok, ska va 200
        articles = response.json().get("articles", [])#svarat blir till pyton dictonary fron json.hämtar nyhetsartiklar. annars tom lista
        return articles if articles else None  # returnera artiklar om de finns
    except Exception:
        return None #om det inte fungerar så returnera None

@app.route("/", methods=["GET", "POST"])# en "route skapas. get och post är metoder som kan användas. get för att visa sidan och post för att ändra sidan/skicka data
def index():
    query = "Exempel"  # start sökning om inget skrivs in
    language = "sv"  # standard språk är svenska


    if request.method == "POST": #tittar om användaren vill söka eller ändra språk, formuläär med post begäran. annars hoppar den över
        query = request.form.get("search", query)  # hämtar användarens sökning
        language = request.form.get("language", "sv")  # hämtar språket

   
    articles = fetch_news(query, language) #skickar med rätt värden på query och language till funktionen fetch_news
    error_message = None if articles else "Kan inte hämta datan nu" #om datan inte hittas så skickar den ett felmeddelande

    return render_template("index.html", articles=articles, query=query, error_message=error_message, language=language)
    #visar själva html med render. lagrar värdet på variabeln så html kan använda den.
    
if __name__ == "__main__":
    app.run(debug=True) 
