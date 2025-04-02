import difflib
import streamlit as st
 
class BehoerdenChat:
    def __init__(self):
        self.fragen_und_antworten = {
            "Produzent": "Das ist jemand, der etwas herstellt.",
            "Importeur": "Das ist jemand, der Waren aus einem anderen Land bringt.",
            "Erzeugnis": "Das ist ein Produkt oder eine Ware.",
            "Registrierungsdossier": "Das ist ein Ordner mit wichtigen Infos, die man bei einer Behörde abgeben muss.",
            "Exposition": "Das bedeutet, dass Menschen oder die Natur mit einem Stoff in Kontakt kommen.",
            "Freisetzung": "Das bedeutet, dass ein Stoff in die Luft, ins Wasser oder auf den Boden gelangt.",
            "vernünftigerweise": "So, wie es logisch und sinnvoll erscheint.",
            "vernünftige": "So, wie es logisch und sinnvoll erscheint.",
            "vernünftigen": "So, wie es logisch und sinnvoll erscheint.",
            "vorhersehbar": "So, dass man es erwarten kann.",
            "vorhersehbare": "So, dass man es erwarten kann.",
            "vorhersehbaren": "So, dass man es erwarten kann.",
            "Verwendungsbedingungen": "So, wie man es normalerweise benutzt.",
            "enthalten": "Etwas ist in etwas drin.",
            "freigesetzt": "Etwas wird herausgelassen.",
            "freigesetzt werden": "Etwas kommt nach draußen.",
            "reicht ein": "Gibt etwas bei einer Behörde ab.",
            "Entsorgung": "Wenn man etwas wegwirft oder beseitigt.",
            "einschließlich der Entsorgung": "Auch, wenn man es wegwirft oder beseitigt.",
            "Exposition von Mensch und Umwelt": "Menschen oder die Natur kommen mit einem Stoff in Kontakt.",
            "ausschließen": "Etwas unmöglich machen.",
            "gilt": "Etwas ist gültig oder trifft zu.",
            "gilt nicht": "Etwas trifft nicht zu oder ist nicht gültig.",
            "Abnehmer": "Jemand, der ein Produkt kauft oder bekommt.",
            "Stoffe": "Bestimmte Materialien oder chemische Substanzen.",
            "registriert": "Offiziell angemeldet.",
            "betreffend": "Zu einem bestimmten Thema gehörend.",
            "für die betreffende Verwendung": "Für genau diese Nutzung.",
            "Verwendung": "Wie man etwas benutzt.",
            "Absätze": "Abschnitte in einem Text.",
            "Der Produzent oder Importeur von Erzeugnissen reicht ein Registrierungsdossier ein.": "Der Hersteller oder Händler muss Papiere bei der Behörde abgeben.",
            "Der Stoff ist in einer Menge von mehr als 1 Tonne pro Jahr enthalten.": "Es gibt mehr als 1.000 kg von dem Stoff pro Jahr.",
            "Der Stoff soll unter normalen oder vernünftigerweise vorhersehbaren Verwendungsbedingungen freigesetzt werden.": "Der Stoff kommt wahrscheinlich raus, wenn man das Produkt normal benutzt.",
            "Absatz 2 gilt nicht, wenn der Produzent oder Importeur eine Exposition ausschließen kann.": "Die Regel in Absatz 2 gilt nicht, wenn der Stoff sicher eingeschlossen bleibt.",
            "Die Absätze 1 bis 5 gelten nicht für Stoffe, die bereits registriert wurden.": "Wenn ein Stoff schon angemeldet ist, muss man nichts mehr tun."
        }
    def frage_stellen(self, frage):
        if frage in self.fragen_und_antworten:
            return self.fragen_und_antworten[frage]
        else:
            moeglichkeiten = difflib.get_close_matches(frage, self.fragen_und_antworten.keys(), n=1, cutoff=0.7)
            if moeglichkeiten:
                return f"Meintest du '{moeglichkeiten[0]}'? {self.fragen_und_antworten[moeglichkeiten[0]]}"
            else:
                return "Ich kenne das Wort oder den Satz nicht. Kannst du es anders sagen?"
 
# Streamlit Web-App
st.title("🛂 Behörden-Chat: Verordnungen einfach erklärt")
st.write("Gib ein Wort oder einen Satz ein, um eine einfache Erklärung zu erhalten.")
 
chat = BehoerdenChat()
 
user_input = st.text_input("Deine Frage:")
if user_input:
    antwort = chat.frage_stellen(user_input)
    st.write(f"**Antwort:** {antwort}")
 
st.markdown("---")
st.write("🔹 **Beispielwörter:** Produzent, Importeur, Exposition, Freisetzung, Entsorgung")
st.write("🔹 **Beispielsätze:** 'Der Stoff ist in einer Menge von mehr als 1 Tonne pro Jahr enthalten.'")