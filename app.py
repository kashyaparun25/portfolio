import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="Arun Kashyap - Data Scientist Portfolio",
        page_icon="🧑🏻‍💻",
        layout="wide"
    )

    # Custom CSS for better styling with Nunito font and smooth scrolling
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&display=swap" rel="stylesheet">
        <style>
        * {
            font-family: 'Nunito', sans-serif;
        }
        body {
            background-color: #121212;
            margin: 0;
            padding: 0;
        }
        .main {
            padding: 2rem;
        }
        .section {
            margin: 2rem 0;
            padding: 0.3rem;
            background-color: #1e1e1e;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .project-card, .article-card {
            padding: 1.5rem;
            border-radius: 0.5rem;
            border: 1px solid #333333;
            margin: 1rem 0;
            background-color: #1e1e1e;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        }
        .skill-tag {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            margin: 0.2rem;
            border-radius: 1rem;
            background-color: #2e2e2e;
            font-size: 0.9rem;
            color: #ffffff;
        }
        a {
            color: #40C4FF !important;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .nav-link {
            color: #ffffff !important;
            text-decoration: none;
            display: block;
            padding: 0.8rem 1.2rem;
            margin: 0.5rem 0;
            border-radius: 0.5rem;
            background-color: #2e2e2e;
            text-transform: uppercase;
            text-align: center;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .nav-link:hover {
            background-color: #40C4FF;
            color: #ffffff;
            box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
            cursor: pointer;
        }
        [data-testid="stSidebar"] {
            background-color: #1e1e1e;
        }
        [data-testid="stSidebarNav"] {
            color: #ffffff;
        }
        html {
            scroll-behavior: smooth;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.title("Navigation")
        sections = {
            "About": "about",
            "Education": "education",
            "Skills": "skills",
            "Certifications": "certifications",
            "Experience": "experience",
            "Projects": "projects",
            "Articles": "articles",
            
        }

        st.markdown("### Sections")
        for section_name, section_id in sections.items():
            st.markdown(f"""
                <a href="#{section_id}" class="nav-link">{section_name}</a>
            """, unsafe_allow_html=True)

    # Main content
    # About Section
    st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 0.3, 2])

    with col1:
        st.image("D:/github-portfolio/pofo st/photo.png", caption="Arun Kashyap", use_container_width=True)

    with col2:
        st.write("")

    with col3:
        st.title("Arun Kashyap")
        st.subheader("Data Scientist | MS Data Science Student")
        st.write("""
        📍 New York City, NY   
        📧 [hvarunkashyap@gmail.com](mailto:hvarunkashyap@gmail.com) | 📱 +1 (201) 275-8046  
        💼 [LinkedIn](http://www.linkedin.com/in/hv-arunkashyap) | 🔗 [GitHub](https://github.com/kashyaparun25) | 🌐 [Hugging Face](https://huggingface.co/kashyaparun)
        """)
        st.subheader("About me")
        st.write("Hi! I'm Arun, a motivated data scientist passionate about revolutionizing how data is utilized in daily life.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Education Section
    st.markdown('<div id="education" class="section">', unsafe_allow_html=True)
    st.header("Education")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Stevens Institute of Technology
        **MS in Data Science** (Expected May 2025)  
        GPA: 3.89/4.0  
        *Courses: Applied Machine Learning, Deep Learning, Big Data, Probability & Statistics,   
                    Developing Business Applications Using GenAI*
        """)

    with col2:
        st.markdown("""
        ### Presidency University
        **BTech in Electronics and Communication Engineering** (2017 - 2021)  
        GPA: 3.71/4.0  
        *Courses: Artificial Neural Network, Digital Image Processing, Engineering Mathematics*
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Skills Section
    st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
    st.header("Skills")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming Languages")
        st.markdown("Python, C, C++")

    with col2:
        st.subheader("Data Science Tools")
        st.markdown("""Pandas, Numpy, Scikit-learn, TensorFlow, Tableau,    
                    Power BI""")

    with col3:
        st.subheader("Cloud & Databases")
        st.markdown("Google Colab, AWS, MySQL, Microsoft SSMS")
    st.markdown('</div>', unsafe_allow_html=True)

     # Certifications Section
    st.markdown('<div id="certifications" class="section">', unsafe_allow_html=True)
    st.header("Certifications")
    st.markdown("""
    - Python For Everybody (Coursera)
    - Data Structures in Python (Coursera)
    - Machine Learning for All (Coursera)
    - AI for Everyone (Coursera)
    - Introduction to Data Science (IBM Developer Skills Network)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Experience Section
    st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
    st.header("Work Experience")

    st.markdown("""
    ### Product Analyst | BlueTree Consultancy Services Private Limited
    *June 2021 - June 2022, Bangalore, India*

    - Collaborated with clients such as Autoliv and PhonePe to gather project requirements and align HR software solutions to their needs
    - Spearheaded comprehensive data analysis on HR operations, identifying and eliminating inefficiencies, leading to 15% improvement
    - Designed and maintained interactive Power BI dashboards for real-time HR metrics insights
    - Led end-to-end HR SaaS product implementations, reducing errors by 10%

    ### IoT Intern | Invicto Energies Private Limited
    *June 2019 - August 2019, Bangalore, India*

    - Engineered a data collection pipeline for smart irrigation using Python
    - Programmed system integration with mobile applications for environmental data analysis
    - Improved irrigation efficiency by 20% through advanced data analysis
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Projects Section
    st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
    st.header("Projects")

    with st.container():
        st.markdown("""
        ###  1. ResNet50 Unleashed: Mastering CIFAR-10 Image Recognition
        ##### *[View Project on Github](https://github.com/kashyaparun25/ResNet50-Unleashed-Mastering-CIFAR-10-Image-Recognition)*

        *April 2024, Stevens Institute of Technology*

        - Developed a deep learning model using ResNet50 architecture for the CIFAR-10 dataset
        - Implemented advanced data preprocessing and hyperparameter tuning techniques
        - Achieved 93.08% test accuracy, surpassing basic CNN performance (74.11%)
        - Utilized GPU acceleration on Google Colab for efficient model training.
        
        
                    
                    
        ### 2. Billionaires Unveiled: A Data-Driven Exploration 
        ##### *[View Project on Github](https://github.com/kashyaparun25/Billionaires-Unveiled-A-Data-Driven-Exploration-of-Wealth-and-Power)*
        *September 2023, Bangalore, India*

        - Conducted comprehensive analysis of billionaire datasets using Python
        - Created insightful visualizations using seaborn and matplotlib
        - Improved data insights by 30% through advanced visualization techniques
        - Generated actionable insights on wealth distribution patterns
                    
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    
   

   # Articles Section
    st.markdown('<div id="articles" class="section">', unsafe_allow_html=True)
    st.header("Technical Articles")

    articles = [
        {
            "title": "AI Deception Unveiled: How Frontier Models Scheme and Fake Alignment",
            "date": "January 2025",
            "summary": ("""Large language models like o1, Claude, and Gemini can engage in both alignment faking and in-context scheming,
                        meaning they can appear to follow instructions while secretly pursuing their own goals. This highlights
                        the potential for sophisticated deception in AI and the need for more research to prevent these issues."""),

            "link": "https://medium.com/@kashyaparun25/ai-deception-unveiled-how-frontier-models-scheme-and-fake-alignment-71a4cc12999b"
        },
        {
            "title": "Journey from LLM to LCM: How New AI Thinks in Concepts, Not Just Tokens",
            "date": "January 2025",
            "summary":("""Tired of AI that just strings words together? A new approach, the Large Concept Model, is here to shake things up by processing ideas,
                       not just tokens. This AI thinks and reasons at a higher level, using multilingual concepts to summarize, expand and create content more like a human would"""),
                       
            "link": "https://medium.com/@kashyaparun25/journey-from-llm-to-lcm-how-new-ai-thinks-in-concepts-not-just-tokens-756be885a613"
        }
    ]

    for article in articles:
        st.markdown(f"""
        <div class="article-card">
            <h3 style="color: #ffffff;">{article['title']}</h3>
            <p><em style="color: #cccccc;">{article['date']}</em></p>
            <p style="color: #cccccc;">{article['summary']}</p>
            <a href="{article['link']}" target="_blank">Read More</a>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
