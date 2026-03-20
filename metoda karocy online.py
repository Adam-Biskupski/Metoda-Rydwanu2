import streamlit as st
import random

# Twoje dane (skrócone dla przejrzystości w przykładzie, użyj swojej pełnej listy)
biblia = {
    "Księga Rodzaju": 50, "Księga Wyjścia": 40, "Księga Kapłańska": 27, "Księga Liczb": 36, "Księga Powtórzonego Prawa": 34,
    "Księga Jozuego": 24, "Księga Sędziów": 21, "Księga Rut": 4, "1 Księga Samuela": 31, "2 Księga Samuela": 24,
    "1 Księga Królewska": 22, "2 Księga Królewska": 25, "1 Księga Kronik": 29, "2 Księga Kronik": 36, "Księga Ezdrasza": 10,
    "Księga Nehemiasza": 13, "Księga Tobiasza": 14, "Księga Judyty": 16, "Księga Estery": 16, "1 Księga Machabejska": 16, "2 Księga Machabejska": 15,
    "Księga Hioba": 42, "Księga Psalmów": 150, "Księga Przysłów": 31, "Księga Koheleta": 12, "Pieśń nad Pieśniami": 8,
    "Księga Mądrości": 19, "Mądrość Syracha": 51, "Księga Izajasza": 66, "Księga Jeremiasza": 52, "Lamentacje": 5,
    "Księga Barucha": 6, "Księga Ezechiela": 48, "Księga Daniela": 14, "Księga Ozeasza": 14, "Księga Joela": 3,
    "Księga Amosa": 9, "Księga Abdiasza": 1, "Księga Jonasza": 4, "Księga Micheasza": 7, "Księga Nahuma": 3,
    "Księga Habakuka": 3, "Księga Sofoniasza": 3, "Księga Aggeusza": 2, "Księga Zachariasza": 14, "Księga Malachiasza": 4,
    "Ewangelia św. Mateusza": 28, "Ewangelia św. Marka": 16, "Ewangelia św. Łukasza": 24, "Ewangelia św. Jana": 21,
    "Dzieje Apostolskie": 28, "List do Rzymian": 16, "1 List do Koryntian": 16, "2 List do Koryntian": 13,
    "List do Galatów": 6, "List do Efezjan": 6, "List do Filipian": 4, "List do Kolosan": 4, "1 List do Tesaloniczan": 5,
    "2 List do Tesaloniczan": 3, "1 List do Tymoteusza": 6, "2 List do Tymoteusza": 4, "List do Tytusa": 3,
    "List do Filemona": 1, "List do Hebrajczyków": 13, "List św. Jakuba": 5, "1 List św. Piotra": 5,
    "2 List św. Piotra": 3, "1 List św. Jana": 5, "2 List św. Jana": 1, "3 List św. Jana": 1, "List św. Judy": 1, "Apokalipsa św. Jana": 22
}

# Grupowanie
items = list(biblia.items())
groups = [items[:5], items[5:21], items[21:46], items[46:]]

def wybierz_rozdzial(grupa, numer):
    wszystkie = []
    for ksiega, liczba in grupa:
        for i in range(1, liczba + 1):
            wszystkie.append(f"{ksiega} – rozdział {i}")
    indeks = (numer - 1) % len(wszystkie)
    return wszystkie[indeks]

# Interfejs Streamlit
st.title("📖 Generator rozdziałów Biblii")

col1, col2 = st.columns([2, 1])

with col1:
    numer_input = st.number_input("Podaj numer (1-187):", min_value=1, max_value=187, value=1)

if st.button("Losuj numer 🎲"):
    numer_input = random.randint(1, 187)
    st.info(f"Wylosowano numer: {numer_input}")

st.divider()

for i, grupa in enumerate(groups, start=1):
    wynik = wybierz_rozdzial(grupa, numer_input)
    st.subheader(f"Część {i}")
    st.write(wynik)