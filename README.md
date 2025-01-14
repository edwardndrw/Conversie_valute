

## Descriere
Această aplicație "Convertor Valutar" este construită folosind **Streamlit** și permite utilizatorilor să convertească sume între diferite valute, utilizând rate de schimb actualizate în timp real. Datele sunt preluate de la un API public de schimb valutar.

---

## Pași pentru rulare

### 1. **Asigurați-vă că aveți instalate toate cerințele necesare**
Aplicația are nevoie de următoarele module Python pentru a funcționa:
- **Streamlit**: Pentru interfața utilizator.
- **Requests**: Pentru a prelua datele de la API.

Instalați-le cu următoarea comandă:
```bash
pip install streamlit requests
```

---


### 2. **Setările API**
Aplicația folosește următorul API public pentru a obține ratele de schimb:
- **Endpoint API**: `https://open.er-api.com/v6/latest/`
  
Asigurați-vă că aveți acces la internet pentru a comunica cu acest API.

---

### 3. **Lansarea aplicației**
Rulați aplicația folosind comanda:
```bash
streamlit run convertor_valutar.py
```

---

### 4. **Funcționalitățile aplicației**
- **Input-uri personalizate**: Introduceți suma de convertit, selectați valuta de plecare și valuta țintă.
- **Conversia valutară**: Click pe butonul "Convertește" pentru a realiza conversia.
- **Inversează valutele**: Utilizați butonul "Inversează" pentru a schimba valuta de plecare cu cea țintă.
- **Afișarea ratei de schimb**: Opțiunea de a vizualiza un tabel cu ratele de schimb pentru valuta selectată.


---

### 5. **Depanare**
- **Eroare la conectare la API**: Verificați conexiunea la internet sau disponibilitatea API-ului.
- **Module lipsă**: Asigurați-vă că toate modulele sunt instalate corect folosind `pip install`.

---



