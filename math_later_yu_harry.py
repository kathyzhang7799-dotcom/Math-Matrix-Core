from fractions import Fraction
import time
import random
import streamlit as st

# --- 1. 网页全局配置 (进入母体控制台) ---
st.set_page_config(
    page_title="The Matrix - Harry's Core Terminal",
    page_icon="🟢",
    layout="wide"
)

# 注入纯正《黑客帝国》暗黑绿幕特效
st.markdown("""
    <style>
    /* 强制背景为纯黑，文字为数字雨荧光绿 */
    .stApp { background-color: #000000 !important; }
    .main { background-color: #000000 !important; color: #00FF00 !important; font-family: 'Courier New', monospace; }
    
    /* 标题与副标题黑客化 */
    h1, h2, h3, h4, h5, h6 { color: #00FF00 !important; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00FF00; }
    p, label, span, div { color: #00FF00 !important; font-family: 'Courier New', monospace; }
    
    /* 输入框样式重写：黑底绿字绿边框 */
    .stTextInput>div>div>input, .stSelectbox>div>div>div { background-color: #050505 !important; color: #00FF00 !important; border: 1px solid #00FF00 !important; font-family: 'Courier New', monospace; }
    
    /* 按钮样式：黑客帝国选择矩阵 */
    .stButton>button { width: 100%; background-color: #000000; color: #00FF00; border: 1px solid #00FF00; font-family: 'Courier New', monospace; box-shadow: 0 0 5px #00FF00; }
    .stButton>button:hover { background-color: #00FF00 !important; color: #000000 !important; font-weight: bold; box-shadow: 0 0 15px #00FF00; }
    
    /* 侧边栏修改 */
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid #00FF00; }
    
    /* 代码块与警告框 */
    code { color: #00FF00 !important; background-color: #111111 !important; border: 1px solid #00FF00; }
    .stAlert { background-color: #0A140A !important; border: 1px solid #00FF00 !important; color: #00FF00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 模拟母体数据流加载 (Digital Rain Loading) ---
if 'matrix_loaded' not in st.session_state:
    st.title("📟 CONNECTING TO THE MATRIX...")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # 模拟黑客解密进度
    progresses = [0, 9, 21, 45, 66, 73, 88, 95, 100]
    for p in progresses:
        progress_bar.progress(p)
        status_text.text(f"📥 Downloading Node Data... [Saskatchewan System] {p}%")
        time.sleep(random.uniform(0.06, 0.18))
    
    st.session_state['matrix_loaded'] = True
    st.success("🔓 OVERRIDE SUCCESSFUL. SOURCE CODE INJECTED.")
    time.sleep(0.6)
    st.rerun()

# --- 3. 主界面核心（黑客帝国风格标题） ---
st.title("🟢 THE MATRIX: LOGIC SOURCE CORE V7")
st.caption("▲ SYSTEM USER: HARRY | NODE: MOOSE JAW, SK | STATUS: STANDBY")
st.write("====================================================================================================")

# --- 4. 侧边栏：选择你的药丸 (功能菜单) ---
with st.sidebar:
    st.subheader("💊 SELECT YOUR PILL")
    menu_choice = st.radio(
        "选择要解码的母体协议:",
        [
            "⚡ [ALGORITHM] 基础四则运算",
            "🧬 [EQUATION] 高级代数公式",
            "📐 [GEOMETRY] 几何周长公式",
            "📊 [DATABASE] 数学参考表",
            "🔒 [CRYPT] 十六进制凯撒加密",
            "🔓 [DECRYPT] 十六进制凯撒解密"
        ]
    )
    st.write("====================")
    st.markdown("**[SYSTEM NOTICE]**")
    st.caption("You take the blue pill, the story ends. You take the red pill, you stay in Wonderland.")

# 辅助函数：保持高精度的分数输出
def to_fraction_str(val):
    if val.is_integer():
        return str(int(val))
    frac = Fraction(val).limit_denominator(1000)
    if abs(float(frac) - val) > 1e-9:
        return f"{val:.4f}"
    return str(frac)


# ==================== 模块 1：基础四则运算 ====================
if "基础四则运算" in menu_choice:
    st.subheader("🧮 [NODE] FRACTION CALCULATION CORE")
    op = st.selectbox("选择运算协议 (Protocol):", ["加法 (+)", "减法 (-)", "乘法 (×)", "除法 (÷)"])
    
    col1, col2 = st.columns(2)
    with col1:
        raw_one = st.text_input("Input Matrix Alpha (e.g., 3, 0.5, 1/3):", key="op1")
    with col2:
        raw_two = st.text_input("Input Matrix Beta:", key="op2")
        
    if st.button("RUN ALGORITHM"):
        if raw_one and raw_two:
            try:
                one = Fraction(raw_one)
                two = Fraction(raw_two)
                if "加法" in op:
                    st.success(f"OUTPUT: {one} + {two} = {one + two}")
                elif "减法" in op:
                    st.success(f"OUTPUT: {one} - {two} = {one - two}")
                elif "乘法" in op:
                    st.success(f"OUTPUT: {one} × {two} = {one * two}")
                elif "除法" in op:
                    if two == 0:
                        st.error("SYSTEM ERROR: Division by zero is restricted.")
                    else:
                        st.success(f"OUTPUT: {one} ÷ {two} = {one / two}")
            except ValueError:
                st.error("SYNTAX ERROR: Invalid numeric or fraction format.")


# ==================== 模块 2：高级代数公式 ====================
elif "高级代数公式" in menu_choice:
    st.subheader("🧬 [NODE] ADVANCED FORMULA ENGINE")
    sub_menu = st.selectbox("选择解析协议:", ["一元二次方程求解器", "完全平方公式展开", "勾股定理计算器"])
    
    if sub_menu == "一元二次方程求解器":
        st.write("▶ Formula: ax² + bx + c = 0")
        c1, c2, c3 = st.columns(3)
        with c1: raw_a = st.text_input("Coefficient a:", key="qa")
        with c2: raw_b = st.text_input("Coefficient b:", key="qb")
        with c3: raw_c = st.text_input("Coefficient c:", key="qc")
        
        if st.button("SOLVE EQUATION"):
            if raw_a and raw_b and raw_c:
                try:
                    a, b, c = float(raw_a), float(raw_b), float(raw_c)
                    if a == 0:
                        st.error("CRITICAL ERROR: 'a' cannot be zero.")
                    else:
                        discriminant = b**2 - 4*a*c
                        if discriminant < 0:
                            st.warning("NOTICE: Real roots do not exist in this matrix sector.")
                        else:
                            ans1 = (-b + (discriminant ** 0.5)) / (2 * a)
                            ans2 = (-b - (discriminant ** 0.5)) / (2 * a)
                            st.success(f"🎉 ROOT RESOLVED: x1 = {to_fraction_str(ans1)} | x2 = {to_fraction_str(ans2)}")
                except ValueError:
                    st.error("SYNTAX ERROR: Inputs must be numerical.")
                    
    elif sub_menu == "完全平方公式展开":
        st.write("▶ Formula: (a + b)² = a² + 2ab + b²")
        c1, col2 = st.columns(2)
        with c1: raw_a = st.text_input("Variable a:", key="paa")
        with col2: raw_b = st.text_input("Variable b:", key="pbb")
        if st.button("EXPAND MATRICES"):
            if raw_a and raw_b:
                try:
                    fa, fb = Fraction(raw_a), Fraction(raw_b)
                    ans = fa**2 + 2*fa*fb + fb**2
                    st.success(f"🎉 EXPANDED RESULT: {ans}")
                except ValueError:
                    st.error("SYNTAX ERROR.")
                    
    elif sub_menu == "勾股定理计算器":
        st.write("▶ Formula: a² + b² = c²")
        mode = st.radio("Target Sector:", ["斜边 (Hypotenuse)", "直角边 (Leg)"])
        if mode == "斜边 (Hypotenuse)":
            c1, col2 = st.columns(2)
            with c1: la = st.text_input("Leg A:", key="la")
            with col2: lb = st.text_input("Leg B:", key="lb")
            if st.button("CALCULATE HYPOTENUSE"):
                try: st.success(f"🎉 RESULT: {(Fraction(la)**2 + Fraction(lb)**2)**0.5}")
                except: st.error("ERROR.")
        else:
            c1, col2 = st.columns(2)
            with c1: la = st.text_input("Known Leg:", key="l_known")
            with col2: lc = st.text_input("Hypotenuse:", key="l_hyp")
            if st.button("CALCULATE LEG"):
                try:
                    a, c = Fraction(la), Fraction(lc)
                    if a >= c: st.error("VIOLATION: Leg cannot exceed Hypotenuse.")
                    else: st.success(f"🎉 RESULT: {(c**2 - a**2)**0.5}")
                except: st.error("ERROR.")


# ==================== 模块 3：几何周长公式 ====================
elif "几何周长公式" in menu_choice:
    st.subheader("📐 [NODE] PERIMETER CALCULATOR")
    shape = st.selectbox("Select Shape:", ["长方形", "三角形", "圆形", "普通四边形"])
    
    if shape == "长方形":
        c1, col2 = st.columns(2)
        with c1: w = st.text_input("Width:")
        with col2: l = st.text_input("Length:")
        if st.button("EXECUTE"):
            try: st.success(f"PERIMETER: {(Fraction(w) + Fraction(l)) * 2}")
            except: st.error("ERROR.")
            
    elif shape == "三角形":
        c1, col2, c3 = st.columns(3)
        with c1: s1 = st.text_input("Side 1:")
        with col2: s2 = st.text_input("Side 2:")
        with c3: s3 = st.text_input("Side 3:")
        if st.button("EXECUTE"):
            try:
                d, b_side, c = Fraction(s1), Fraction(s2), Fraction(s3)
                if d >= (b_side+c) or b_side >= (c+d) or c >= (d+b_side):
                    st.error("VIOLATION: Invalid Triangle Dimensions.")
                else: st.success(f"PERIMETER: {d + b_side + c}")
            except: st.error("ERROR.")
            
    elif shape == "圆形":
        pi_mode = st.selectbox("Select π Precision:", ["Low (π = 3)", "Standard (π = 3.14)", "High (π = 3.1415926)"])
        r = st.text_input("Radius:")
        if st.button("EXECUTE"):
            try:
                r_f = float(r)
                pi = 3 if "Low" in pi_mode else (3.14 if "Standard" in pi_mode else 3.1415926)
                st.success(f"CIRCUMFERENCE: {pi * r_f * 2}")
            except: st.error("ERROR.")
            
    elif shape == "普通四边形":
        c1, col2, c3, c4 = st.columns(4)
        with c1: g1 = st.text_input("S1:")
        with col2: g2 = st.text_input("S2:")
        with c3: g3 = st.text_input("S3:")
        with col4: g4 = st.text_input("S4:")
        if st.button("EXECUTE"):
            try: st.success(f"PERIMETER: {Fraction(g1)+Fraction(g2)+Fraction(g3)+Fraction(g4)}")
            except: st.error("ERROR.")


# ==================== 模块 4：数学参考表 ====================
elif "数学参考表" in menu_choice:
    st.subheader("📊 [DATABASE] ENCRYPTED MATRIX CONSTANTS")
    table_type = st.radio("Select Sector:", ["九九乘法表", "1000以内质数表", "平方数表", "立方数表", "常用勾股数"])
    
    if table_type == "九九乘法表":
        st.code("1x1=1\n1x2=2 2x2=4\n... [THE MATRIX MULTIPLICATION TABLE LOADED]")
    elif table_type == "1000以内质数表":
        st.code("2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53...")
    elif table_type == "平方数表":
        st.code("1^2=1, 2^2=4, ..., 31^2=961")
    elif table_type == "立方数表":
        st.code("01³ = 1, 02³ = 8, ..., 10³ = 1000")
    elif table_type == "常用勾股数":
        st.code("3—4—5 | 5—12—13 | 8—15—17 | 7—24—25 | 9—40—41")


# ==================== 模块 5：十六进制凯撒加密 ====================
elif "十六进制凯撒加密" in menu_choice:
    st.subheader("🔒 [ENCRYPT] HEXADECIMAL CAESAR INJECTION")
    user_input = st.text_input("Enter plain text to mask (Will be encrypted into hex stream):", type="password")
    if st.button("INJECT CODES"):
        if user_input:
            list_one = []
            for i in user_input:
                list_one.append(hex(ord(i) + 3)[2:])
            clean_output = " ".join(list_one)
            st.success("🔒 CIPHER STREAM GENERATED SUCCESSFUL:")
            st.code(clean_output, language="text")
        else:
            st.warning("Empty data stream detected.")


# ==================== 模块 6：十六进制凯撒解密 ====================
elif "十六进制解密" in menu_choice:
    st.subheader("🔓 [DECRYPT] HEXADECIMAL CODES BREAK SYSTEM")
    user_input = st.text_input("Enter hex cipher stream (space-separated):")
    if st.button("BREAK MATRIX CIPHER"):
        if user_input:
            try:
                new_list = user_input.split()
                new_list_ = []
                for i in new_list:
                    new_list_.append(chr(int(i, 16) - 3))
                clean_output = "".join(new_list_)
                st.success("🔓 DECRYPTION COMPLETE. PLAIN TEXT RESTORED:")
                st.code(clean_output, language="text")
            except:
                st.error("DECRYPTION FAILURE: Malformed hexadecimal stream format.")

# --- 5. 网页页脚 (终极谢幕) ---
st.write("====================================================================================================")
st.caption("WARNING: Unauthorized access to this terminal will trigger agent alert protocols.")
st.caption("© 2026 Harry's Cyber Workshop | System Ver: Matrix-V7.0-Stable")
