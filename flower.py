import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def draw_flower(ax, x, y, radius=1.0, petals=6, wobble=0.1, color='pink'):
    """Draw a single flower with petals"""
    for i in range(petals):
        angle = i * 2 * np.pi / petals
        petal_x = x + radius * np.cos(angle) + np.random.uniform(-wobble, wobble)
        petal_y = y + radius * np.sin(angle) + np.random.uniform(-wobble, wobble)
        ax.plot([x, petal_x], [y, petal_y], color=color, linewidth=6, alpha=0.7)
        circle = plt.Circle((petal_x, petal_y), radius/2, color=color, alpha=0.6)
        ax.add_patch(circle)
    ax.plot(x, y, 'o', color='yellow', markersize=radius*10)

def draw_poster(text='Hello', text_x=0, text_y=0, text_size=40, text_color='black', 
                num_flowers=8, seed=42):
    """Create a flower poster with customizable text"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    # Draw flowers
    for _ in range(num_flowers):
        x, y = np.random.uniform(-8, 8, 2)
        radius = np.random.uniform(1.0, 2.0)
        petals = np.random.randint(5, 10)
        wobble = np.random.uniform(0.1, 0.5)
        color = np.random.choice(['pink', 'red', 'purple', 'orange'])
        draw_flower(ax, x, y, radius, petals, wobble, color)
    
    # Draw text
    ax.text(text_x, text_y, text, fontsize=text_size, color=text_color,
            ha='center', va='center', weight='bold')
    
    return fig

# Streamlit App Configuration
st.set_page_config(page_title="Flower Poster Generator", page_icon="🌸", layout="wide")

st.title("🌸 꽃 포스터 생성기")
st.markdown("아름다운 꽃들과 함께 나만의 포스터를 만들어보세요!")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ 설정")
    
    # Text settings
    st.markdown("#### 📝 텍스트 설정")
    text_input = st.text_input("텍스트", value="Hello", help="포스터에 표시할 텍스트")
    text_x = st.slider("텍스트 X 위치", min_value=-8.0, max_value=8.0, value=0.0, step=0.1)
    text_y = st.slider("텍스트 Y 위치", min_value=-8.0, max_value=8.0, value=0.0, step=0.1)
    text_size = st.slider("텍스트 크기", min_value=10, max_value=100, value=40, step=1)
    text_color = st.color_picker("텍스트 색상", value="#000000")
    
    st.markdown("---")
    
    # Flower settings
    st.markdown("#### 🌺 꽃 설정")
    num_flowers = st.slider("꽃 개수", min_value=3, max_value=20, value=8, step=1)
    seed = st.number_input("시드 값", min_value=0, value=42, step=1, 
                          help="같은 시드 값 = 같은 패턴")
    
    st.markdown("---")
    
    # Generate button
    if st.button("🎲 새로운 꽃 패턴 생성", use_container_width=True):
        seed = np.random.randint(0, 10000)
        st.rerun()

with col2:
    st.subheader("🖼️ 포스터 미리보기")
    
    # Generate and display poster
    with st.spinner("포스터를 생성하는 중..."):
        fig = draw_poster(
            text=text_input,
            text_x=text_x,
            text_y=text_y,
            text_size=text_size,
            text_color=text_color,
            num_flowers=num_flowers,
            seed=seed
        )
        st.pyplot(fig)
        plt.close(fig)

# Footer with instructions
st.markdown("---")
st.markdown("""
### 💡 사용 팁
- **텍스트 위치**: 슬라이더를 조정하여 텍스트를 원하는 위치로 이동하세요
- **색상 선택**: 색상 피커를 클릭하여 다양한 색상을 시도해보세요
- **시드 값**: 마음에 드는 패턴의 시드 값을 기록해두면 나중에 다시 만들 수 있습니다
- **새 패턴**: "새로운 꽃 패턴 생성" 버튼으로 완전히 새로운 디자인을 만들어보세요
""")

# Sidebar info
st.sidebar.header("ℹ️ 정보")
st.sidebar.info(
    "이 앱은 랜덤하게 생성된 꽃들로 "
    "아름다운 포스터를 만들어줍니다. "
    "왼쪽의 설정을 조정하여 나만의 디자인을 만들어보세요!"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**현재 설정:**")
st.sidebar.text(f"텍스트: {text_input}")
st.sidebar.text(f"꽃 개수: {num_flowers}")
st.sidebar.text(f"시드: {seed}")
