def carrega_dados_agua():
    url_agua_2019 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2019.csv"
    url_agua_2020 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2020.csv"
    url_agua_2021 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2021.csv"
    url_agua_2022 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2022.csv"
    url_agua_2023 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2023.csv"
    url_agua_2024 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2024.csv"

    # Carregar os dados diretamente dos links do GitHub
    df_censo_ac_agua_2019 = pd.read_csv(url_agua_2019, delimiter=';', encoding='utf-8', low_memory=False)
    df_censo_ac_agua_2020 = pd.read_csv(url_agua_2020, delimiter=';', encoding='utf-8', low_memory=False)
    df_censo_ac_agua_2021 = pd.read_csv(url_agua_2021, delimiter=';', encoding='utf-8', low_memory=False)
    df_censo_ac_agua_2022 = pd.read_csv(url_agua_2022, delimiter=';', encoding='utf-8', low_memory=False)
    df_censo_ac_agua_2023 = pd.read_csv(url_agua_2023, delimiter=';', encoding='utf-8', low_memory=False)
    df_censo_ac_agua_2024 = pd.read_csv(url_agua_2024, delimiter=';', encoding='utf-8', low_memory=False)

    # Combina todos os dataframes em um único dataframe
    df_combined = pd.concat([
        df_censo_ac_agua_2019,
        df_censo_ac_agua_2020,
        df_censo_ac_agua_2021,
        df_censo_ac_agua_2022,
        df_censo_ac_agua_2023,
        df_censo_ac_agua_2024
])
    return df_combined