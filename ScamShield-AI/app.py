import streamlit as st
import base64
from pathlib import Path
from gemini_service import analyze_message


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

girl_path = Path(__file__).parent / "assets" / "scam_girl.png"

girl_base64 = base64.b64encode(
    girl_path.read_bytes()
).decode()

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

/* ===== GLOBAL ===== */

.stApp {
    background:
        radial-gradient(circle at 10% 15%, rgba(124,58,237,.18), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,.14), transparent 30%),
        radial-gradient(circle at 50% 90%, rgba(236,72,153,.08), transparent 30%),
        #050816;
    color:#f8fafc;
    overflow-x:hidden;
}

.block-container {
    max-width:1200px;
    padding:3rem 2rem 4rem;
}

/* ===== BACKGROUND FLOATERS ===== */

.stApp:before,
.stApp:after {
    content:"";
    position:fixed;
    width:180px;
    height:180px;
    border-radius:50%;
    filter:blur(70px);
    opacity:.25;
    pointer-events:none;
    animation:floatGlow 7s ease-in-out infinite;
}

.stApp:before {
    background:#7c3aed;
    top:15%;
    left:-80px;
}

.stApp:after {
    background:#06b6d4;
    right:-80px;
    bottom:15%;
    animation-delay:2s;
}

@keyframes floatGlow {
    0%,100% { transform:translateY(0) scale(1); }
    50% { transform:translateY(-20px) scale(1.08); }
}

/* ===== HEADER ===== */

.logo {
    font-size:38px;
    font-weight:900;
    letter-spacing:-1.5px;
    animation:fadeDown .8s ease both;
}

.logo span {
    background:linear-gradient(90deg,#38bdf8,#818cf8,#c084fc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.tagline {
    color:#94a3b8;
    font-size:15px;
    margin-top:-6px;
    animation:fadeDown 1s ease both;
}

@keyframes fadeDown {
    from { opacity:0; transform:translateY(-15px); }
    to { opacity:1; transform:translateY(0); }
}

/* ===== HERO ===== */

.hero {
    position:relative;
    min-height:500px;
    margin-top:25px;
    margin-bottom:30px;
    padding:55px 45% 45px 45px;
    border-radius:30px;
    overflow:hidden;

    background:
        linear-gradient(135deg,
        rgba(20,27,55,.96),
        rgba(8,14,32,.92));

    border:1px solid rgba(129,140,248,.22);
    box-shadow:
        0 25px 80px rgba(0,0,0,.35),
        inset 0 0 50px rgba(99,102,241,.04);
}

/* ===== HERO TEXT ===== */

.hero-content {
    position:relative;
    z-index:5;
    animation:heroText 1.2s .8s ease both;
}

@keyframes heroText {
    from {
        opacity:0;
        transform:translateX(-35px);
    }
    to {
        opacity:1;
        transform:translateX(0);
    }
}

.hero-badge {
    display:inline-block;
    padding:8px 14px;
    border-radius:30px;
    color:#e879f9;
    background:rgba(217,70,239,.10);
    border:1px solid rgba(217,70,239,.25);
    font-size:13px;
    font-weight:700;
    margin-bottom:18px;
}

.hero-title {
    font-size:42px;
    line-height:1.08;
    font-weight:900;
    letter-spacing:-1.5px;
}

.hero-title .gradient {
    background:linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #d946ef
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-text {
    color:#a7b1c6;
    font-size:16px;
    line-height:1.7;
    margin-top:18px;
}

/* ===== GIRL ===== */

.girl {
    position:absolute;
    z-index:4;

    right:10%;
    bottom:0;

    width:43%;
    max-width:500px;
    max-height:420px;

    object-fit:contain;
    object-position:center bottom;

    filter:
        drop-shadow(0 20px 35px rgba(99,102,241,.20));

    transform-origin:center bottom;

    animation:
        girlRise 1.5s cubic-bezier(.22,1,.36,1) both,
        girlFloat 5s 1.6s ease-in-out infinite;
}

@keyframes girlRise {

    0% {
        opacity:0;
        transform:translateY(220px) scale(.90);
    }

    70% {
        opacity:1;
        transform:translateY(-8px) scale(1.02);
    }

    100% {
        opacity:1;
        transform:translateY(0) scale(1);
    }
}

@keyframes girlFloat {

    0%,100% {
        transform:translateY(0) rotate(0deg);
    }

    50% {
        transform:translateY(-8px) rotate(.5deg);
    }
}

/* ===== GIRL ===== */

.girl {
    position:absolute;
    z-index:4;

    right:10%;
    bottom:0;

    width:35%;
    max-width:500px;
    max-height:420px;

    object-fit:contain;
    object-position:center bottom;

    filter:
        drop-shadow(0 20px 35px rgba(99,102,241,.20));

    transform-origin:center bottom;

    animation:
        girlRise 1.5s cubic-bezier(.22,1,.36,1) both,
        girlFloat 5s 1.6s ease-in-out infinite;
}

@keyframes girlRise {

    0% {
        opacity:0;
        transform:translateY(220px) scale(.90);
    }

    70% {
        opacity:1;
        transform:translateY(-8px) scale(1.02);
    }

    100% {
        opacity:1;
        transform:translateY(0) scale(1);
    }
}

@keyframes girlFloat {

    0%,100% {
        transform:translateY(0) rotate(0deg);
    }

    50% {
        transform:translateY(-8px) rotate(.5deg);
    }
}

/* ===== SCAM SIGNALS ===== */

.signal-bubble {
    position:absolute;
    z-index:3;
    padding:12px 18px;
    border-radius:18px;
    font-weight:700;
    font-size:13px;
    backdrop-filter:blur(12px);
    box-shadow:0 10px 35px rgba(0,0,0,.25);
    animation:
        signalIn .9s ease both,
        signalFloat 4s 1s ease-in-out infinite;
}

.signal-one {
    top:55px;
    right:26%;
    color:#86efac;
    border:1px solid rgba(34,197,94,.5);
    background:rgba(20,83,45,.35);
    animation-delay:.9s;
}

.signal-two {
    top:145px;
    right:37%;
    color:#fca5a5;
    border:1px solid rgba(248,113,113,.5);
    background:rgba(127,29,29,.35);
    animation-delay:1.15s;
}

.signal-three {
    top:85px;
    right:4%;
    color:#93c5fd;
    border:1px solid rgba(96,165,250,.5);
    background:rgba(30,64,175,.25);
    animation-delay:1.35s;
}

@keyframes signalIn {
    from {
        opacity:0;
        transform:translateX(50px) scale(.8);
    }
    to {
        opacity:1;
        transform:translateX(0) scale(1);
    }
}

@keyframes signalFloat {
    0%,100% { transform:translateY(0) rotate(0deg); }
    50% { transform:translateY(-7px) rotate(-1deg); }
}

/* ===== DETECT / UNDERSTAND / PROTECT ===== */

.feature-row {
    display:flex;
    gap:12px;
    margin-top:25px;
}

.feature {
    flex:1;
    padding:12px;
    border-radius:16px;
    background:rgba(15,23,42,.65);
    border:1px solid rgba(148,163,184,.12);
    transition:.3s ease;
}

.feature:hover {
    transform:translateY(-5px);
    border-color:#818cf8;
    box-shadow:0 10px 30px rgba(99,102,241,.18);
}

.feature b {
    display:block;
    margin-bottom:3px;
}

.feature small {
    color:#94a3b8;
}

/* ===== INPUT CARD ===== */

.input-card {
    position:relative;
    padding:28px;
    border-radius:24px;

    background:linear-gradient(
        145deg,
        rgba(17,27,52,.95),
        rgba(9,15,30,.95)
    );

    border:1px solid rgba(99,102,241,.35);

    box-shadow:
        0 20px 60px rgba(0,0,0,.25),
        inset 0 1px rgba(255,255,255,.04);

    animation:cardIn .8s .5s ease both;
}

@keyframes cardIn {
    from {
        opacity:0;
        transform:translateY(25px);
    }
    to {
        opacity:1;
        transform:translateY(0);
    }
}

/* ===== BUTTON ===== */

.stButton > button {
    height:55px !important;
    border-radius:15px !important;
    border:1px solid rgba(129,140,248,.5) !important;

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6,
            #d946ef
        ) !important;

    color:white !important;
    font-size:16px !important;
    font-weight:800 !important;

    box-shadow:
        0 10px 30px rgba(139,92,246,.25) !important;

    transition:
        transform .25s ease,
        box-shadow .25s ease !important;
}

.stButton > button:hover {
    transform:translateY(-3px) scale(1.01);
    box-shadow:
        0 15px 40px rgba(168,85,247,.4) !important;
}

.stButton > button:active {
    transform:scale(.98);
}

/* ===== TEXTAREA ===== */

.stTextArea textarea {
    background:#0b1225 !important;
    color:#f8fafc !important;
    border:1px solid rgba(129,140,248,.22) !important;
    border-radius:16px !important;
    font-size:15px !important;
    transition:.25s ease !important;
}

.stTextArea textarea:focus {
    border-color:#818cf8 !important;
    box-shadow:0 0 0 2px rgba(129,140,248,.12) !important;
}

/* ===== SELECT ===== */

.stSelectbox > div > div {
    background:#0b1225 !important;
    border-radius:14px !important;
    border-color:rgba(129,140,248,.2) !important;
}

/* ===== RESULT CARDS ===== */

.card {
    background:rgba(12,19,38,.82);
    border:1px solid rgba(148,163,184,.13);
    border-radius:20px;
    padding:24px;
    margin-top:20px;
}

.card-title {
    font-size:21px;
    font-weight:800;
    margin-bottom:14px;
}
            
            /* ===== INPUT SECTION ===== */

.input-section-title {
    font-size:24px;
    font-weight:800;
    margin-top:15px;
    margin-bottom:6px;
}

.input-section-subtitle {
    color:#94a3b8;
    font-size:14px;
    margin-bottom:12px;
}

/* Text area */
.stTextArea textarea {
    background:rgba(11,18,37,.9) !important;
    color:#f8fafc !important;
    border:1px solid rgba(129,140,248,.25) !important;
    border-radius:18px !important;
    font-size:15px !important;
    padding:18px !important;
    transition:.3s ease !important;
}

.stTextArea textarea:hover {
    border-color:rgba(129,140,248,.55) !important;
}

.stTextArea textarea:focus {
    border-color:#818cf8 !important;
    box-shadow:0 0 0 2px rgba(129,140,248,.12),
               0 0 25px rgba(99,102,241,.08) !important;
}

/* Language */
.stSelectbox > div > div {
    background:#0b1225 !important;
    border:1px solid rgba(129,140,248,.22) !important;
    border-radius:14px !important;
}

/* Scan button */
.stButton > button {
    height:52px !important;
    border:none !important;
    border-radius:15px !important;
    background:linear-gradient(
        90deg,
        #6366f1,
        #8b5cf6,
        #d946ef
    ) !important;
    color:white !important;
    font-size:16px !important;
    font-weight:800 !important;
    transition:.3s ease !important;
    box-shadow:0 10px 30px rgba(99,102,241,.22) !important;
}

.stButton > button:hover {
    transform:translateY(-2px);
    box-shadow:0 14px 35px rgba(139,92,246,.35) !important;
}

.risk-card {
    background:
        radial-gradient(circle at 90% 20%,rgba(239,68,68,.18),transparent 35%),
        rgba(30,15,30,.85);
    border:1px solid rgba(248,113,113,.3);
    border-radius:22px;
    padding:28px;
    margin-top:25px;
}

.risk-number {
    font-size:58px;
    font-weight:900;
}

.risk-label {
    font-size:15px;
    color:#fca5a5;
    font-weight:800;
}

.signal,
.action {
    padding:13px 16px;
    margin:8px 0;
    border-radius:12px;
    transition:.25s ease;
}

.signal {
    background:rgba(30,41,59,.65);
    border-left:3px solid #818cf8;
}

.action {
    background:rgba(20,83,45,.22);
    border-left:3px solid #4ade80;
}

.signal:hover,
.action:hover {
    transform:translateX(5px);
}

/* ===== TRAP ===== */

.trap {
    display:flex;
    align-items:center;
    justify-content:center;
    gap:10px;
    flex-wrap:wrap;
    margin-top:18px;
}

.trap-step {
    padding:14px 18px;
    border-radius:14px;
    background:rgba(30,41,59,.7);
    border:1px solid rgba(129,140,248,.18);
    transition:.3s ease;
}

.trap-step:hover {
    transform:translateY(-4px);
    border-color:#818cf8;
}

/* ===== FOOTER ===== */

.footer {
    text-align:center;
    color:#64748b;
    margin-top:55px;
    font-size:13px;
}

/* ===== MOBILE ===== */

@media(max-width:800px) {

    .block-container {
        padding:1rem;
    }

    .logo {
        font-size:30px;
    }

    .hero {
        min-height:650px;
        padding:35px 25px;
    }

    .hero-title {
        font-size:32px;
    }

    .hero-content {
        z-index:6;
    }

    .girl {
        width:75%;
        right:10%;
        bottom:0;
    }

    .signal-one {
        top:330px;
        right:5%;
    }

    .signal-two {
        top:410px;
        left:5%;
    }

    .signal-three {
        top:480px;
        right:5%;
    }

    .feature-row {
        flex-direction:column;
    }

    .input-card {
        padding:20px;
    }
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# BRAND
# -----------------------------

st.html("""
<div class="brand">

    <div class="logo">
        🛡️ Scam<span>Shield</span> AI
    </div>

    <div class="tagline">
        Detect. Understand. Protect.
    </div>

</div>
""")


# -----------------------------
# HERO
# -----------------------------

st.html(f"""
<div class="hero">

    <div class="signal-bubble signal-one">
        🎁 You won a prize!
    </div>

    <div class="signal-bubble signal-two">
        🚨 URGENT! Account blocked
    </div>

    <div class="signal-bubble signal-three">
        📩 KYC update required
    </div>

    <div class="hero-content">

        <div class="hero-badge">
            ✨ AI-POWERED SCAM DETECTION
        </div>

        <div class="hero-title">
            Before you click.<br>
            <span class="gradient">Before you pay.</span>
        </div>

        <div class="hero-text">
            Check suspicious messages, emails, WhatsApp texts
            and UPI requests before taking action.
        </div>

        <div class="feature-row">

            <div class="feature">
                🔍
                <b>Detect</b>
                <small>Find scam patterns</small>
            </div>

            <div class="feature">
                🧠
                <b>Understand</b>
                <small>Know why it's risky</small>
            </div>

            <div class="feature">
                🛡️
                <b>Protect</b>
                <small>Take safer action</small>
            </div>

        </div>

    </div>

    <img
    src="data:image/png;base64,{girl_base64}"
    class="girl"
>

</div>
""")


# -----------------------------
# INPUT SECTION
# -----------------------------

st.markdown("""
<div class="input-section-title">
    🔎 Check before you click
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="input-section-subtitle">
    Paste an SMS, WhatsApp message, email or UPI request below.
</div>
""", unsafe_allow_html=True)

message = st.text_area(
    "Message",
    height=160,
    label_visibility="collapsed",
    placeholder="""Example:
URGENT! Your bank account will be blocked today.
Complete your KYC immediately using this link."""
)

language = st.selectbox(
    "Response language",
    ["English", "Hindi", "Bengali"]
)

analyze_button = st.button(
    "🔍  Scan for Scam Risk  →",
    use_container_width=True
)


# -----------------------------
# ANALYSIS
# -----------------------------

if analyze_button:

    if not message.strip():

        st.warning("Please enter a suspicious message first.")

    else:

        with st.spinner("ScamShield AI is analyzing the message..."):

            try:

                result = analyze_message(
                    message,
                    language
                )

                st.session_state["result"] = result

            except Exception as e:

                st.error(f"Something went wrong: {e}")


# -----------------------------
# DISPLAY RESULT
# -----------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    risk_score = result.get("risk_score", 0)
    risk_level = result.get("risk_level", "UNKNOWN")
    category = result.get(
        "scam_category",
        "Unknown"
    )

    signals = result.get(
        "signals",
        []
    )

    evidence = result.get(
        "evidence",
        []
    )

    tactics = result.get(
        "manipulation_tactics",
        []
    )

    actions = result.get(
        "safe_actions",
        []
    )

    emergency = result.get(
        "emergency_guidance",
        False
    )


    # -------------------------
    # RISK RESULT
    # -------------------------

    st.html(f"""
<div class="risk-card">

    <div class="risk-label">
        🚨 {risk_level} RISK
    </div>

    <div class="risk-number">
        {risk_score}<span style="font-size:25px;">/100</span>
    </div>

    <div style="font-size:18px;">
        {category}
    </div>

</div>
""")


    # -------------------------
    # TWO COLUMNS
    # -------------------------

    col1, col2 = st.columns(2)


    # -------------------------
    # SUSPICIOUS SIGNALS
    # -------------------------

    with col1:

        st.markdown(
            '<div class="card-title">⚠️ Suspicious Signals</div>',
            unsafe_allow_html=True
        )

        for signal in signals:

            st.markdown(
                f'<div class="signal">⚠️ {signal}</div>',
                unsafe_allow_html=True
            )


    # -------------------------
    # EVIDENCE
    # -------------------------

    with col2:

        st.markdown(
            '<div class="card-title">🔎 Evidence</div>',
            unsafe_allow_html=True
        )

        for item in evidence:

            st.markdown(
                f'<div class="signal">🔎 {item}</div>',
                unsafe_allow_html=True
            )


    # -------------------------
    # EXPLAIN THE TRAP
    # -------------------------

    st.markdown(
        '<div class="card-title" style="margin-top:35px;">🧠 Explain the Trap</div>',
        unsafe_allow_html=True
    )

    st.html("""
<div class="trap">

    <div class="trap-step">
        😨 Fear
    </div>

    <div>→</div>

    <div class="trap-step">
        ⏰ Urgency
    </div>

    <div>→</div>

    <div class="trap-step">
        🏦 Authority
    </div>

    <div>→</div>

    <div class="trap-step">
        👆 Action
    </div>

    <div>→</div>

    <div class="trap-step">
        💸 Potential Loss
    </div>

</div>
""")


    # -------------------------
    # ACTUAL TACTICS
    # -------------------------

    st.markdown(
        '<div class="card-title" style="margin-top:25px;">🎭 Detected Manipulation Tactics</div>',
        unsafe_allow_html=True
    )

    for tactic in tactics:

        st.markdown(
            f'<div class="signal">🎭 {tactic}</div>',
            unsafe_allow_html=True
        )


    # -------------------------
    # SAFE ACTIONS
    # -------------------------

    st.markdown(
        '<div class="card-title" style="margin-top:35px;">🛡️ Safe Next Steps</div>',
        unsafe_allow_html=True
    )

    for action in actions:

        st.markdown(
            f'<div class="action">✓ {action}</div>',
            unsafe_allow_html=True
        )


    # -------------------------
    # EMERGENCY MODE
    # -------------------------

    if emergency:

     st.html("""
<div class="risk-card">

    <div style="font-size:24px;font-weight:700;">
        🚨 Emergency Guidance Available
    </div>

    <p>
        If you already clicked the link, shared sensitive information,
        or transferred money, use the emergency response flow.
    </p>

</div>
""")

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("""
<div class="footer">

ScamShield AI • AI-powered digital safety assistant<br>
Detect suspicious patterns. Understand the trap. Take safer action.

</div>
""", unsafe_allow_html=True)