import streamlit as st
from PIL import Image
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data-related career consultant bot."},
            {"role": "user", "content": question},
        ]
    )
    return response.choices[0].message['content']

def submit_query():
    user_input = st.session_state.query  # Access user input from session state
    if user_input:  # Check if there is input
        response = ask(user_input)
        st.session_state.response = response  # Store response in session state    

def main():
    # Mentoring Introduction
    st.subheader('데이터 전문가 멘토링')
    st.write("""
    👋 안녕하세요? 다양한 산업에서 10년 이상 실무 경험을 가진 멘토님들이 여러분들의 고민을 같이 해결해주기 위해 모였습니다. 멘토님들은 **데이터사이언스/데이터분석, PO/PM, 사업개발 및 비즈니스분석** 등 전문성과 풍부한 실무경험을 보유하였으며, 여러분들의 취업 및 직무전환, 역량개발에 대한 다양한 커리어 고민을 듣고 적극적으로 돕고자 합니다. 합리적인 비용으로 관심 있는 멘토님과 상담을 시작해보세요. 
    """)
    
    # Sidebar
    with st.sidebar:
        if st.button("Home"): pass
        if st.button("전문가 멘토링 신청하기"):
            st.write("멘토링 진행방식 및 유의사항을 확인하고 아래 버튼을 클릭하여 신청해주세요.")
            st.markdown("[**신청서 작성**](https://forms.gle/xUawk93Wkw4YTfrg6)")
            st.write("멘토링에 대해 궁금한 사항이 있으면 링크를 통해 문의해주세요.")
            st.markdown("[**문의하기**](https://forms.gle/Vrt8ubNx7XWyGHr86)")
        if st.button("멘토링 방식과 비용"):
            st.write("멘토의 프로필을 확인하고 관심있는 멘토에게 멘토링을 신청하세요. 멘토가 직접 다음 과정을 안내해드립니다.")
            st.write("멘토링 비용은 멘토마다 다르게 산정됩니다. 신청서 작성시 비용을 확인해주시고 궁금한 것이 있다면 멘토에게 문의해주세요.")
        
        st.subheader("👨‍🚀 Chat with the Career AI")    
        user_input = st.text_input("간단한 문의를 AI챗봇과 진행해보세요.", key="query", on_change=submit_query)
        # Submit button
        if st.button("SEND"):
            with st.spinner("Wait..."):
                submit_query()  # Call the submit function when the button is pressed    
        if 'response' in st.session_state:
            st.markdown(st.session_state['response'])
    
    
    image = Image.open('mypic.png').resize((200, 200))
    # Mentor Information
    mentors = [
        {"name": "Liam Song", 
             "job_title": "데이터사이언티스트", 
             "year": "13년",
             "company": "마켓컬리, 우아한형제들, 현대카드", 
             "industry": "IT",
             "projects": "추천시스템 및 수요예측 등 머신러닝 모델을 개발", 
             "detail1": "데이터사이언스 분야로 전직하거나 신입으로 취업하고자 하는 분들에게 도움이 되는 경험과 지식을 나누어 드리고 싶습니다.",
             "detail2": "주요 관심분야는 **예측 및 최적화, 추천/랭킹모델, LLM 모델** 등이며, 주로 이커머스 및 금융분야에서 커리어를 쌓아왔습니다. **Python, SQL, Spark** 등 프로그래밍 언어를 선호하며 다양한 시각화 및 통계분석도 진행하였습니다. 최근에는 10명 규모의 데이터사이언스팀의 팀장으로서 구성원의 성장과 리더십에도 많은 관심을 갖고 있습니다.",
         "detail3": """아래는 멘토의 기존 **강의 경력**입니다.     
             - Python Programming, and Data Analysis and Machine Learning for KCC    
             - 삼성전자 Jira & Confluence 교육    
             - 롯데그룹 Data 전문가 워크샵 특강    
             - 중소벤처기업진흥공단 AI 이어드림 스쿨 1기, 2기 자문위원    
             - K-Degital Credit 데이터사이언티스트 양성 과정 6~8기 교육 진행    
             - 데이터사이언스 Extention School 1기, 2기 강의    
             - 카톨릭대학교 4세대 연구방법론 강의    
             - 카이스트 MBA 데이터사이언티스트 현직자 특강    
             """,
         "detail4": """아래 **기술블로그와 언론 자료**를 참고해주세요.     
            - https://helloworld.kurly.com/blog/introduce_datascience_team/   
            - https://techblog.woowahan.com/2536/    
            - https://techblog.woowahan.com/2686/    
            - https://www.joongang.co.kr/article/25037652#home   
            - https://www.etnews.com/20210818000196    
            """,
        },
        {"name": "X", 
             "job_title": "X", 
             "year": "X",
             "company": "X", 
             "industry": "X",
             "projects": "X", 
             "detail1": "X",
             "detail2": "X",
             "detail3": """X""",
             "detail4": """X""",
        },
        {"name": "X", 
             "job_title": "X", 
             "year": "X",
             "company": "X", 
             "industry": "X",
             "projects": "X", 
             "detail1": "X",
             "detail2": "X",
             "detail3": """X""",
             "detail4": """X""",
        },
        {"name": "X", 
             "job_title": "X", 
             "year": "X",
             "company": "X", 
             "industry": "X",
             "projects": "X", 
             "detail1": "X",
             "detail2": "X",
             "detail3": """X""",
             "detail4": """X""",
        }
    ]
    
    st.subheader('멘토님 소개')
    st.write("""
    아래에서 관심 있는 멘토님의 이름을 클릭하시면 자세한 멘토님들의 프로필을 확인할수 있습니다. 
    """)
    
    for mentor in mentors:
        with st.expander(f"{mentor['name']} ({mentor['job_title']} at {mentor['company']})"):
            if mentor['name'] != "X":
                st.image(image, use_column_width=False)
            else:
                st.write("Error: 프로필 이미지를 삽입해주세요")
            st.write(f"안녕하세요? {mentor['company']}등 {mentor['industry']} 분야에서 {mentor['job_title']}로서 {mentor['year']}간 {mentor['projects']}하였습니다. {mentor['detail1']}")
            st.write(f"{mentor['detail2']}")
            st.write(f"{mentor['detail3']}")
            st.write(f"{mentor['detail4']}")
            
    # Mentoring effectiveness
    st.subheader('멘토링 후기')
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **데이터사이언티스트로 취업에 성공한 K님.**
        > "저는 비전공자이지만 데이터사이언티스로서 IT회사에 취업하기 위해 멘토링을 진행했고, 포트폴리오와 면접 준비를 통해 원하는 IT회사에서 데이터사이언티스트로 근무중입니다."
        """)
    
    with col2:
        st.success("""
        **데이터 분석가로 직무 전환에 성공한 J님.**
        > "기존에 마케터로 근무했었지만 데이터 분석 관련 공부와 멘토링의 도움으로 직무 전환에 성공할수 있었어요. 저 같이 데이터 직무로 전환하는 분들이 있다면 멘토링을 강추합니다."
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning("""
        **비즈니스 분석가로 경력을 확장한 T님.**
        > "저는 사업전략과 사업기획을 주로 해왔었지만, 멘토링을 통해 데이터 및 통계 분석 능력을 갖게 되었어요. 데이터 기반한 기획/전략가로서 원래 하던 업무를 더 잘할수 있게 되었습니다."
        """)
    
    with col2:
        st.success("""
        **프로덕트 오너로 직무 전환에 성공한 S님.**
        > "기존 데이터 직무에서 프로덕트 오너로 직무 전환에 성공했어요. 관심만 있고 잘 모르는 분야이지만 멘토링을 통해 직무 전환에 대해 확신을 갖을수 있었고, 지금은 매우 만족합니다."
        """)
    
    
    
    # Mentoring Process
    st.subheader('멘토링 진행방식')
    st.info("""
    ① 멘토링 신청서를 작성합니다.    
    ② 신청서를 기반으로 1주일 안에 멘토가 매칭됩니다.     
    ③ 매칭된 멘토님과 1:1 멘토링을 진행합니다.    
    """)
    
    apply_link = 'https://forms.gle/xUawk93Wkw4YTfrg6'
    st.markdown(f'📝 [**신청서 작성**]({apply_link})', unsafe_allow_html=True)
    
    st.subheader('멘토링 Q&A')
    st.write("""
    **Q)** 멘토링 세부 주제와 내용은 어떻게 정해지나요?    
    **A)** 멘토링 신청후 사전에 멘토님과 세부적인 주제와 내용에 대해 논의하시고 진행합니다.
    """
    )
    st.write("""
    **Q)** 멘토링 기간이나 일정, 비용은 어떻게 정해지고 환불은 어떻게 하면 되나요?    
    **A)** 기간이나 일정, 비용 및 환불정책은 멘토님마다 다르게 운영되고 있습니다. 멘토님과 상의해주세요.
    """
    )
    st.write("""
    **Q)** 1대1로만 멘토링이 진행이 되나요?   
    **A)** 기본적으로 1대1 진행이 원칙이지만 멘토 및 멘티의 합의에 따라 1대N으로도 진행될수 있습니다.
    """
            )
    
    question_link = 'https://forms.gle/Vrt8ubNx7XWyGHr86'
    st.info(f"멘토링에 대해 궁금한 사항이 있으면 [**문의하기**]({question_link})' 클릭하여 문의해주세요.")

if __name__ == '__main__':
    main()
