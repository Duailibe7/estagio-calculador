import streamlit as st

st.set_page_config(page_title="Calculadora de Ponto Medial", page_icon="🦾")

st.title('🦾 Calculadora de Ponto Medial do Braço')

st.subheader('Preencha os dados do paciente')

nome = st.text_input('Nome do paciente')

altura = st.number_input('Altura do ombro ao cotovelo (em cm)', min_value=0.0, step=0.1)

if st.button('Calcular ponto medial'):
    if nome and altura > 0:
        media = altura / 2
        st.success(f'✅ Como {nome} tem {altura} cm de braço, o ponto medial é **{media:.1f} cm**.')
    else:
        st.error('⚠️ Preencha todos os campos corretamente.')
