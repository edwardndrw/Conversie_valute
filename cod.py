import streamlit as st
import requests

# Endpoint-ul API
API_URL = "https://open.er-api.com/v6/latest/"

# Titlul aplicației cu stilizare personalizată
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #ff5722; font-family: 'Arial', sans-serif;">Convertor Valutar</h1>
        <p style="font-size: 18px; color: #616161;">Convertește orice sumă între valute, folosind ratele de schimb actualizate în timp real.</p>
    </div>
""", unsafe_allow_html=True)

# CSS personalizat pentru stilizare
st.markdown("""
    <style>
        /* Culoare de fundal pentru corp */
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }

        /* Stiluri pentru butoane */
        .stButton>button {
            background-color: #ff5722;
            color: white;
            border-radius: 50px;
            padding: 12px 25px;
            font-size: 18px;
            transition: all 0.3s ease;
            width: 100%;
            border: none;
        }
        .stButton>button:hover {
            background-color: #f44336;
            transform: scale(1.1);
            color: white !important;
        }

        /* Stiluri personalizate pentru câmpurile de input */
        .stNumberInput>div>div>input {
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            width: 100%;
        }

        /* Efect de tranziție fade-in */
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }

        /* Butonul Reverse cu iconiță */
        .reverse-button {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #3f51b5;
            color: white;
            padding: 10px 20px;
            border-radius: 50px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .reverse-button:hover {
            background-color: #303f9f;
            transform: scale(1.1);
        }
        .reverse-button i {
            margin-right: 8px;
        }

        /* Stiluri personalizate pentru Selectbox */
        .stSelectbox>div>div>input {
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Câmpurile de input pentru aplicație
amount = st.number_input("Sumă", min_value=0.0, format="%f", step=0.01, key="amount_input")


# Funcția pentru a obține lista de valute din API
def get_currencies():
    try:
        response = requests.get(API_URL + "USD")  # Implicit la USD pentru obținerea codurilor valutare
        data = response.json()
        if "rates" in data:
            return list(data["rates"].keys())
        else:
            st.error("Nu s-au putut obține codurile valutare.")
            return []
    except Exception as e:
        st.error(f"A apărut o eroare la obținerea valutelor: {e}")
        return []


currencies = get_currencies()
if not currencies:
    st.stop()

# Definirea selecțiilor implicite pentru valute
if "from_currency" not in st.session_state:
    st.session_state.from_currency = "USD"
if "to_currency" not in st.session_state:
    st.session_state.to_currency = "EUR"


# Logică pentru a schimba valutele
def reverse_currencies():
    st.session_state.from_currency, st.session_state.to_currency = (
        st.session_state.to_currency,
        st.session_state.from_currency,
    )


# Layout cu două coloane pentru butoanele Convert și Reverse
col1, col2 = st.columns(2)
with col1:
    if st.button("Convertește", key="convert_button"):
        from_currency = st.session_state.from_currency
        to_currency = st.session_state.to_currency

        if from_currency == to_currency:
            st.write(f"{amount} {from_currency} = {amount} {to_currency}")
        else:
            try:
                # Obține ratele de schimb de la API
                response = requests.get(API_URL + from_currency)
                data = response.json()

                # Realizează conversia
                if "rates" in data:
                    rate = data["rates"].get(to_currency)
                    if rate:
                        converted_amount = amount * rate
                        st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                    else:
                        st.error("Ratele de conversie nu sunt disponibile.")
                else:
                    st.error("Nu s-au putut obține ratele de schimb.")
            except Exception as e:
                st.error(f"A apărut o eroare: {e}")

with col2:
    # Butonul Reverse
    if st.button("Inversează", key="reverse_button"):
        reverse_currencies()

# Selectoare de valute
st.markdown("<hr>", unsafe_allow_html=True)  # Divider
col1, col2 = st.columns(2)

with col1:
    st.session_state.from_currency = st.selectbox(
        "Din",
        currencies,
        index=currencies.index(st.session_state.from_currency),
        key="from_currency_select",
        format_func=lambda x: f"{x}",
    )

with col2:
    st.session_state.to_currency = st.selectbox(
        "În",
        currencies,
        index=currencies.index(st.session_state.to_currency),
        key="to_currency_select",
        format_func=lambda x: f"{x}",
    )

#Afișează tabelul cu ratele de schimb
st.subheader("Tabel cu ratele de schimb")


def get_exchange_rates(base_currency):
    try:
        response = requests.get(API_URL + base_currency)
        data = response.json()
        if "rates" in data:
            return data["rates"]
        else:
            st.error("Nu s-au putut obține ratele de schimb.")
            return {}
    except Exception as e:
        st.error(f"A apărut o eroare la obținerea ratelor de schimb: {e}")
        return {}


if st.checkbox("Afișează Tabelul cu Ratele de Schimb"):
    rates = get_exchange_rates(st.session_state.from_currency)
    if rates:
        st.write(f"Ratele de schimb pentru 1 {st.session_state.from_currency}:")
        st.table(rates)