import streamlit as st
from fractions import Fraction
import time
import random

# ==========================================
# 🌌 CYBER MATRIX UI THEME INJECTION
# ==========================================
st.markdown("""
    <style>
    .reportview-container { background: #000000; }
    .main { background-color: #000000; color: #00FF00; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00FF00 !important; text-shadow: 0 0 10px #00FF00; }
    div.stButton > button:first-child {
        background-color: #000000; color: #00FF00; border: 2px solid #00FF00;
        box-shadow: 0 0 10px #00FF00; font-family: 'Courier New', monospace; font-weight: bold;
    }
    div.stButton > button:first-child:hover { background-color: #00FF00; color: #000000; }
    .stTextInput>div>div>input {
        background-color: #111111; color: #00FF00; border: 1px solid #00FF00;
        font-family: 'Courier New', monospace;
    }
    div[data-testid="stMarkdownContainer"] { color: #00FF00; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ THE MATRIX: LOGIC SOURCE CORE V7")
st.write("Welcome to the Integrated Mathematical Calculator Core & Matrix Encryption System.")

# ==========================================
# 🎛️ SIDEBAR MENU SYSTEM
# ==========================================
st.sidebar.title("🎛️ CONTROL PANEL")
menu_choice = st.sidebar.selectbox(
    "Select Feature:",
    [
        "Home / Core Initializer",
        "1. Addition Mode",
        "2. Subtraction Mode",
        "3. Multiplication Mode",
        "4. Division Mode",
        "5. Advanced Formulas",
        "6. Mathematical Reference Lists",
        "7. Perimeter Formulas",
        "8. Hexadecimal ASCII Matrix Encryption",
        "9. Hexadecimal ASCII Matrix Decryption"
    ]
)

# ==========================================
# 0. HOME / REBOOT ANIMATION
# ==========================================
if menu_choice == "Home / Core Initializer":
    st.subheader("📟 SYSTEM STATUS: READY")
    if st.button("🧬 RUN CORE SECURITY CHECK"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        progresses = [0, 13, 31, 36, 43, 44, 58, 85, 97, 100]
        for p in progresses:
            status_text.text(f"Loading system core... {p}%")
            progress_bar.progress(p / 100)
            time.sleep(random.uniform(0.05, 0.2))
        st.success("🟢 System loaded successfully! Ready for high-precision deployment.")

# ==========================================
# 1. ADDITION MODE
# ==========================================
elif menu_choice == "1. Addition Mode":
    st.subheader("➕ [Addition Mode]")
    raw_one = st.text_input("Enter the first number or fraction:", key="plus1")
    raw_two = st.text_input("Enter the second number or fraction:", key="plus2")
    if st.button("RUN ADDITION"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"Result: {one} + {two} = {one + two}")
        except ValueError:
            st.error("❌ Error: Please enter a valid number or fraction!")

# ==========================================
# 2. SUBTRACTION MODE
# ==========================================
elif menu_choice == "2. Subtraction Mode":
    st.subheader("➖ [Subtraction Mode]")
    raw_one = st.text_input("Enter the minuend:", key="minus1")
    raw_two = st.text_input("Enter the subtrahend:", key="minus2")
    if st.button("RUN SUBTRACTION"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"Result: {one} - {two} = {one - two}")
        except ValueError:
            st.error("❌ Error: Please enter a valid number or fraction!")

# ==========================================
# 3. MULTIPLICATION MODE
# ==========================================
elif menu_choice == "3. Multiplication Mode":
    st.subheader("✖️ [Multiplication Mode]")
    raw_one = st.text_input("Enter the first multiplier:", key="mul1")
    raw_two = st.text_input("Enter the second multiplier:", key="mul2")
    if st.button("RUN MULTIPLICATION"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"Result: {one} × {two} = {one * two}")
        except ValueError:
            st.error("❌ Error: Please enter a valid number or fraction!")

# ==========================================
# 4. DIVISION MODE
# ==========================================
elif menu_choice == "4. Division Mode":
    st.subheader("➗ [Division Mode]")
    raw_one = st.text_input("Enter the dividend:", key="div1")
    raw_two = st.text_input("Enter the divisor:", key="div2")
    if st.button("RUN DIVISION"):
        if raw_two == "0":
            st.warning("⚠️ Error: Division by zero is not allowed!")
        else:
            try:
                one = Fraction(raw_one)
                two = Fraction(raw_two)
                st.code(f"Result: {one} ÷ {two} = {one / two}")
            except ValueError:
                st.error("❌ Error: Please enter a valid number or fraction!")

# ==========================================
# 5. ADVANCED FORMULAS
# ==========================================
elif menu_choice == "5. Advanced Formulas":
    sub_menu = st.radio("Select Formula Engine:", ["Quadratic Equation Solver", "Perfect Square Expansion", "Pythagorean Theorem"])
    
    if sub_menu == "Quadratic Equation Solver":
        st.subheader("📐 Quadratic Equation Calculator (ax² + bx + c = 0)")
        raw_a = st.text_input("Enter coefficient a:")
        raw_b = st.text_input("Enter coefficient b:")
        raw_c = st.text_input("Enter coefficient c:")
        if st.button("SOLVE EQUATION"):
            try:
                input_one, input_two, input_three = float(raw_a), float(raw_b), float(raw_c)
                if input_one == 0:
                    st.error("❌ Error: Coefficient 'a' cannot be 0.")
                else:
                    discriminant = input_two ** 2 - 4 * input_one * input_three
                    if discriminant < 0:
                        st.error("❌ Real roots do not exist for this equation.")
                    else:
                        anser_one = (-input_two + (discriminant ** 0.5)) / (2 * input_one)
                        anser_two = (-input_two - (discriminant ** 0.5)) / (2 * input_one)
                        st.success(f"🎉 Result: {anser_one} or {anser_two}")
            except ValueError:
                st.error("❌ Error: Invalid input. Please enter numbers only!")

    elif sub_menu == "Perfect Square Expansion":
        st.subheader("--- Perfect Square Formula Expansion (a²+2ab+b²) ---")
        raw_a = st.text_input("Enter value for a:", key="pf1")
        raw_b = st.text_input("Enter value for b:", key="pf2")
        if st.button("EXPAND FORMULA"):
            try:
                user_input_for_wan_quan_ping_fang_one = Fraction(raw_a)
                user_input_for_wan_quan_ping_fang_two = Fraction(raw_b)
                ansers_for_wan_quan_ping_fang = user_input_for_wan_quan_ping_fang_one ** 2 + 2 * user_input_for_wan_quan_ping_fang_one * user_input_for_wan_quan_ping_fang_two + user_input_for_wan_quan_ping_fang_two ** 2
                st.success(f"🎉 Expanded Result: {str(ansers_for_wan_quan_ping_fang)}")
            except ValueError:
                st.error("❌ Error: Please enter whole numbers or decimals!")

    elif sub_menu == "Pythagorean Theorem":
        st.subheader("--- Pythagorean Theorem Calculator ---")
        choice = st.selectbox("What are you calculating?", ["Hypotenuse -> Choice 1", "Leg -> Choice 2"])
        if choice == "Hypotenuse -> Choice 1":
            raw_a = st.text_input("Enter length of leg A:")
            raw_b = st.text_input("Enter length of leg B:")
            if st.button("CALCULATE HYPOTENUSE"):
                try:
                    a, b = Fraction(raw_a), Fraction(raw_b)
                    ans = (a ** 2 + b ** 2) ** 0.5
                    st.success(f"🎉 Hypotenuse length: {ans}")
                except ValueError:
                    st.error("❌ Error: Invalid input!")
        else:
            raw_a = st.text_input("Enter length of the known leg:")
            raw_c = st.text_input("Enter length of the hypotenuse:")
            if st.button("CALCULATE LEG"):
                try:
                    a, c = Fraction(raw_a), Fraction(raw_c)
                    if a >= c:
                        st.warning("⚠️ Error: Leg length cannot be greater than or equal to the hypotenuse!")
                    else:
                        ans = (c ** 2 - a ** 2) ** 0.5
                        st.success(f"🎉 The other leg length: {ans}")
                except ValueError:
                    st.error("❌ Error: Invalid input!")

# ==========================================
# 6. MATHEMATICAL REFERENCE TABLES
# ==========================================
elif menu_choice == "6. Mathematical Reference Lists":
    st.subheader("📚 System Internal Mathematical Database")
    ref_table = st.selectbox("Select Table Unit:", ["Multiplication Table", "Prime Numbers Matrix (Within 1000)", "Square Numbers Table", "Cube Numbers Database", "Common Pythagorean Triples"])
    
    if ref_table == "Multiplication Table":
        st.code("""
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
1x4=4 2x4=8 3x4=12 4x4=16
1x5=5 2x5=10 3x5=15 4x5=20 5x5=25
1x6=6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36
1x7=7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49
1x8=8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64
1x9=9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81
        """)
    elif ref_table == "Prime Numbers Matrix (Within 1000)":
        st.code("""
2,    3,    5,    7,   11,   13,   17,   19,   23,   29, 
31,   37,   41,   43,   47,   53,   59,   61,   67,   71, 
73,   79,   83,   89,   97,  101,  103,  107,  109,  113, 
127,  131,  137,  139,  149,  151,  157,  163,  167,  173, 
179,  181,  191,  193,  197,  199,  211,  223,  227,  229, 
233,  239,  241,  251,  257,  263,  269,  271,  277,  281, 
283,  293,  307,  311,  313,  317,  331,  337,  347,  349, 
353,  359,  367,  373,  379,  383,  389,  397,  401,  409, 
419,  421,  431,  433,  439,  443,  449,  457,  461,  463, 
467,  479,  487,  491,  499,  503,  509,  521,  523,  541, 
547,  557,  563,  569,  571,  577,  587,  593,  599,  601, 
607,  613,  617,  619,  631,  641,  643,  647,  653,  659, 
661,  673,  677,  683,  691,  701,  709,  719,  727,  733, 
739,  743,  751,  757,  761,  769,  773,  779,  787,  797, 
809,  811,  821,  823,  827,  829,  839,  853,  857,  859, 
863,  877,  881,  883,  887,  907,  911,  919,  929,  937, 
941,  947,  953,  967,  971,  977,  983,  991,  997
        """)
    elif ref_table == "Square Numbers Table":
        st.code("""
1^2 = 1          2^2 = 4          3^2 = 9          4^2 = 16   
5^2 = 25         6^2 = 36         7^2 = 49         8^2 = 64   
9^2 = 81         10^2 = 100       11^2 = 121       12^2 = 144  
13^2 = 169       14^2 = 196       15^2 = 225       16^2 = 256  
17^2 = 289       18^2 = 324       19^2 = 361       20^2 = 400  
21^2 = 441       22^2 = 484       23^2 = 529       24^2 = 576  
25^2 = 625       26^2 = 676       27^2 = 729       28^2 = 784  
29^2 = 841       30^2 = 900       31^2 = 961
        """)
    elif ref_table == "Cube Numbers Database":
        st.code("""
┌────────────────────────────────────────────────────────────────────────┐
│  ▶▶▶ [SYSTEM DATABASE] UNLOCKED: PERFECT CUBE NUMBERS (1-10) ◀◀◀       │
├────────────────────────────────────────────────────────────────────────┤
│    [001]  01³ = 1                   [006]  06³ = 216                   │
│    [002]  02³ = 8                   [007]  07³ = 343                   │
│    [003]  03³ = 27                  [008]  08³ = 512                   │
│    [004]  04³ = 64                  [009]  09³ = 729                   │
│    [005]  05³ = 125                 [010]  10³ = 1000                  │
└────────────────────────────────────────────────────────────────────────┘
        """)
    elif ref_table == "Common Pythagorean Triples":
        st.code("""
    Leg1  Leg2  Hypotenuse
    3  —  4  —  5
    5  —  12 —  13
    8  —  15 —  17
    7  —  24 —  25
    9  —  40 —  41
    11 —  60 —  61
    12 —  35 —  37
    20 —  21 —  29
        """)

# ==========================================
# 7. PERIMETER FORMULAS
# ==========================================
elif menu_choice == "7. Perimeter Formulas":
    st.subheader("📐 Perimeter Calculation Mode")
    shape = st.selectbox("Select Shape Unit:", ["Rectangle", "Triangle", "Circle Circumference", "Quadrilateral"])
    
    if shape == "Rectangle":
        c = st.text_input("Enter width:", key="rec1")
        d = st.text_input("Enter length:", key="rec2")
        if st.button("CALCULATE RECTANGLE PERIMETER"):
            st.success(f"Perimeter: {(Fraction(c)+Fraction(d))*2}")
            
    elif shape == "Triangle":
        d = st.text_input("Side length 1:", key="tri1")
        b_side = st.text_input("Side length 2:", key="tri2")
        c = st.text_input("Side length 3:", key="tri3")
        if st.button("CALCULATE TRIANGLE PERIMETER"):
            try:
                d_f, b_f, c_f = Fraction(d), Fraction(b_side), Fraction(c)
                if d_f >= (b_f+c_f) or b_f >= (c_f+d_f) or c_f >= (d_f+b_f):
                    st.error("❌ Invalid Triangle: The sum of any two sides must be greater than the third side.")
                else:
                    st.success(f"Triangle Perimeter: {d_f + b_f + c_f}")
            except ValueError: st.error("❌ Please enter valid numbers.")
            
    elif shape == "Circle Circumference":
        pi_mode = st.radio("Select Precision Level:", ["Low Precision (π = 3)", "Standard Mode (π = 3.14)", "High Precision (π = 3.1415926)"])
        r = st.text_input("Enter circle radius:")
        if st.button("CALCULATE CIRCUMFERENCE"):
            r_val = float(r)
            pi_val = 3.0 if "Low" in pi_mode else (3.14 if "Standard" in pi_mode else 3.1415926)
            st.success(f"Circumference: {pi_val * r_val * 2}")
            
    elif shape == "Quadrilateral":
        g1 = st.text_input("Side 1 (ganjinwanshi):", key="quad1")
        g2 = st.text_input("Side 2 (ganjinwanshizaiyibian):", key="quad2")
        g3 = st.text_input("Side 3 (ganjinwanshidisanbian):", key="quad3")
        g4 = st.text_input("Side 4 (zhongyuyaowanshilema):", key="quad4")
        if st.button("CALCULATE QUADRILATERAL PERIMETER"):
            try:
                st.success(f"🎉 Quadrilateral Perimeter: {Fraction(g1) + Fraction(g2) + Fraction(g3) + Fraction(g4)}")
            except ValueError: st.error("❌ Please enter numbers.")

# ==========================================
# 8. MATRIX CIPHER ENCRYPTION ENGINE
# ==========================================
elif menu_choice == "8. Hexadecimal ASCII Matrix Encryption":
    st.subheader("🔐 Hexadecimal Caesar Encryption")
    user_input = st.text_input("Enter password to encrypt:", key="enc_input")
    if st.button("🔥 INJECT CIPHER"):
        if user_input:
            list_one = []
            for i in user_input:
                list_one.append(hex(ord(i) + 3)[2:])
            clean_output = " ".join(list_one)
            st.info("Encryption Complete! Terminal stream output:")
            st.code(clean_output)
        else:
            st.warning("Input required before matrix injection.")

# ==========================================
# 9. MATRIX CIPHER DECRYPTION ENGINE (FIXED!)
# ==========================================
elif menu_choice == "9. Hexadecimal ASCII Matrix Decryption":
    st.subheader("🔓 Hexadecimal Caesar Decryption")
    st.write("💡 *Notice: Ensure hexadecimal chars are separated by SPACES (e.g., `6b 64 75 75 bc`)*")
    user_input = st.text_input("Paste ciphertext stream here:", key="dec_input")
    if st.button("🟢 BREAK MATRIX CIPHER"):
        if user_input:
            try:
                new_list = user_input.split()
                new_list_ = []
                for i in new_list:
                    new_list_.append(chr(int(i, 16) - 3))
                clean_output = "".join(new_list_)
                st.success("🎉 Decryption Complete! Recovered baseline data:")
                st.code(clean_output)
            except Exception as e:
                st.error("❌ Matrix Error! Verify data spacing format matches standard hex stream structures.")
        else:
            st.warning("Hexadecimal data stream cannot be blank.")

# ==========================================
# 📜 FOOTER SYSTEM META
# ==========================================
st.markdown("---")
st.caption("© 2026 Harry's Cyber Workshop | Moose Jaw Facility | Powered by Streamlit")
