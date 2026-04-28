# Streamlit App — LawMindAI

import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page Configuration ──────────────────────────────────────────────
st.set_page_config(
    page_title="LawMindAI — AI Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Import Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Main header ── */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.2rem;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        font-size: 1.15rem;
        color: #6B7280;
        font-weight: 400;
        margin-bottom: 2rem;
        line-height: 1.6;
    }

    /* ── Cards ── */
    .feature-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(79,70,229,0.08);
        border-color: #C7D2FE;
    }
    .feature-icon {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    .feature-title {
        font-weight: 600;
        font-size: 1rem;
        color: #1E1E2E;
        margin-bottom: 0.3rem;
    }
    .feature-desc {
        font-size: 0.88rem;
        color: #6B7280;
        line-height: 1.5;
    }

    /* ── Result container ── */
    .result-container {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .result-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1E1E2E;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F8F7FF 0%, #EEF2FF 100%);
        border-right: 1px solid #E5E7EB;
    }
    .sidebar-brand {
        font-size: 1.4rem;
        font-weight: 700;
        color: #4F46E5;
        margin-bottom: 0.3rem;
    }
    .sidebar-tagline {
        font-size: 0.85rem;
        color: #6B7280;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    .sidebar-section-title {
        font-size: 0.75rem;
        font-weight: 600;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .step-item {
        display: flex;
        align-items: flex-start;
        gap: 0.6rem;
        margin-bottom: 0.8rem;
    }
    .step-num {
        background: #4F46E5;
        color: white;
        font-size: 0.7rem;
        font-weight: 700;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        margin-top: 2px;
    }
    .step-text {
        font-size: 0.88rem;
        color: #374151;
        line-height: 1.4;
    }

    /* ── Badge ── */
    .badge {
        display: inline-block;
        background: #EEF2FF;
        color: #4F46E5;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        border: 1px solid #C7D2FE;
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #9CA3AF;
        font-size: 0.8rem;
    }

    /* ── Text area ── */
    textarea {
        border-radius: 12px !important;
        border: 1.5px solid #D1D5DB !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        transition: border-color 0.2s ease !important;
    }
    textarea:focus {
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 3px rgba(79,70,229,0.1) !important;
    }

    /* ── Submit button ── */
    .stFormSubmitButton > button {
        background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: 0.01em !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 14px rgba(79,70,229,0.25) !important;
        width: 100% !important;
    }
    .stFormSubmitButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 24px rgba(79,70,229,0.35) !important;
    }
    .stFormSubmitButton > button:active {
        transform: translateY(0) !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-color: #4F46E5 !important;
    }

    /* hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">⚖️ LawMindAI</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-tagline">'
        'AI-powered legal assistant built for Indian law. '
        'Get case analysis, applicable IPC sections, legal precedents, and drafted documents instantly.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="sidebar-section-title">How it works</div>', unsafe_allow_html=True)

    steps = [
        ("1", "Describe your legal issue in plain English"),
        ("2", "AI analyzes and classifies the case"),
        ("3", "Relevant IPC sections are identified"),
        ("4", "Legal precedents are researched"),
        ("5", "A formal legal document is drafted"),
    ]
    for num, text in steps:
        st.markdown(
            f'<div class="step-item">'
            f'<div class="step-num">{num}</div>'
            f'<div class="step-text">{text}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown('<div class="sidebar-section-title">Powered by</div>', unsafe_allow_html=True)
    st.markdown(
        '<span class="badge">Gemini 2.0 Flash</span> '
        '<span class="badge">CrewAI</span> '
        '<span class="badge">ChromaDB</span>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        '<div style="font-size:0.78rem; color:#9CA3AF; line-height:1.5;">'
        '⚠️ <strong>Disclaimer:</strong> This tool provides AI-generated legal analysis for informational purposes only. '
        'It does not constitute legal advice. Please consult a qualified lawyer for professional guidance.'
        '</div>',
        unsafe_allow_html=True
    )

# ── Main Content ────────────────────────────────────────────────────
st.markdown('<div class="hero-title">AI Legal Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">'
    'Describe your legal issue below. Our multi-agent AI system will analyze your case, '
    'find applicable IPC sections, research precedent cases, and draft a formal legal document for you.'
    '</div>',
    unsafe_allow_html=True
)

# ── Feature cards ───────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

features = [
    ("🔍", "Case Analysis", "Classifies your issue into structured legal categories"),
    ("📖", "IPC Sections", "Finds the most relevant Indian Penal Code sections"),
    ("⚖️", "Precedents", "Researches similar past court judgments"),
    ("📝", "Legal Draft", "Generates a formal complaint, FIR, or legal notice"),
]

for col, (icon, title, desc) in zip([col1, col2, col3, col4], features):
    with col:
        st.markdown(
            f'<div class="feature-card">'
            f'<div class="feature-icon">{icon}</div>'
            f'<div class="feature-title">{title}</div>'
            f'<div class="feature-desc">{desc}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# ── Input Form ──────────────────────────────────────────────────────
with st.form("legal_query_form"):
    user_input = st.text_area(
        "Describe your legal issue",
        height=160,
        placeholder=(
            "Example: A man broke into my house at night while my family was sleeping. "
            "He stole jewelry and cash from our bedroom. When I confronted him, "
            "he threatened me with a knife and ran away. We reported it to the police, "
            "but I'm not sure which legal charges should be filed under IPC."
        ),
    )
    submit = st.form_submit_button("🚀  Analyze & Draft Legal Document")

# ── Processing ──────────────────────────────────────────────────────
if submit:
    if not user_input.strip():
        st.warning("⚠️ Please enter a legal issue to analyze.")
    else:
        with st.spinner("🔄 Our AI agents are analyzing your case — this may take a minute..."):
            try:
                from crew import legat_assistant_crew
                result = legat_assistant_crew.kickoff(inputs={"user_input": user_input})
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.stop()

        st.success("✅ Legal analysis completed successfully!")

        st.markdown(
            '<div class="result-container">'
            '<div class="result-header">📄 Legal Document</div>'
            '</div>',
            unsafe_allow_html=True
        )

        output_text = result if isinstance(result, str) else str(result)
        st.markdown(output_text)

        # Download button
        st.download_button(
            label="📥 Download as Text File",
            data=output_text,
            file_name="legal_document.txt",
            mime="text/plain",
        )

# ── Footer ──────────────────────────────────────────────────────────
st.markdown(
    '<div class="app-footer">'
    'Built with ❤️ using CrewAI, Gemini & Streamlit &nbsp;|&nbsp; LawMindAI © 2026'
    '</div>',
    unsafe_allow_html=True
)
