from voice import generate_voice
import streamlit as st
import asyncio

class App:
    def __init__(self):
        def render():
            
            #Logo
            st.logo('assets\\logo.png', size='large')
            
            #Caption
            st.markdown(
                """
                <h1 style="font-size: 13px;opacity: 40%; font-weight: 400;">
                TEXT  →  VOICE
                </h1>
                
                """, unsafe_allow_html=True
            )
            
            
            #Caption
            st.markdown(
                """
                <h1 style="font-family: inter;font-size: 35px;font-weight:300;">
                Turn any manuscript into a</br><span style='color:#F59E0B;font-style:italic;font-weight:800;'>studio‑quality</span> narration.
                </h1>
                
                """, unsafe_allow_html=True
            )
            
            
            #Text area styling
            st.markdown("""
            <style>
            
            div[data-testid="stTextArea"] {
                width: 100%;
            }

            div[data-testid="stTextArea"] textarea {
                background-color: #19191b !important;
                color: #e5e5e5 !important;
                border: 1px solid #b87900 !important;
                border-radius: 10px !important;
                padding: 38px 38px !important;
                font-size: 18px !important;
                line-height: 1.6 !important;
                min-height: 200px !important;
                resize: none !important;
                outline: none !important;
                transition: all 0.25s ease !important;
                
            }

           
            div[data-testid="stTextArea"] textarea::placeholder {
                color: #737681 !important;
                opacity: 1 !important;
            }

            
            div[data-testid="stTextArea"] textarea:focus {
                border-color: #d89500 !important;

            div[data-testid="stTextArea"] div[data-testid="InputInstructions"] {
                color: #737681 !important;
                font-size: 13px !important;
            }

            

            /* Remove Streamlit label spacing if label is hidden */
            div[data-testid="stTextArea"] label {
                display: none !important;
            }
            </style>
            
           
            """, unsafe_allow_html=True)

            #Text, summary, article text input
            text = st.text_area(
                "",
                placeholder="Paste your manuscript, article, or story...",
                max_chars=50000,
                height=300
            )
            
            
            
            
            #Voice selection
            select_voice = st.selectbox('Voice', options=["en-US-AnaNeural",
                                                          "en-US-AndrewMultilingualNeural",
                                                          "en-US-AndrewNeural",
                                                          "en-US-AriaNeural",
                                                          "en-US-AvaMultilingualNeural",
                                                          "en-US-AvaNeural",
                                                          "en-US-BrianMultilingualNeural",
                                                          "en-US-BrianNeural",
                                                          "en-US-ChristopherNeural",
                                                          "en-US-EmmaMultilingualNeural",
                                                          "en-US-EmmaNeural",
                                                          "zh-CN-liaoning-XiaobeiNeural",
                                                          "zh-CN-XiaoyiNeural",
                                                          "en-US-MichelleNeural",
                                                          "en-US-RogerNeural",
                                                          "en-US-SteffanNeural",
                                                          "en-NG-AbeoNeural",
                                                          "en-NG-EzinneNeural",
                                                          "af-ZA-AdriNeural",
                                                          "af-ZA-WillemNeural"   
                                                          ], placeholder='Select a voice')
           
            
            #Button styling
            st.markdown("""
                <style>
                div.stButton > button {
                    background-color: #b87900 !important;
                    color: white !important;
                    border: 1px solid #d89500 !important;
                    border-radius: 10px !important;
                    padding: 10px 24px !important;
                    font-size: 16px !important;
                    font-weight: 600 !important;
                    box-shadow: 0 0 10px rgba(184, 121, 0, 0.3) !important;
                    transition: all 0.2s ease !important;
                }

                div.stButton > button:hover {
                    background-color: #d89500 !important;
                    border-color: #f0a800 !important;
                    box-shadow: 0 0 15px rgba(216, 149, 0, 0.5) !important;
                    transform: translateY(-1px);
                }

                div.stButton > button:active {
                    transform: translateY(0);
                }
                </style>
                """, unsafe_allow_html=True)
  
            #Container  
            with st.container(border=False):
                
                #Button
                if st.button('Generate Audio', icon=':material/music_note_2:', width='stretch'):
                    try:
                        if text:
                            with st.spinner('Rendering...'):
                                audio = asyncio.run(generate_voice(text, select_voice))
                                st.toast('✅ Sucessfully Generated Audio!')
                                st.container(border=False, height=20)
                                st.audio(audio, format="audio/mp3", autoplay=True)          
                                
                        else:
                            st.error('Text Field is empty!')
                                   
                    except Exception:
                        st.warning('Slow or No Internet Connection?')
                               
        render()
     
app = App()