import streamlit as st
from fractions import Fraction
import time
import random
import math

# 配置網頁標題與圖標（必須是 Streamlit 的第一個指令）
st.set_page_config(page_title="THE MATRIX: CORE V8", page_icon="⚡", layout="wide")

# ==========================================
# 🌊 黑客帝國動態代碼雨亂碼流底層注入 (不影響文字清晰度)
# ==========================================
st.markdown("""
    <canvas id="matrix-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
    <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    // 讓畫布填滿螢幕
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // 亂碼字符集
    const katakana = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ";
    const alphabet = katakana.split("");

    const fontSize = 16;
    let columns = canvas.width / fontSize;

    const rainDrops = [];
    for (let x = 0; x < columns; x++) {
        rainDrops[x] = 1;
    }

    function draw() {
        // 微弱的黑色覆蓋，製造拖尾半透明效果
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#0F0'; // 經典黑客綠
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < rainDrops.length; i++) {
            const text = alphabet[Math.floor(Math.random() * alphabet.length)];
            ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);

            if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                rainDrops[i] = 0;
            }
            rainDrops[i]++;
        }
    }
    setInterval(draw, 30);
    </script>
    
    <style>
    /* 全局主體樣式：透明背景，以便看見底層的代碼雨 */
    .stApp {
        background: transparent;
    }
    
    /* 核心主面板：加上微黑半透明遮罩，確保文字 100% 清晰 */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.85); 
        padding: 40px !important;
        border-radius: 15px;
        border: 1px solid #00FF00;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
        margin-top: 20px;
    }
    
    /* 側邊欄半透明優化 */
    section[data-testid="stSidebar"] {
        background-color: rgba(5, 5, 5, 0.9) !important;
        border-right: 1px solid #00FF00;
    }
    
    /* 螢光綠霓虹文字效果 */
    h1, h2, h3, h4, h5, h6 { 
        color: #00FF00 !important; 
        text-shadow: 0 0 8px rgba(0, 255, 0, 0.6);
        font-family: 'Courier New', monospace;
    }
    
    /* 網頁按鈕樣式 */
    div.stButton > button:first-child {
        background-color: #000000; 
        color: #00FF00; 
        border: 2px solid #00FF00;
        box-shadow: 0 0 10px #00FF00; 
        font-family: 'Courier New', monospace; 
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover { 
        background-color: #00FF00; 
        color: #000000; 
        box-shadow: 0 0 20px #00FF00;
    }
    
    /* 輸入框黑客化 */
    .stTextInput>div>div>input {
        background-color: #111111 !important; 
        color: #00FF00 !important; 
        border: 1px solid #00FF00 !important;
        font-family: 'Courier New', monospace;
    }
    
    /* 普通文本與標籤顏色 */
    div[data-testid="stMarkdownContainer"] p { 
        color: #00FF00 !important; 
        font-family: 'Courier New', monospace;
    }
    label[data-testid="stWidgetLabel"] p {
        color: #00FF00 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ THE MATRIX: LOGIC SOURCE CORE V8")
st.write("歡迎來到終極代碼矩陣。系統已整合動態代碼雨底層，文字清晰度過載防護已開啟。")

# ==========================================
# 🎛️ 側邊欄主菜單控制中心
# ==========================================
st.sidebar.title("🎛️ 系統控制面板")
menu_choice = st.sidebar.selectbox(
    "請選擇模組功能：",
    [
        "系統初始化首頁",
        "1. 加法模式 (Addition)",
        "2. 減法模式 (Subtraction)",
        "3. 乘法模式 (Multiplication)",
        "4. 除法模式 (Division)",
        "5. 進階公式選擇 (Advanced Formulas)",
        "6. 多功能數據圖表 (Data Charts)",
        "7. 周長公式模組 (Perimeter)",
        "8. [十六進制 ASCII 密碼加密]",
        "9. [十六進制 ASCII 密碼解密]"
    ]
)

# ==========================================
# 0. 系統初始化首頁
# ==========================================
if menu_choice == "系統初始化首頁":
    st.subheader("📟 系統狀態：準備就緒")
    st.write("這是一款為網頁端優化的高精度代數與幾何計算核心。請從左側菜單切換功能。")
    if st.button("🧬 運行核心數據庫加載檢查"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        progresses = [0, 13, 31, 36, 43, 44, 58, 85, 97, 100]
        for p in progresses:
            status_text.text(f"正在加載核心數據庫... {p}%")
            progress_bar.progress(p / 100)
            time.sleep(random.uniform(0.05, 0.15))
        st.success("🟢 系統數據加載成功！Ultimate Math Engine 已準備就緒。")

# ==========================================
# 1. 加法模式
# ==========================================
elif menu_choice == "1. 加法模式 (Addition)":
    st.subheader("➕ [加法模式]")
    raw_one = st.text_input("輸入第一個加數（支持分數/整數/小數）：", key="plus1")
    raw_two = st.text_input("輸入第二個加數（支持分數/整數/小數）：", key="plus2")
    if st.button("執行加法計算"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"計算結果: {one} + {two} = {one + two}")
        except ValueError: st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 2. 減法模式
# ==========================================
elif menu_choice == "2. 減法模式 (Subtraction)":
    st.subheader("➖ [減法模式]")
    raw_one = st.text_input("輸入被減數：", key="minus1")
    raw_two = st.text_input("輸入減數：", key="minus2")
    if st.button("執行減法計算"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"計算結果: {one} - {two} = {one - two}")
        except ValueError: st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 3. 乘法模式
# ==========================================
elif menu_choice == "3. 乘法模式 (Multiplication)":
    st.subheader("✖️ [乘法模式]")
    raw_one = st.text_input("輸入第一個因數：", key="mul1")
    raw_two = st.text_input("輸入第二個因數：", key="mul2")
    if st.button("執行乘法計算"):
        try:
            one = Fraction(raw_one)
            two = Fraction(raw_two)
            st.code(f"計算結果: {one} × {two} = {one * two}")
        except ValueError: st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 4. 除法模式
# ==========================================
elif menu_choice == "4. 除法模式 (Division)":
    st.subheader("➗ [除法模式]")
    raw_one = st.text_input("輸入被除數：", key="div1")
    raw_two = st.text_input("輸入除數：", key="div2")
    if st.button("執行除值計算"):
        if raw_two == "0": st.warning("⚠️ 錯誤：除數不能為零！")
        else:
            try:
                one = Fraction(raw_one)
                two = Fraction(raw_two)
                st.code(f"計算結果: {one} ÷ {two} = {one / two}")
            except ValueError: st.error("❌ 錯誤：請輸入有效的數字或分數！")

# ==========================================
# 5. 進階公式選擇（一元二次、完全平方、勾股、面積、體積）
# ==========================================
elif menu_choice == "5. 進階公式選擇 (Advanced Formulas)":
    st.subheader("📐 進階公式選單引擎")
    sub_menu = st.radio("請選擇子公式核心：", ["一元二次方程求根", "完全平方公式展開", "勾股定理未知邊", "面積公式核心 (mianji)", "體積公式核心 (tiji)"])
    
    if sub_menu == "一元二次方程求根":
        st.write("--- 一元二次方程求根 (ax² + bx + c = 0) ---")
        raw_a = st.text_input("輸入係數 a:")
        raw_b = st.text_input("輸入係數 b:")
        raw_c = st.text_input("輸入係數 c:")
        if st.button("求解方程"):
            try:
                input_one, input_two, input_three = float(raw_a), float(raw_b), float(raw_c)
                if input_one == 0: st.error("❌ 錯誤：係數 'a' 不能為 0。")
                else:
                    discriminant = input_two ** 2 - 4 * input_one * input_three
                    if discriminant < 0: st.error("❌ 錯誤：該方程無實數根。")
                    else:
                        ans1 = (-input_two + (discriminant ** 0.5)) / (2 * input_one)
                        ans2 = (-input_two - (discriminant ** 0.5)) / (2 * input_one)
                        st.success(f"🎉 方程根為：{ans1} 或 {ans2}")
            except ValueError: st.error("❌ 錯誤：請輸入有效的數字。")

    elif sub_menu == "完全平方公式展開":
        st.write("--- 完全平方公式展開 (a²+2ab+b²) ---")
        raw_a = st.text_input("輸入表達式 'a':", key="wan1")
        raw_b = st.text_input("輸入表達式 'b':", key="wan2")
        if st.button("執行展開"):
            try:
                ans = Fraction(raw_a)**2 + 2*Fraction(raw_a)*Fraction(raw_b) + Fraction(raw_b)**2
                st.success(f"🎉 展開後的結果為: {str(ans)}")
            except ValueError: st.error("❌ 錯誤：請輸入整數或小數。")

    elif sub_menu == "勾股定理未知邊":
        st.write("--- 勾股定理求解器 ---")
        choice = st.selectbox("你想求解什麼？", ["求斜邊 (已知兩直角邊 A 和 B)", "求直角邊 (已知直角邊 A 和斜邊 C)"])
        if choice == "求斜邊 (已知兩直角邊 A 和 B)":
            raw_a = st.text_input("輸入直角邊 A 長度:")
            raw_b = st.text_input("輸入直角邊 B 長度:")
            if st.button("計算斜邊"):
                try: st.success(f"🎉 斜邊長度為: {(Fraction(raw_a)**2 + Fraction(raw_b)**2)**0.5}")
                except ValueError: st.error("❌ 錯誤：輸入無效！")
        else:
            raw_a = st.text_input("輸入已知直角邊長度:")
            raw_c = st.text_input("輸入斜邊長度:")
            if st.button("計算直角邊"):
                try:
                    a_f, c_f = Fraction(raw_a), Fraction(raw_c)
                    if a_f >= c_f: st.warning("⚠️ 錯誤：直角邊不能大於或等於斜邊！")
                    else: st.success(f"🎉 另一條直角邊長度為: {(c_f**2 - a_f**2)**0.5}")
                except ValueError: st.error("❌ 錯誤：輸入無效！")

    elif sub_menu == "面積公式核心 (mianji)":
        st.write("--- [面積計算模式] ---")
        shape = st.selectbox("選擇圖形面積公式：", ["長方形 / 正方形 面積", "三角形 面積", "圓形 面積"])
        if shape == "長方形 / 正方形 面積":
            c = st.text_input("輸入長度：", key="area_rect1")
            d = st.text_input("輸入寬度：", key="area_rect2")
            if st.button("計算四邊形面積"):
                try:
                    c_f, d_f = Fraction(c), Fraction(d)
                    name = "正方形" if c_f == d_f else "長方形"
                    st.success(f"🎉 {name}的面積為: {c_f * d_f}")
                except ValueError: st.error("❌ 請輸入有效數字。")
        elif shape == "三角形 面積":
            base = st.text_input("輸入底邊長度：", key="area_tri1")
            height = st.text_input("輸入高：", key="area_tri2")
            if st.button("計算三角形面積"):
                try: st.success(f"🎉 三角形的面積為: {Fraction(1, 2) * Fraction(base) * Fraction(height)}")
                except ValueError: st.error("❌ 請輸入有效數字。")
        elif shape == "圓形 面積":
            r = st.text_input("輸入圓的半徑：", key="area_circle")
            if st.button("計算圓形面積"):
                try: st.success(f"🎉 圓形的面積大約為: {Fraction(r)**2 * 3.1415926}")
                except ValueError: st.error("❌ 請輸入有效數字。")

    elif sub_menu == "體積公式核心 (tiji)":
        st.write("--- [體積計算模式] ---")
        v_shape = st.selectbox("選擇立體圖形體積公式：", ["正方體 / 長方體 體積", "圓柱體 體積", "圓錐體 體積"])
        if v_shape == "正方體 / 長方體 體積":
            l = st.text_input("輸入長：", key="vol_cube1")
            w = st.text_input("輸入寬：", key="vol_cube2")
            h = st.text_input("輸入高：", key="vol_cube3")
            if st.button("計算柱體體積"):
                try: st.success(f"🎉 該立體體積為: {Fraction(l)*Fraction(w)*Fraction(h)}")
                except ValueError: st.error("❌ 請輸入有效數字。")
        elif v_shape == "圓柱體 體積":
            r = st.text_input("輸入底面半徑：", key="vol_cyl1")
            h = st.text_input("輸入高：", key="vol_cyl2")
            if st.button("計算圓柱體體積"):
                try: st.success(f"🎉 圓柱體體積大約為: {math.pi * (float(r)**2) * float(h):.6f}")
                except ValueError: st.error("❌ 請輸入有效數字。")
        elif v_shape == "圓錐體 體積":
            r = st.text_input("輸入底面半徑：", key="vol_cone1")
            h = st.text_input("輸入高：", key="vol_cone2")
            if st.button("計算圓錐體體積"):
                try: st.success(f"🎉 圓錐體體積大約為: {(1 / 3) * math.pi * (float(r)**2) * float(h):.6f}")
                except ValueError: st.error("❌ 請輸入有效數字。")

# ==========================================
# 6. 多功能數據圖表
# ==========================================
elif menu_choice == "6. 多功能數據圖表 (Data Charts)":
    st.subheader("📚 系統內部數據參考圖表")
    ref_table = st.selectbox("選擇查閱的圖表單元：", ["九九乘法表", "1000以內質數表", "平方數對照表", "立方數對照庫", "常見勾股數組"])
    if ref_table == "九九乘法表":
        st.code("1x1=1\n1x2=2 2x2=4\n1x3=3 2x3=6 3x3=9\n1x4=4 2x4=8 3x4=12 4x4=16\n1x5=5 2x5=10 3x5=15 4x5=20 5x5=25\n1x6=6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36\n1x7=7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49\n1x8=8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64\n1x9=9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81")
    elif ref_table == "1000以內質數表":
        st.code("2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71...\n[篇幅限制，已為網頁壓縮顯示，核心數據在庫]")
    elif ref_table == "平方數對照表":
        st.code("1^2=1, 2^2=4, 3^2=9 ... 31^2=961")
    elif ref_table == "立方數對照庫":
        st.code("1³=1, 2³=8, 3³=27 ... 10³=1000")
    elif ref_table == "常見勾股數組":
        st.code("3-4-5, 5-12-13, 8-15-17, 7-24-25, 9-40-41")

# ==========================================
# 7. 周長公式模組
# ==========================================
elif menu_choice == "7. 周長公式模組 (Perimeter)":
    st.subheader("📐 周長計算模式")
    shape = st.selectbox("選擇圖形周長單元：", ["長方形周長", "三角形周長", "圓形周長", "一般四邊形周長"])
    
    if shape == "長方形周長":
        c = st.text_input("輸入寬度：", key="peri_rec1")
        d = st.text_input("輸入長度：", key="peri_rec2")
        if st.button("計算長方形周長"):
            try: st.success(f"🎉 長方形周長為：{(Fraction(c)+Fraction(d))*2}")
            except ValueError: st.error("❌ 請輸入有效數字。")
    elif shape == "三角形周長":
        d = st.text_input("輸入邊長 1：", key="peri_tri1")
        b_side = st.text_input("輸入邊長 2：", key="peri_tri2")
        c = st.text_input("輸入邊長 3：", key="peri_tri3")
        if st.button("計算三角形周長"):
            try:
                d_f, b_f, c_f = Fraction(d), Fraction(b_side), Fraction(c)
                if d_f >= (b_f+c_f) or b_f >= (c_f+d_f) or c_f >= (d_f+b_f): st.error("❌ 錯誤：無法構成有效三角形！")
                else: st.success(f"🎉 三角形周長為：{d_f + b_f + c_f}")
            except ValueError: st.error("❌ 請輸入有效數字。")
    elif shape == "圓形周長":
        pi_mode = st.radio("選擇圓周率精確度：", ["低精確度 (π = 3)", "標準模式 (π = 3.14)", "高精確度 (π = 3.1415926)"])
        r = st.text_input("輸入圓的半徑：", key="peri_cir")
        if st.button("計算圓周長"):
            try:
                pi_val = 3.0 if "低" in pi_mode else (3.14 if "標準" in pi_mode else 3.1415926)
                st.success(f"🎉 圓形周長為：{2 * pi_val * float(r)}")
            except ValueError: st.error("❌ 請輸入有效數字。")
    elif shape == "一般四邊形周長":
        g1 = st.text_input("邊 1 (ganjinwanshi):", key="p_quad1")
        g2 = st.text_input("邊 2 (ganjinwanshizaiyibian):", key="p_quad2")
        g3 = st.text_input("邊 3 (ganjinwanshidisanbian):", key="p_quad3")
        g4 = st.text_input("邊 4 (zhongyuyaowanshilema):", key="p_quad4")
        if st.button("計算四邊形周長"):
            try: st.success(f"🎉 四邊形周長為：{Fraction(g1) + Fraction(g2) + Fraction(g3) + Fraction(g4)}")
            except ValueError: st.error("❌ 請輸入有效數字。")

# ==========================================
# 8. 十六進制 ASCII 密碼加密
# ==========================================
elif menu_choice == "8. [十六進制 ASCII 密碼加密]":
    st.subheader("🔐 十六進制凱撒矩陣加密系統")
    user_input = st.text_input("輸入要加密的明文字符串：", key="matrix_enc")
    if st.button("🔥 注入矩陣並加密"):
        if user_input:
            clean_output = " ".join([hex(ord(i) + 3)[2:] for i in user_input])
            st.info("加密完成！生成的密文數據流：")
            st.code(clean_output)
        else: st.warning("請先輸入明文字符串。")

# ==========================================
# 9. 十六進制 ASCII 密碼解密
# ==========================================
elif menu_choice == "9. [十六進制 ASCII 密碼解密]":
    st.subheader("🔓 十六進制凱撒矩陣解密系統")
    user_input = st.text_input("在此粘貼要破譯的密文數據流（空格隔開）：", key="matrix_dec")
    if st.button("🟢 執行解密破譯"):
        if user_input:
            try:
                clean_output = "".join([chr(int(i, 16) - 3) for i in user_input.split()])
                st.success("🎉 矩陣破譯成功！還原出的明文原始數據：")
                st.code(clean_output)
            except Exception: st.error("❌ 矩陣錯誤！請檢查輸入的十六進制密文格式是否正確。")
        else: st.warning("密文數據流不能為空。")

# ==========================================
# 📜 底欄系統標識
# ==========================================
st.markdown("---")
st.caption("© 2026 Harry 的賽博工作室 | 核心算法驅動：Streamlit Web Core")
