# app.py
import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. Ladda API-nyckel från .env-filen
load_dotenv()
try:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
except Exception as e:
    st.error(f"Kunde inte ladda OpenAI klient: {e}")
    st.stop()


# 2. Huvudfunktion för AI-logik
def analyze_match(cv_text, job_description):
    """Anropar OpenAI API för att analysera matchningen."""
    
    # Detaljerad prompt engineering för att få ett bra svar
    prompt = f"""
    Du är en expertrekryterare och din uppgift är att analysera hur väl ett givet CV matchar en jobbannons.

    1. Skapa en matchningsprocent (endast siffra, t.ex. 85).
    2. Ge en kort sammanfattning (2-3 meningar) av de starkaste matchningarna.
    3. Ge 3-5 konkreta och konstruktiva förslag på hur kandidaten kan förbättra sitt CV för att bättre passa denna specifika jobbannons.

    ---
    JOBBANNONS:
    {job_description}

    ---
    CV:
    {cv_text}

    ---
    Formatet på ditt svar ska vara:

    MATCH: [Procent]%
    SAMMANFATTNING: [Din korta text]
    FÖRSLAG: 
    1. [Förslag 1]
    2. [Förslag 2]
    ...
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Du kan uppgradera till gpt-4o för bättre resultat
            messages=[
                {"role": "system", "content": "Du är en AI-assistent som analyserar CV och jobbannonser."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ett fel uppstod vid anrop till OpenAI API: {e}"


# 3. Streamlit Gränssnitt
st.set_page_config(page_title="AI CV Matchare", layout="wide")
st.title("🤖 AI-driven CV & Jobbannons Matchare")
st.markdown("Klistra in en jobbannons och ditt CV nedan för att se hur väl du matchar och få förslag på förbättringar.")

col1, col2 = st.columns(2)

with col1:
    job_description = st.text_area("📋 Klistra in Jobbannons", height=300)

with col2:
    cv_text = st.text_area("👤 Klistra in ditt CV (textform)", height=300)

if st.button("🚀 Analysera Matchning"):
    if not job_description or not cv_text:
        st.warning("Vänligen klistra in både jobbannonsen och CV-texten.")
    else:
        with st.spinner("Analyserar din matchning... detta kan ta en stund..."):
            result = analyze_match(cv_text, job_description)
            
            st.subheader("📊 Analysresultat")
            
            # Försök att extrahera och formatera resultatet snyggt
            try:
                # Delar upp svaret baserat på de definierade rubrikerna i prompten
                match_line, summary_line, suggestions_header, *suggestions = result.strip().split('\n')
                
                # Visa Matchningsprocent
                match_percent = match_line.split(':')[1].strip()
                if "%" in match_percent:
                     # Försöker visa det som en snygg mätare om möjligt
                    try:
                        st.progress(int(match_percent.replace('%', '').strip()) / 100)
                    except:
                        pass # Fallback
                st.info(f"**{match_line.split(':')[0].strip()}:** {match_percent}")

                # Visa Sammanfattning
                st.success(f"**{summary_line.split(':')[0].strip()}:** {summary_line.split(':')[1].strip()}")
                
                # Visa Förslag
                st.markdown(f"**{suggestions_header.strip()}**")
                for suggestion in suggestions:
                    if suggestion.strip(): # Undvik tomma rader
                        st.markdown(suggestion.strip())

            except:
                # Fallback om promptformatet inte följdes exakt
                st.text(result)