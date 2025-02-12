import base64

import streamlit as st

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(verbose=True)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

def main():
    st.title("音声文字起こしアプリ")

    uploaded_file = st.file_uploader("音声ファイルを選択", type=["m4a", "mp3", "wav"])

    if uploaded_file is not None:
        st.audio(uploaded_file)

        if st.button("文字起こしを開始"):
            with st.spinner("文字起こしを実行中..."):
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=uploaded_file
                )
            st.success("文字起こしが完了しました")

            res = transcription.text
            st.write(res)

            encoded = base64.b64encode(res.encode()).decode()

            st.markdown(
                f'<a href="data:file/txt;base64,{encoded}" download="transcript.txt">ダウンロード</a>',
                unsafe_allow_html=True,
            )

if __name__ == "__main__":
    main()
