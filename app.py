import streamlit as st
from PIL import Image

st.set_page_config(page_title="Calculadora de Ponto Medial", page_icon="🦾")

st.title('🦾 Calculadora de Ponto Medial do Braço')

st.subheader('Preencha os dados do paciente')

# Input do nome
nome = st.text_input('Nome do paciente')

# Escolha da unidade
unidade = st.selectbox('Selecione a unidade de medida', ['Centímetros (cm)', 'Polegadas (in)'])

# Input da altura
altura = st.number_input(f'Altura do ombro ao cotovelo (em {unidade})', min_value=0.0, step=0.1)

# Botões lado a lado
col1, col2 = st.columns(2)

with col1:
    calcular = st.button('Calcular ponto medial')

with col2:
    limpar = st.button('Limpar campos')

if limpar:
    # Para "limpar" os campos, a forma simples é recarregar a página, ou usar sessão (mais avançado)
    st.experimental_rerun()

if calcular:
    if nome and altura > 0:
        media = altura / 2
        st.success(f'✅ Como {nome} tem {altura:.2f} {unidade.split()[0]}, o ponto medial é **{media:.2f} {unidade.split()[0]}**.')

        # Mostrar imagem com explicação
        # (coloque uma imagem que tenha no seu projeto, ou use uma URL de imagem)
        try:
            # Tente abrir uma imagem local chamada "braco.png"
            img = Image.open('braco.png')
            st.image(img, caption='Ponto medial do braço', use_column_width=True)
        except:
            st.info('Imagem ilustrativa não encontrada, coloque o arquivo "braco.png" na mesma pasta do app.')

    else:
        st.error('⚠️ Preencha todos os campos corretamente.')
