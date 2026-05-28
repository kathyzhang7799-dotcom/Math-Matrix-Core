import streamlit as st
from fractions import Fraction
import time
import random

# ==========================================
# 🌌 黑客帝國暗黑螢光綠主題樣式注入
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
st.write("欢迎来到整合數學計算核心與矩陣加密系統。本核心配備完善的防呆與錯誤處理機制。")

# ==========================================
# 📑 側邊欄：功能主選單
# ==========================================
st.sidebar.title("🎛️ 控制面板")
menu_choice = st.sidebar.selectbox(
    "請選擇核心功能：",
    [
        "主頁 / 系統加載",
        "1. 加法模式 (Addition)",
        "2. 減法模式 (Subtraction)",
        "3. 乘法模式 (Multiplication)",
        "4. 除法模式 (Division)",
        "5. 高級公式 (Advanced Formulas)",
        "6. 數學參考表格 (Reference Lists)",
        "7. 周長公式 (Perimeter Formulas)",
        "8. 十六進制 ASCII 矩陣加密",
        "9. 十六進制 ASCII 矩陣解密"
    ]
)

# ==========================================
# 0. 主頁系統加載動畫
# ==========================================
if menu_choice == "主頁 / 系統加載":
    st.subheader("📟 SYSTEM STATUS: READY")
    if st.button("🧬 執行核心安全檢測"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        progresses = [0, 13, 31, 36, 43, 44, 58, 85, 97, 100]
        for p in progresses:
            status_text.text(f"Loading system core... {p}%")
            progress_bar.progress(p / 100)
            time.sleep(random.uniform(0.05, 0.2))
        st.success("🟢 系統加載成功！歡迎使用 Integrated Math Calculator Core。")

# ==========================================
# 1. 加法模式
# ==========================================
elif menu_choice == "1. 加法模式 (Addition)":
    st.subheader("➕ [Addition Mode]")
    raw_one = st.text_input("輸入第一個數字或分數：", key="plus1")
    raw_two = st.text_input("輸入第二個數字或分數：", key="plus2")
    if st.button("計算和 (RUN ADDITION)"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"Result: {one} + {two} = {one + two}")
        except ValueError:
            st.error("❌ 錯誤：請輸入有效的整數、小數或分數（例如 3/4）！")

# ==========================================
# 2. 減法模式
# ==========================================
elif menu_choice == "2. 減法模式 (Subtraction)":
    st.subheader("➖ [Subtraction Mode]")
    raw_one = st.text_input("輸入被減數：", key="minus1")
    raw_two = st.text_input("輸入減數：", key="minus2")
    if st.button("計算差 (RUN SUBTRACTION)"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"Result: {one} - {two} = {one - two}")
        except ValueError:
            st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 3. 乘法模式
# ==========================================
elif menu_choice == "3. 乘法模式 (Multiplication)":
    st.subheader("✖️ [Multiplication Mode]")
    raw_one = st.text_input("輸入第一個因數：", key="mul1")
    raw_two = st.text_input("輸入第二個因數：", key="mul2")
    if st.button("計算積 (RUN MULTIPLICATION)"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"Result: {one} × {two} = {one * two}")
        except ValueError:
            st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 4. 除法模式
# ==========================================
elif menu_choice == "4. 除法模式 (Division)":
    st.subheader("➗ [Division Mode]")
    raw_one = st.text_input("輸入被除數：", key="div1")
    raw_two = st.text_input("輸入除數：", key="div2")
    if st.button("計算商 (RUN DIVISION)"):
        if raw_two == "0":
            st.warning("⚠️ 錯誤：除數不能為零！")
        else:
            try:
                one = Fraction(raw_one)
                two = Fraction(raw_two)
                st.code(f"Result: {one} ÷ {two} = {one / two}")
            except ValueError:
                st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 5. 高級公式
# ==========================================
elif menu_choice == "5. 高級公式 (Advanced Formulas)":
    sub_menu = st.radio("選擇公式類型：", ["一元二次方程求解器", "完全平方公式展開", "勾股定理（畢氏定理）"])
    
    if sub_menu == "一元二次方程求解器":
        st.subheader("📐 Quadratic Equation Solver (ax² + bx + c = 0)")
        raw_a = st.text_input("輸入係數 a：")
        raw_b = st.text_input("輸入係數 b：")
        raw_c = st.text_input("輸入係數 c：")
        if st.button("求解方程"):
            try:
                input_one, input_two, input_three = float(raw_a), float(raw_b), float(raw_c)
                if input_one == 0:
                    st.error("❌ 錯誤：二次項係數 'a' 不能為 0。")
                else:
                    discriminant = input_two ** 2 - 4 * input_one * input_three
                    if discriminant < 0:
                        st.error("❌ 錯誤：此方程無實數根。")
                    else:
                        ans_one = (-input_two + (discriminant ** 0.5)) / (2 * input_one)
                        ans_two = (-input_two - (discriminant ** 0.5)) / (2 * input_one)
                        st.success(f"🎉 求解成功！ roots: {ans_one} 或 {ans_two}")
            except ValueError:
                st.error("❌ 錯誤：請確保輸入的全部為數字！")

    elif sub_menu == "完全平方公式展開":
        st.subheader("展開式：(a+b)² = a² + 2ab + b²")
        raw_a = st.text_input("輸入 a 的值：", key="pf1")
        raw_b = st.text_input("輸入 b 的值：", key="pf2")
        if st.button("執行公式展開"):
            try:
                a_f = Fraction(raw_a)
                b_f = Fraction(raw_b)
                ans = a_f**2 + 2*a_f*b_f + b_f**2
                st.success(f"🎉 展開結果: {ans}")
            except ValueError:
                st.error("❌ 錯誤：請輸入整數、小數或分數。")

    elif sub_menu == "勾股定理（畢氏定理）":
        st.subheader(" Pythagoras Calculator")
        choice = st.selectbox("你要計算什麼？", ["求斜邊 (Hypotenuse)", "求直角邊 (Leg)"])
        if choice == "求斜邊 (Hypotenuse)":
            raw_a = st.text_input("輸入直角邊 A 的長度：")
            raw_b = st.text_input("輸入直角邊 B 的長度：")
            if st.button("計算斜邊"):
                try:
                    a, b = Fraction(raw_a), Fraction(raw_b)
                    ans = (a**2 + b**2)**0.5
                    st.success(f"🎉 斜邊長度為：{ans}")
                except ValueError:
                    st.error("❌ 輸入無效！")
        else:
            raw_a = st.text_input("輸入已知的直角邊長度：")
            raw_c = st.text_input("輸入斜邊長度：")
            if st.button("計算直角邊"):
                try:
                    a, c = Fraction(raw_a), Fraction(raw_c)
                    if a >= c:
                        st.warning("⚠️ 錯誤：直角邊長度不能大於或等於斜邊！")
                    else:
                        ans = (c**2 - a**2)**0.5
                        st.success(f"🎉 另一條直角邊長度為：{ans}")
                except ValueError:
                    st.error("❌ 輸入無效！")

# ==========================================
# 6. 數學參考表格
# ==========================================
elif menu_choice == "6. 數學參考表格 (Reference Lists)":
    st.subheader("📚 系統內置數學數據庫")
    ref_table = st.selectbox("選擇要查看 interim 的表格：", ["九九乘法表", "1000以內的質數表", "平方數表 (1-31)", "立方數表 (1-10)", "常見勾股數"])
    
    if ref_table == "九九乘法表":
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
    elif ref_table == "1000以內的質數表":
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
    elif ref_table == "平方數表 (1-31)":
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
    elif ref_table == "立方數表 (1-10)":
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
    elif ref_table == "常見勾股數":
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
# 7. 周長公式
# ==========================================
elif menu_choice == "7. 周長公式 (Perimeter Formulas)":
    st.subheader("📐 Perimeter Calculation Mode")
    shape = st.selectbox("選擇幾何圖形：", ["長方形", "三角形", "圓形周長(圓周長)", "四邊形"])
    
    if shape == "長方形":
        c = st.text_input("輸入長方形寬度：", key="rec1")
        d = st.text_input("輸入長方形長度：", key="rec2")
        if st.button("計算長方形周長"):
            st.success(f"Perimeter: {(Fraction(c)+Fraction(d))*2}")
            
    elif shape == "三角形":
        d = st.text_input("邊長 1：", key="tri1")
        b_side = st.text_input("邊長 2：", key="tri2")
        c = st.text_input("邊長 3：", key="tri3")
        if st.button("計算三角形周長"):
            try:
                d_f, b_f, c_f = Fraction(d), Fraction(b_side), Fraction(c)
                if d_f >= (b_f+c_f) or b_f >= (c_f+d_f) or c_f >= (d_f+b_f):
                    st.error("❌ 兩邊之和大於第三邊，這不是合法的三角形！")
                else:
                    st.success(f"Triangle Perimeter: {d_f + b_f + c_f}")
            except ValueError: st.error("輸入錯誤")
            
    elif shape == "圓形周長(圓周長)":
        pi_mode = st.radio("選擇 π 的精度：", ["低精度 (π = 3)", "標準模式 (π = 3.14)", "高精度 (π = 3.1415926)"])
        r = st.text_input("輸入圓的半徑：")
        if st.button("計算圓周長"):
            r_val = float(r)
            pi_val = 3.0 if "低精度" in pi_mode else (3.14 if "標準" in pi_mode else 3.1415926)
            st.success(f"Circumference: {pi_val * r_val * 2}")
            
    elif shape == "四邊形":
        g1 = st.text_input("邊長 1：", key
