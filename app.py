import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="Arun Kashyap - Data Scientist Portfolio",
        page_icon="🧑🏻‍💻",
        layout="wide"
    )

    # Custom CSS remains the same as in your original code
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

    # Sidebar remains the same
    with st.sidebar:
        st.title("Navigation")
        sections = {
            "About": "about",
            "Education": "education",
            "Skills": "skills",
            "Certifications": "certifications",
            "Experience": "experience",
            "Projects": "projects",
            "Activities": "activities",
            "Articles": "articles",
        }

        st.markdown("### Sections")
        for section_name, section_id in sections.items():
            st.markdown(f"""
                <a href="#{section_id}" class="nav-link">{section_name}</a>
            """, unsafe_allow_html=True)

    # About Section
    st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 0.3, 2])

    with col1:
        st.image("photo.png", caption="Arun Kashyap", use_container_width=True)

    with col2:
        st.write("")

    with col3:
        st.title("Arun Kashyap")
        st.subheader("Data Scientist | MS Data Science Student")
        st.write("""
        📍 New York City, NY   
        📧 [hvarunkashyap@gmail.com](mailto:hvarunkashyap@gmail.com) | 📱 +1 (201) 275-8046  
        💼 [LinkedIn](http://www.linkedin.com/in/hv-arunkashyap) | 🔗 [GitHub](https://github.com/kashyaparun25)
        """)
        st.subheader("About me")
        st.write("""I am a driven Data Science graduate student at Stevens Institute of Technology, passionate about transforming complex data into actionable insights using machine learning, deep learning, and Generative AI. With hands-on expertise in building AI agents, implementing model fine-tuning, and designing scalable big data pipelines, I thrive on solving real-world challenges with cutting-edge technologies.

In my professional journey, I’ve collaborated with industry leaders like Autoliv and PhonePe, creating impactful HR SaaS solutions that enhanced efficiency and enabled data-driven decision-making. From developing AI-powered chatbots with LangChain to deploying PySpark pipelines for fraud detection, I bring a strong blend of technical acumen and innovation.

Fueled by a passion for AI innovation and practical problem-solving, I aim to drive meaningful impact in tech-driven industries through intelligent, scalable solutions.""")
    st.markdown('</div>', unsafe_allow_html=True)

    # Education Section - Updated with latest GPA
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
        **BTech in Electronics and Communication Engineering** (2021)  
        GPA: 3.71/4.0  
        *Courses: Artificial Neural Network, Digital Image Processing, Engineering Mathematics*
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Skills Section - Updated with latest skills from resume
    st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
    st.header("Skills")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming & AI Tools")
        st.markdown("""
        - Python (Numpy, Pandas, Scikit-learn, TensorFlow, Matplotlib, Seaborn)
        - Hugging Face Transformers
        - LangChain
        - Model fine-tuning""")

    with col2:
        st.subheader("Database & Visualization")
        st.markdown("""
        - PostgreSQL 
        - MySQL
        - SQL Server Management Studio (SSMS) 
        - Power BI""")

    with col3:
        st.subheader("Big Data & Cloud Platforms")
        st.markdown("""
        - PySpark
        - AWS (EMR, S3)
        - GCP (Cloud SQL, Cloud Run)
        - Google Colab""")
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

    # Experience Section - Updated with latest experience
    st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
    st.header("Work Experience")

    st.markdown("""
    ### Product Analyst | BlueTree Consultancy Services Private Limited
    *June 2021 - June 2023, Bangalore, India*

    - Collaborated with **Autoliv**, a global leader in automotive safety systems, to design and implement custom HR SaaS solutions, optimizing workforce operations and improving efficiency by 15% through advanced **Power BI dashboards**
    - Partnered with **PhonePe**, India's leading fintech company, to integrate HR analytics with their digital payment systems, leveraging **Python scripting** and **Postman API** testing
    - Engineered **interactive Power BI dashboards** for real-time HR metrics insights
    - Spearheaded end-to-end HR SaaS implementations, reducing deployment errors by 10%

    ### IoT Intern | Invicto Energies Private Limited
    *June 2019 - August 2019, Bangalore, India*

    - Developed a Python-based data collection pipeline for smart irrigation
    - Integrated system with BOLT IoT mobile application for environmental data analysis
    - Applied Regression Analysis and advanced data preprocessing techniques, improving irrigation efficiency by 20%
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Projects Section - Updated with latest projects
    st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
    st.header("Projects")

    projects = [
        {
            "title": "ResNet50 Unleashed: Mastering CIFAR-10 Image Recognition",
            "date": "April 2024",
            "location": "Stevens Institute of Technology",
            "description": [
                "Worked on improving image recognition accuracy for the CIFAR-10 dataset (60,000 images across 10 classes)",
                "Implemented a CNN with ResNet50, applying data preprocessing and hyperparameter tuning",
                "Achieved 93.08% test accuracy, significantly surpassing basic CNN performance (74.11%)"
            ],
            "link": "https://github.com/kashyaparun25/ResNet50-Unleashed-Mastering-CIFAR-10-Image-Recognition"
        },
        {
            "title": "Anti-Money Laundering Detection Using Big Data Technologies",
            "date": "2024",
            "location": "Stevens Institute of Technology",
            "description": [
                "Developed a distributed pipeline on AWS EMR using PySpark to process a 3GB dataset of 31M financial transactions",
                "Engineered advanced features and mitigated class imbalance using SMOTE",
                "Trained a Random Forest model, achieving AUROC: 0.95 and F1-score: 0.90"
            ],
            "link": "https://github.com/kashyaparun25/Anti-Money-Laundering-Detection-Using-Big-Data-Technologies"
        },
        {
            "title": "AI-Powered Health Monitoring Chatbot",
            "date": "2024",
            "location": "Stevens Institute of Technology",
            "description": [
                "Built an AI-driven chatbot with LangChain for memory and agentic LLMs",
                "Integrated WHOOP API, PostgreSQL, and Claude AI for health metrics analysis",
                "Delivered interactive data visualizations using Matplotlib and Seaborn"
            ],
            "link": "https://github.com/kashyaparun25/AI-Powered-Health-Monitoring-Chatbot"
        },
        {
            "title": "Emotion Classification and Mental Health Chatbot",
            "date": "2024",
            "location": "Stevens Institute of Technology",
            "description": [
                "Developed a multi-label emotion classification model using RoBERTa",
                "Achieved a macro F1-score of 74% on the GoEmotions dataset",
                "Implemented LangChain for conversational memory and context-aware responses"
            ],
            "link": "https://github.com/kashyaparun25/Mental-Health-Chatbot-using-RoBERTa-and-Gemini"
        }
    ]

    for project in projects:
        st.markdown(f"""
        ### {project['title']}
        ##### *[View Project on Github]({project['link']})*
        *{project['date']}, {project['location']}*
        """)
        for point in project['description']:
            st.markdown(f"- {point}")
        st.write("")

    st.markdown('</div>', unsafe_allow_html=True)

    # Activities Section - New section from resume
    st.markdown('<div id="activities" class="section">', unsafe_allow_html=True)
    st.header("Activities")
    st.markdown("""
    - Secured a bronze medal at a State-level Taekwondo World Federation competition (May 2018, Bangalore, India)
    - Volunteered as an organizer for academic and cultural events, enhancing community engagement and leadership skills (August 2023, India)
    - Designed and managed a community garden project, fostering teamwork while promoting sustainability and environmental awareness (January 2015 - Present, India)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Articles Section
    st.markdown('<div id="articles" class="section">', unsafe_allow_html=True)
    st.header("Technical Articles")

    articles = [
        {
            "title": "AI Deception Unveiled: How Frontier Models Scheme and Fake Alignment",
            "date": "January 2025",
            "summary": """Large language models like o1, Claude, and Gemini can engage in both alignment faking and in-context scheming,
                        meaning they can appear to follow instructions while secretly pursuing their own goals. This highlights
                        the potential for sophisticated deception in AI and the need for more research to prevent these issues.""",
            "link": "https://medium.com/@kashyaparun25/ai-deception-unveiled-how-frontier-models-scheme-and-fake-alignment-71a4cc12999b"
        },
        {
            "title": "Journey from LLM to LCM: How New AI Thinks in Concepts, Not Just Tokens",
            "date": "January 2025",
            "summary": """Tired of AI that just strings words together? A new approach, the Large Concept Model, is here to shake things up by processing ideas,
                       not just tokens. This AI thinks and reasons at a higher level, using multilingual concepts to summarize, expand and create content more like a human would""",
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
