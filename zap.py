import streamlit as st
from urllib.parse import quote, urlencode

# Configuração inicial do app
st.set_page_config(page_title="Gerador de Links WhatsApp", layout="centered")
st.sidebar.header(("Mkt Hub :peach:"))
hub_firenze = st.sidebar.selectbox('', ['Link WhatsApp', 'Gerador de UTM',], 0)


st.sidebar.header(("Sobre o autor :copyright:"))
st.sidebar.markdown((
    """
Desenvolvi esse hub de ferramentas com a ideia de tornar acessível e sem anúncios! 
- [Instagram](https://www.instagram.com/owemersonsilva_/) By Wemerson Silva
- [Linkedin](https://www.linkedin.com/in/wemerson-silva-5098071a9/) By Wemerson Silva
- [Site](https://www.eudine.com.br/?utm_source=streamlit&utm_medium=mkt-hub&utm_campaign=sidebar) By Eudine Brasil
"""
))

if hub_firenze == 'Link WhatsApp':

    # Título do app
    st.title("Zap Links - Gerador de Links do WhatsApp :calling:")

    # Seção de entrada de dados
    st.header("Crie seu link personalizado:")
    phone_number = st.text_input("Número de telefone (Digite somente o código de área):", placeholder="Ex: 11999999999")
    message = st.text_area("Mensagem:", placeholder="Digite sua mensagem aqui...")

    # Botão para gerar o link
    if st.button("Gerar Link"):
        # Codificar a mensagem para o formato URL
        encoded_message = quote(message) if message else ""
        
        # Construir o link
        if phone_number:
            link = f"https://wa.me/{phone_number}?text={encoded_message}"
        else:
            link = f"https://wa.me/?text={encoded_message}"
        
        # Mostrar o link gerado
        st.success("Link gerado com sucesso!")
        st.code(link, language="text")

       
    
if hub_firenze == 'Gerador de UTM':

    # Título do aplicativo
    st.title("UTM Tracker - Gerador de UTM :signal_strength:")

    # Formulário de entrada de dados
    with st.form("utm_form"):
        st.header("Insira os parâmetros abaixo:")

        # Campos de entrada
        site_url = st.text_input("Link do site:", placeholder="https://www.seusite.com")
        utm_source = st.text_input("UTM source:", placeholder="Ex: google")
        utm_medium = st.text_input("UTM medium:", placeholder="Ex: cpc")
        utm_campaign = st.text_input("UTM campaign:", placeholder="Ex: promocao-verao")
        utm_term = st.text_input("UTM term (opcional):", placeholder="Ex: sapatos")
        utm_content = st.text_input("UTM content (opcional):", placeholder="Ex: banner-1")

        # Botão de submissão
        submitted = st.form_submit_button("Gerar UTM")

    # Lógica para gerar o link com UTM
    if submitted:
        if not site_url:
            st.error("O link do site é obrigatório!")
        else:
            # Dicionário com os parâmetros
            utm_params = {
                "utm_source": utm_source,
                "utm_medium": utm_medium,
                "utm_campaign": utm_campaign,
                "utm_term": utm_term if utm_term else None,
                "utm_content": utm_content if utm_content else None,
            }
            # Remover parâmetros vazios
            utm_params = {key: value for key, value in utm_params.items() if value}

            # Construir a URL final
            utm_url = f"{site_url}?{urlencode(utm_params)}"

            # Exibir o resultado
            st.success("URL com UTM gerada com sucesso!")
            st.code(utm_url, language="text")

        
