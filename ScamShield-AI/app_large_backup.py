import streamlit as st
from gemini_service import analyze_message
import base64
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# IMAGE LOADER
# ============================================================

def get_base64_image(path):

    path = Path(path)

    if not path.exists():
        return ""

    return base64.b64encode(
        path.read_bytes()
    ).decode()


girl_img = get_base64_image("assets/girl.png")
girl_smile_img = get_base64_image("assets/girl_smile.png")


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


/* =========================================================
   GLOBAL
========================================================= */

* {
    font-family: 'Inter', sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 10% 15%,
            rgba(124,58,237,0.20),
            transparent 30%
        ),

        radial-gradient(
            circle at 90% 20%,
            rgba(14,165,233,0.15),
            transparent 30%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(236,72,153,0.08),
            transparent 35%
        ),

        #050814;

    color: #f8fafc;

    overflow-x: hidden;
}


.block-container {

    max-width: 1250px;

    padding-top: 1.2rem;
    padding-bottom: 4rem;
}


/* =========================================================
   REMOVE STREAMLIT DEFAULT SPACING
========================================================= */

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    display: none;
}


/* =========================================================
   TOP NAV
========================================================= */

.navbar {

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 12px 18px;

    margin-bottom: 20px;

    background:
        rgba(10,15,30,0.65);

    border:

        1px solid
        rgba(148,163,184,0.10);

    border-radius: 18px;

    backdrop-filter: blur(18px);

    animation:
        navDrop
        0.8s
        ease-out;
}


@keyframes navDrop {

    from {

        opacity: 0;

        transform:
            translateY(-20px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


.logo {

    font-size: 28px;

    font-weight: 800;

    letter-spacing: -1px;

}


.logo-blue {

    color: #60a5fa;

}


.logo-purple {

    color: #a78bfa;

}


.nav-links {

    display: flex;

    gap: 10px;

}


.nav-item {

    padding:
        9px 15px;

    border-radius: 12px;

    color: #aab4c8;

    font-size: 13px;

    transition:
        0.3s ease;

}


.nav-item:hover {

    color: white;

    background:
        rgba(124,58,237,0.15);

    transform:
        translateY(-2px);

}


/* =========================================================
   HERO AREA
========================================================= */

.hero-stage {

    position: relative;

    min-height: 520px;

    overflow: hidden;

    border-radius: 30px;

    padding: 65px 55px 35px;

    margin-bottom: 35px;

    background:

        radial-gradient(
            circle at 75% 45%,
            rgba(124,58,237,0.18),
            transparent 30%
        ),

        linear-gradient(
            135deg,
            rgba(16,24,45,0.95),
            rgba(7,11,25,0.95)
        );

    border:
        1px solid
        rgba(129,140,248,0.18);

    box-shadow:

        0 30px 80px
        rgba(0,0,0,0.35);

}


/* =========================================================
   BACKGROUND ORBS
========================================================= */

.orb {

    position: absolute;

    border-radius: 50%;

    filter: blur(1px);

    pointer-events: none;

    animation:
        floatOrb
        6s
        ease-in-out
        infinite;

}


.orb1 {

    width: 120px;

    height: 120px;

    background:
        rgba(124,58,237,0.12);

    top: 30px;

    left: 30px;

}


.orb2 {

    width: 80px;

    height: 80px;

    background:
        rgba(59,130,246,0.13);

    right: 100px;

    top: 80px;

    animation-delay: 1.5s;

}


.orb3 {

    width: 60px;

    height: 60px;

    background:
        rgba(236,72,153,0.12);

    right: 40%;

    bottom: 30px;

    animation-delay: 3s;

}


@keyframes floatOrb {

    0%,100% {

        transform:
            translate3d(0,0,0)
            rotate(0deg);

    }

    50% {

        transform:
            translate3d(8px,-15px,0)
            rotate(8deg);

    }

}


/* =========================================================
   HERO TEXT
========================================================= */

.hero-content {

    position: relative;

    z-index: 4;

    max-width: 650px;

    animation:
        heroText
        1.5s
        cubic-bezier(.16,1,.3,1)
        both;

}


@keyframes heroText {

    0% {

        opacity: 0;

        transform:
            translateX(-80px);

    }

    70% {

        opacity: 1;

    }

    100% {

        transform:
            translateX(0);

    }

}


.badge {

    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding:
        9px 15px;

    border-radius: 50px;

    background:
        rgba(168,85,247,0.12);

    border:
        1px solid
        rgba(168,85,247,0.30);

    color: #d8b4fe;

    font-size: 13px;

    font-weight: 600;

    margin-bottom: 20px;

    animation:
        badgeAppear
        1s
        ease-out
        0.3s
        both;

}


@keyframes badgeAppear {

    from {

        opacity: 0;

        transform:
            scale(.8);

    }

    to {

        opacity: 1;

        transform:
            scale(1);

    }

}


.hero-title {

    font-size:
        clamp(42px, 5vw, 70px);

    line-height: 1.02;

    font-weight: 800;

    letter-spacing:
        -3px;

    margin: 0;

}


.hero-title .white {

    color: white;

}


.hero-title .gradient {

    background:

        linear-gradient(
            90deg,
            #60a5fa,
            #8b5cf6,
            #ec4899
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color:
        transparent;

}


.hero-description {

    color: #9aa7bd;

    font-size: 16px;

    line-height: 1.7;

    max-width: 580px;

    margin-top: 22px;

}


/* =========================================================
   DETECT / UNDERSTAND / PROTECT
========================================================= */

.feature-row {

    display: flex;

    gap: 14px;

    margin-top: 30px;

}


.feature {

    display: flex;

    align-items: center;

    gap: 10px;

    animation:
        featureReveal
        1s
        ease-out
        both;

}


.feature:nth-child(1) {
    animation-delay: .4s;
}

.feature:nth-child(2) {
    animation-delay: .6s;
}

.feature:nth-child(3) {
    animation-delay: .8s;
}


@keyframes featureReveal {

    from {

        opacity: 0;

        transform:
            translateY(20px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


.feature-icon {

    width: 42px;

    height: 42px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    font-size: 18px;

}


.detect {

    background:
        rgba(236,72,153,0.15);

    box-shadow:
        0 0 25px
        rgba(236,72,153,0.15);

}


.understand {

    background:
        rgba(59,130,246,0.15);

}


.protect {

    background:
        rgba(34,197,94,0.15);

}


.feature-text strong {

    display: block;

    font-size: 13px;

}


.feature-text span {

    color: #7f8ba3;

    font-size: 11px;

}


/* =========================================================
   GIRL
========================================================= */

.girl-container {

    position: absolute;

    z-index: 5;

    right: 4%;

    bottom: -15px;

    width: 43%;

    max-width: 500px;

    display: flex;

    justify-content: center;

    align-items: flex-end;

    animation:
        girlRise
        1.8s
        cubic-bezier(.16,1,.3,1)
        both;

}


@keyframes girlRise {

    0% {

        opacity: 0;

        transform:
            translateY(180px)
            scale(.92);

    }

    65% {

        opacity: 1;

    }

    100% {

        transform:
            translateY(0)
            scale(1);

    }

}


.girl {

    width: 100%;

    height: auto;

    display: block;

    filter:

        drop-shadow(
            0 25px 45px
            rgba(0,0,0,.55)
        )

        drop-shadow(
            0 0 35px
            rgba(124,58,237,.22)
        );

    animation:
        girlFloat
        5s
        ease-in-out
        infinite;

}


@keyframes girlFloat {

    0%,100% {

        transform:
            translateY(0)
            rotate(0deg);

    }

    25% {

        transform:
            translateY(-6px)
            rotate(-0.7deg);

    }

    50% {

        transform:
            translateY(-12px)
            rotate(0.5deg);

    }

    75% {

        transform:
            translateY(-5px)
            rotate(0.7deg);

    }

}


/* Optional smile image */

.girl-smile {

    position: absolute;

    width: 100%;

    opacity: 0;

    animation:
        smileSwitch
        8s
        ease-in-out
        infinite;

}


@keyframes smileSwitch {

    0%,35% {

        opacity: 0;

    }

    45%,65% {

        opacity: 1;

    }

    75%,100% {

        opacity: 0;

    }

}


/* =========================================================
   FLOATING SCAM BUBBLES
========================================================= */

.scam-bubble {

    position: absolute;

    z-index: 3;

    padding:
        14px 18px;

    border-radius: 16px;

    backdrop-filter:
        blur(12px);

    font-size: 13px;

    font-weight: 600;

    box-shadow:
        0 15px 35px
        rgba(0,0,0,.25);

    animation:
        bubbleAppear
        1.2s
        cubic-bezier(.16,1,.3,1)
        both,
        bubbleFloat
        5s
        ease-in-out
        infinite;

}


.bubble1 {

    top: 65px;

    right: 34%;

    background:
        rgba(34,197,94,.10);

    border:
        1px solid
        rgba(34,197,94,.45);

    color: #86efac;

    animation-delay:
        1.2s,
        2s;

}


.bubble2 {

    top: 150px;

    right: 4%;

    background:
        rgba(59,130,246,.10);

    border:
        1px solid
        rgba(59,130,246,.45);

    color: #93c5fd;

    animation-delay:
        1.5s,
        2.5s;

}


.bubble3 {

    top: 275px;

    right: 30%;

    background:
        rgba(236,72,153,.10);

    border:
        1px solid
        rgba(236,72,153,.45);

    color: #f9a8d4;

    animation-delay:
        1.8s,
        3s;

}


@keyframes bubbleAppear {

    from {

        opacity: 0;

        transform:
            translateY(35px)
            scale(.8);

    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);

    }

}


@keyframes bubbleFloat {

    0%,100% {

        margin-top: 0;

    }

    50% {

        margin-top: -9px;

    }

}


/* =========================================================
   ANALYZER CARD
========================================================= */

.analyzer {

    position: relative;

    z-index: 10;

    padding: 30px;

    border-radius: 26px;

    background:

        linear-gradient(
            135deg,
            rgba(18,27,50,.94),
            rgba(10,15,31,.92)
        );

    border:
        1px solid
        rgba(99,102,241,.30);

    box-shadow:

        0 20px 60px
        rgba(0,0,0,.30),

        inset 0 1px 0
        rgba(255,255,255,.04);

}


.analyzer-title {

    font-size: 23px;

    font-weight: 750;

    margin-bottom: 6px;

}


.analyzer-subtitle {

    color: #8491a8;

    font-size: 14px;

    margin-bottom: 20px;

}


/* =========================================================
   STREAMLIT INPUTS
========================================================= */

textarea {

    background:
        rgba(5,10,24,.75) !important;

    border:
        1px solid
        rgba(148,163,184,.18) !important;

    border-radius:
        16px !important;

    color: white !important;

    transition:
        .3s ease !important;

}


textarea:focus {

    border:
        1px solid
        rgba(139,92,246,.75) !important;

    box-shadow:

        0 0 0 3px
        rgba(139,92,246,.10),

        0 0 25px
        rgba(139,92,246,.12) !important;

}


/* SELECTBOX */

div[data-baseweb="select"] > div {

    background:
        rgba(5,10,24,.75) !important;

    border:
        1px solid
        rgba(148,163,184,.18) !important;

    border-radius:
        14px !important;

}


/* =========================================================
   BUTTON
========================================================= */

.stButton > button {

    border: none !important;

    border-radius:
        15px !important;

    min-height:
        52px !important;

    font-size:
        15px !important;

    font-weight:
        700 !important;

    color: white !important;

    background:

        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6,
            #d946ef
        ) !important;

    box-shadow:

        0 8px 25px
        rgba(124,58,237,.28);

    transition:
        all .3s ease !important;

}


.stButton > button:hover {

    transform:
        translateY(-3px)
        scale(1.01);

    box-shadow:

        0 14px 35px
        rgba(139,92,246,.45);

}


.stButton > button:active {

    transform:
        scale(.98);

}


/* =========================================================
   EXAMPLE BUTTONS
========================================================= */

.example-title {

    margin-top: 22px;

    margin-bottom: 10px;

    color: #aab5ca;

    font-size: 13px;

}


.example-pill {

    display: inline-block;

    padding:
        9px 14px;

    margin:
        4px;

    border-radius: 50px;

    background:
        rgba(30,41,59,.75);

    border:
        1px solid
        rgba(148,163,184,.15);

    color: #cbd5e1;

    font-size: 12px;

    transition:
        .3s ease;

}


.example-pill:hover {

    transform:
        translateY(-3px);

    border-color:
        rgba(139,92,246,.55);

    background:
        rgba(124,58,237,.12);

}


/* =========================================================
   RESULT CARD
========================================================= */

.risk-card {

    position: relative;

    overflow: hidden;

    margin-top: 28px;

    padding: 30px;

    border-radius: 24px;

    background:

        radial-gradient(
            circle at 90% 20%,
            rgba(239,68,68,.16),
            transparent 35%
        ),

        linear-gradient(
            135deg,
            rgba(80,20,35,.55),
            rgba(15,23,42,.9)
        );

    border:
        1px solid
        rgba(248,113,113,.28);

    animation:
        resultReveal
        .7s
        cubic-bezier(.16,1,.3,1);

}


@keyframes resultReveal {

    from {

        opacity: 0;

        transform:
            translateY(25px)
            scale(.98);

    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);

    }

}


.risk-number {

    font-size:
        clamp(48px,6vw,72px);

    font-weight:
        800;

    line-height:
        1;

    margin:
        10px 0;

}


.risk-label {

    color:
        #fca5a5;

    font-weight:
        700;

    font-size:
        13px;

    letter-spacing:
        1px;

}


/* =========================================================
   SIGNALS
========================================================= */

.signal {

    padding:
        14px 16px;

    margin:
        9px 0;

    border-radius:
        13px;

    background:
        rgba(30,41,59,.65);

    border:
        1px solid
        rgba(148,163,184,.10);

    border-left:
        3px solid
        #8b5cf6;

    transition:
        .3s ease;

    animation:
        signalReveal
        .5s
        ease-out
        both;

}


.signal:hover {

    transform:
        translateX(5px);

    background:
        rgba(124,58,237,.10);

}


@keyframes signalReveal {

    from {

        opacity: 0;

        transform:
            translateX(-15px);

    }

    to {

        opacity: 1;

        transform:
            translateX(0);

    }

}


/* =========================================================
   SAFE ACTION
========================================================= */

.action {

    padding:
        14px 16px;

    margin:
        9px 0;

    border-radius:
        13px;

    background:
        rgba(34,197,94,.07);

    border:
        1px solid
        rgba(34,197,94,.12);

    border-left:
        3px solid
        #4ade80;

    transition:
        .3s ease;

}


.action:hover {

    transform:
        translateX(5px);

    background:
        rgba(34,197,94,.12);

}


/* =========================================================
   TRAP FLOW
========================================================= */

.trap {

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    gap:
        10px;

    flex-wrap:
        wrap;

    margin-top:
        15px;

}


.trap-step {

    padding:
        14px 18px;

    border-radius:
        14px;

    background:
        rgba(20,27,48,.8);

    border:
        1px solid
        rgba(99,102,241,.20);

    font-size:
        13px;

    font-weight:
        600;

    transition:
        .3s ease;

}


.trap-step:hover {

    transform:
        translateY(-4px);

    border-color:
        rgba(139,92,246,.55);

    box-shadow:
        0 8px 25px
        rgba(124,58,237,.15);

}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align:
        center;

    color:
        #59657b;

    margin-top:
        55px;

    font-size:
        12px;

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 850px) {

    .nav-links {
        display: none;
    }


    .hero-stage {

        min-height:
            750px;

        padding:
            40px 25px;

    }


    .hero-content {

        max-width:
            100%;

    }


    .hero-title {

        font-size:
            42px;

        letter-spacing:
            -2px;

    }


    .feature-row {

        flex-direction:
            column;

    }


    .girl-container {

        width:
            75%;

        right:
            12%;

        bottom:
            -5px;

    }


    .bubble1 {

        right:
            10%;

        top:
            340px;

    }


    .bubble2 {

        right:
            3%;

        top:
            430px;

    }


    .bubble3 {

        left:
            5%;

        top:
            500px;

    }


    .analyzer {

        padding:
            20px;

    }

}


@media (max-width: 500px) {

    .hero-stage {

        min-height:
            680px;

    }


    .hero-title {

        font-size:
            35px;

    }


    .hero-description {

        font-size:
            14px;

    }


    .girl-container {

        width:
            82%;

        right:
            8%;

    }


    .scam-bubble {

        font-size:
            10px;

        padding:
            9px 12px;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================

st.markdown("""
<div class="navbar">

    <div class="logo">
        🛡️ Scam<span class="logo-blue">Shield</span>
        <span class="logo-purple">AI</span>
    </div>

    <div class="nav-links">

        <div class="nav-item">⌂ Home</div>

        <div class="nav-item">◉ How It Works</div>

        <div class="nav-item">▣ About</div>

        <div class="nav-item">♢ Safety Tips</div>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

girl_html = ""

if girl_img:

    girl_html = f"""
    <div class="girl-container">

        <img
            class="girl"
            src="data:image/png;base64,{girl_img}"
        >

        {
            f'''
            <img
                class="girl girl-smile"
                src="data:image/png;base64,{girl_smile_img}"
            >
            '''
            if girl_smile_img
            else ""
        }

    </div>
    """


st.markdown(f"""

<div class="hero-stage">

    <div class="orb orb1"></div>
    <div class="orb orb2"></div>
    <div class="orb orb3"></div>


    <!-- FLOATING SCAM MESSAGES -->

    <div class="scam-bubble bubble1">
        🎁 You won a prize!<br>
        <small>Click here...</small>
    </div>

    <div class="scam-bubble bubble2">
        ⚠️ Your KYC is pending<br>
        <small>Update now...</small>
    </div>

    <div class="scam-bubble bubble3">
        💳 Claim your cashback!
    </div>


    <!-- HERO CONTENT -->

    <div class="hero-content">

        <div class="badge">
            ✦ AI-POWERED SCAM DETECTION
        </div>


        <h1 class="hero-title">

            <span class="white">
                Before you click.
            </span>

            <br>

            <span class="gradient">
                Before you pay.
            </span>

        </h1>


        <p class="hero-description">

            Check suspicious SMS, WhatsApp messages,
            emails and UPI requests before you act.
            Understand the manipulation and know
            what to do next.

        </p>


        <div class="feature-row">

            <div class="feature">

                <div class="feature-icon detect">
                    🔍
                </div>

                <div class="feature-text">
                    <strong>Detect</strong>
                    <span>Find scam patterns</span>
                </div>

            </div>


            <div class="feature">

                <div class="feature-icon understand">
                    🧠
                </div>

                <div class="feature-text">
                    <strong>Understand</strong>
                    <span>Know why it's risky</span>
                </div>

            </div>


            <div class="feature">

                <div class="feature-icon protect">
                    🛡️
                </div>

                <div class="feature-text">
                    <strong>Protect</strong>
                    <span>Take safer action</span>
                </div>

            </div>

        </div>

    </div>


    {girl_html}

</div>

""", unsafe_allow_html=True)


# ============================================================
# ANALYZER
# ============================================================

st.markdown("""
<div class="analyzer">

    <div class="analyzer-title">
        🔎 Check a suspicious message
    </div>

    <div class="analyzer-subtitle">
        Paste an SMS, WhatsApp message, email or UPI request
        and let ScamShield AI investigate it.
    </div>

</div>
""", unsafe_allow_html=True)


message = st.text_area(
    "Suspicious message",
    height=160,
    placeholder="""Example:

URGENT! Your bank account will be blocked today.
Complete your KYC immediately using this link.""",
    label_visibility="collapsed"
)


col1, col2 = st.columns([1, 2])


with col1:

    language = st.selectbox(
        "Response language",
        ["English", "Hindi", "Bengali"]
    )


with col2:

    st.markdown(
        '<div style="height:28px;"></div>',
        unsafe_allow_html=True
    )

    analyze_button = st.button(
        "🔍  Analyze with ScamShield AI  →",
        use_container_width=True
    )


# ============================================================
# EXAMPLES
# ============================================================

st.markdown("""
<div class="example-title">
    💡 Try a sample
</div>

<div>

<span class="example-pill">🏦 Fake bank alert</span>

<span class="example-pill">🎁 Prize message</span>

<span class="example-pill">🔗 Suspicious link</span>

<span class="example-pill">📞 Unknown caller</span>

<span class="example-pill">💳 UPI payment request</span>

</div>
""", unsafe_allow_html=True)


# ============================================================
# ANALYSIS
# ============================================================

if analyze_button:

    if not message.strip():

        st.warning(
            "Please enter a suspicious message first."
        )

    else:

        with st.spinner(
            "🧠 ScamShield AI is investigating..."
        ):

            try:

                result = analyze_message(
                    message,
                    language
                )

                st.session_state["result"] = result

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ============================================================
# DISPLAY RESULT
# ============================================================

if "result" in st.session_state:

    result = st.session_state["result"]


    risk_score = result.get(
        "risk_score",
        0
    )

    risk_level = result.get(
        "risk_level",
        "UNKNOWN"
    )

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


    # ========================================================
    # RISK SCORE
    # ========================================================

    st.markdown(f"""

    <div class="risk-card">

        <div class="risk-label">
            🚨 {risk_level} RISK
        </div>

        <div class="risk-number">
            {risk_score}
            <span style="
                font-size:24px;
                color:#94a3b8;
            ">
                /100
            </span>
        </div>

        <div style="
            color:#dbeafe;
            font-size:17px;
            font-weight:600;
        ">
            {category}
        </div>

    </div>

    """, unsafe_allow_html=True)


    # ========================================================
    # SIGNALS / EVIDENCE
    # ========================================================

    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            "### ⚠️ Suspicious Signals"
        )

        for signal in signals:

            st.markdown(
                f"""
                <div class="signal">
                    ⚠️ {signal}
                </div>
                """,
                unsafe_allow_html=True
            )


    with col2:

        st.markdown(
            "### 🔎 Evidence"
        )

        for item in evidence:

            st.markdown(
                f"""
                <div class="signal">
                    🔎 {item}
                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # TRAP
    # ========================================================

    st.markdown(
        "### 🧠 How the scam works"
    )


    st.markdown("""
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
    """, unsafe_allow_html=True)


    # ========================================================
    # TACTICS
    # ========================================================

    st.markdown(
        "### 🎭 Detected Manipulation Tactics"
    )


    for tactic in tactics:

        st.markdown(
            f"""
            <div class="signal">
                🎭 {tactic}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # SAFE ACTIONS
    # ========================================================

    st.markdown(
        "### 🛡️ Safe Next Steps"
    )


    for action in actions:

        st.markdown(
            f"""
            <div class="action">
                ✓ {action}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # EMERGENCY
    # ========================================================

    if emergency:

        st.markdown("""
        <div class="risk-card">

            <div style="
                font-size:22px;
                font-weight:750;
            ">
                🚨 Emergency Guidance
            </div>

            <p style="color:#cbd5e1;">
                If you already clicked the link,
                shared sensitive information,
                or transferred money, follow
                the emergency response steps.
            </p>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    🛡️ ScamShield AI

    <br>

    Detect suspicious patterns.
    Understand the trap.
    Take safer action.

</div>
""", unsafe_allow_html=True)