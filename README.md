# 🤖 AI-driven CV/Jobbannons Matchare

Detta är ett demonstrativt webbverktyg byggt med **Python** och **Streamlit** som använder **OpenAI API** för att analysera hur väl ett givet CV matchar en specificerad jobbannons.

Applikationen tillhandahåller en matchningsprocent, en sammanfattning av nyckelkompetenser samt konkreta och konstruktiva förslag på hur kandidaten kan förbättra sitt CV för att öka chanserna att bli kallad till intervju.

## ✨ Funktioner

* **Matchningsanalys:** Ger en procentuell matchning mellan CV och jobbannons.
* **Styrkeöversikt:** Sammanfattar de starkaste kompetenserna och erfarenheterna.
* **Förbättringsförslag:** Ger praktiska råd för att anpassa CV:t till jobbannonsen.
* **Enkel UI:** Använder Streamlit för ett rent och snabbt användargränssnitt.

## 🛠️ Tekniker

* **Programmeringsspråk:** Python
* **Huvudbibliotek:** `openai` (för Large Language Model-interaktion)
* **Webbramverk:** `streamlit` (för att bygga det interaktiva gränssnittet)
* **Pakethantering:** `pip`, virtuell miljö (`venv`)
* **Miljövariabler:** `python-dotenv` (för säker hantering av API-nycklar)

🚀 Kom igång (Lokal installation)
Följ dessa steg för att få en lokal kopia av projektet igång på din maskin.

1. Klona Repositoryt
Öppna din terminal eller kommandotolk och klona projektet:

Bash

git clone <din-github-repo-url>
cd ai-cv-matcher
2. Skapa och Aktivera Virtuell Miljö
Detta säkerställer att alla beroenden är isolerade från andra Python-projekt.

Bash

# Skapa miljön
python -m venv venv

# Aktivera miljön (Windows CMD)
venv\Scripts\activate.bat 

# Eller Aktivera miljön (Windows PowerShell)
.\venv\Scripts\Activate.ps1 

# Eller Aktivera miljön (macOS/Linux)
# source venv/bin/activate 
3. Installera Beroenden
Se till att den virtuella miljön är aktiv (du ser (venv) i din prompt) och installera sedan de nödvändiga paketen:

Bash

pip install openai streamlit python-dotenv
4. Konfigurera API-Nyckeln
Du behöver en giltig API-nyckel från OpenAI. Observera att OpenAI API är en betaltjänst.

Hämta din nyckel från OpenAI Platform.

Skapa en fil med namnet .env i projektets rotkatalog.

Lägg till din nyckel i filen (dessa rader kommer inte att laddas upp till GitHub tack vare .gitignore):

Kodavsnitt

# .env
OPENAI_API_KEY="din-hemliga-openai-api-nyckel-här"
5. Kör Applikationen
Starta Streamlit-servern med huvudfilen app.py:

Bash

streamlit run app.py
Applikationen öppnas automatiskt i din webbläsare (vanligtvis på http://localhost:8501).
