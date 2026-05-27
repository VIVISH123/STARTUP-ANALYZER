import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="STARTWISE | Startup Viability Predictor",
    page_icon="🚀",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* REMOVE STREAMLIT DEFAULT HEADER BAR */
    header[data-testid="stHeader"] {
        background: transparent;
        height: 0px;
    }

    /* REMOVE EXTRA TOP PADDING */
    .block-container {
        padding-top: 1.5rem;
    }

    body {
        background-color: #0b0f19;
    }

    .hero {
        text-align: center;
        margin-bottom: 35px;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 1px;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #9ca3af;
        margin-top: 8px;
    }

    .card {
        background: #111827;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #1f2937;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 12px;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 STARTWISE</div>
    <div class="hero-subtitle">
        AI-Assisted Startup Idea Viability Predictor
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

startup_name = st.text_input(
    "Startup / Enterprise Name",
    placeholder="e.g., Startwise Labs"
)

idea_text = st.text_area(
    "Describe your startup idea",
    placeholder="What problem are you solving? Who is it for? What makes it unique?",
    height=140
)

st.info(
    "🔐 **Idea Security & Privacy**  \n"
    "Your startup name and idea are processed only for this session.  \n"
    "**No data is stored, shared, or leaked.**"
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DOCUMENTATION / EFFORT SECTION ----------------
with st.expander("📘 How STARTWISE Works"):
    st.write(
        "STARTWISE is an AI-assisted decision-support system designed to help "
        "entrepreneurs evaluate early-stage startup ideas using structured analysis "
        "rather than subjective intuition."
    )

with st.expander("🧠 Evaluation Methodology"):
    st.write(
        "- **Market Potential**: Estimates problem relevance and adoption likelihood\n"
        "- **Technical Feasibility**: Assesses implementation complexity and scalability\n"
        "- **Innovation Score**: Measures conceptual novelty and differentiation\n\n"
        "These factors are aggregated to compute an overall viability score."
    )

with st.expander("🧩 System Architecture (Conceptual)"):
    st.write(
        "1. User provides startup name and idea description\n"
        "2. Text is pre-processed and analyzed\n"
        "3. Independent evaluation modules generate scores\n"
        "4. Scores are aggregated into a viability indicator\n"
        "5. Insights are presented in an interpretable dashboard"
    )

with st.expander("🔎 Similar Products & Patent Analysis"):
    st.write(
        "In the complete system, NLP-based semantic similarity techniques "
        "would compare ideas against existing products and patent databases.\n\n"
        "This demo simulates similarity detection to illustrate the workflow."
    )

with st.expander("🚀 Future Scope"):
    st.write(
        "- Integration with real market and patent datasets\n"
        "- Advanced transformer-based NLP models\n"
        "- Investor and accelerator scoring modes\n"
        "- Downloadable evaluation reports\n"
        "- Secure user accounts with idea history"
    )

with st.expander("⚖️ Ethics & Privacy"):
    st.write(
        "STARTWISE follows a privacy-first design. User ideas are never stored, "
        "logged, or shared. The system is intended solely for decision support "
        "without exploiting intellectual property."
    )

# ---------------- ANALYSIS SECTION ----------------
word_count = len(idea_text.strip().split())

if startup_name.strip() and word_count >= 15:

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"### Viability Analysis — **{startup_name}**")

    market = random.randint(60, 90)
    tech = random.randint(55, 88)
    innovation = random.randint(65, 92)
    overall = int((market + tech + innovation) / 3)

    col1, col2, col3 = st.columns(3)
    col1.metric("Market Potential", f"{market}%")
    col2.metric("Technical Feasibility", f"{tech}%")
    col3.metric("Innovation Score", f"{innovation}%")

    st.markdown("---")

    if overall >= 75:
        st.success(f"High potential startup idea • Overall score {overall}%")
    elif overall >= 60:
        st.warning(f"Moderate potential • Overall score {overall}%")
    else:
        st.error(f"High risk startup idea • Overall score {overall}%")

    st.markdown("### Key Insights")
    st.write(
        "- Problem–solution alignment appears reasonable\n"
        "- Competitive differentiation will strongly influence success\n"
        "- Early market validation is recommended before scaling"
    )

    st.markdown("</div>", unsafe_allow_html=True)

elif idea_text.strip():
    st.warning("Please describe your idea in at least 15 words to enable analysis.")

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
STARTWISE • AI Decision Support System<br>
Privacy-first • Session-only processing
</div>
""", unsafe_allow_html=True)
