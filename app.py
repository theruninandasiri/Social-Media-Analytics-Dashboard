import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Social Media Analytics Dashboard",
    page_icon="📶",
    layout="wide",
    initial_sidebar_state="expanded"
)

#CUSTOM CSS FOR INTERFACE - PLEASANT COLOR GRADIENT BACKGROUND
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Pleasant Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #1a1a2e);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main content area background - clean white with blur */
    .main > div {
        background: rgba(255, 255, 255, 0.94);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
    }
    
    /* Header styling with glass effect */
    .main-header {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        letter-spacing: -0.5px;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.95);
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
        font-weight: 600;
    }
    
    /* Metric card styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 0.8rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
        margin: 0.3rem;
        min-height: 100px;
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        background: white;
    }
    
    .metric-number {
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.2rem 0;
        padding: 0;
        line-height: 1.2;
    }
    
    .metric-label {
        font-size: 0.75rem;
        color: #555;
        font-weight: 500;
        letter-spacing: 0.3px;
        margin: 0;
        padding: 0;
        line-height: 1.3;
    }
    
    /* Sidebar styling - Glass effect */
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255,255,255,0.15);
    }
    
    .sidebar .sidebar-content {
        background: transparent;
    }
    
    /* Sidebar text color */
    .sidebar .sidebar-content h1,
    .sidebar .sidebar-content h2,
    .sidebar .sidebar-content h3,
    .sidebar .sidebar-content p,
    .sidebar .sidebar-content label {
        color: white !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.3rem !important;
        background: rgba(255,255,255,0.9);
        padding: 0.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        flex-wrap: wrap !important;
        justify-content: center !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.3rem 0.7rem !important;
        font-weight: 700 !important;
        font-size: 0.8rem !important;
        transition: all 0.3s;
        color: black !important;
        white-space: nowrap !important;
        display: inline-block !important;
        width: auto !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #667eea20, #764ba220);
        transform: translateY(-1px);
        color: black !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Make all subheaders WHITE BOLD */
    .stSubheader {
        color: white !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 5px 12px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 0.8rem;
        line-height: 1.3;
    }
    
    /* Target all h2 elements */
    h2, .css-1y4p8pa h2, .stMarkdown h2 {
        color: white !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 5px 12px;
        border-radius: 8px;
        display: inline-block;
        font-size: 1rem !important;
        line-height: 1.3;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.4rem 0.8rem;
        font-weight: 600;
        transition: all 0.3s;
        width: 100%;
        font-size: 0.8rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102,126,234,0.4);
    }
    
    /* Info/Warning/Success boxes */
    .stAlert {
        border-radius: 12px;
        font-weight: 500;
        font-size: 0.8rem;
        padding: 0.5rem;
        background: rgba(255,255,255,0.95);
    }
    
    /* Make Info/Warning/Success text BLACK */
    .stAlert .stMarkdown, 
    .stAlert .stMarkdown p,
    .element-container .stAlert p {
        color: black !important;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        font-size: 0.8rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(245,247,250,0.95);
        border-radius: 8px;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        color: #2c3e50 !important;
        padding: 0.4rem;
    }
    
    .streamlit-expanderHeader span {
        font-weight: 700 !important;
        font-size: 0.85rem !important;
    }
    
    /* Custom white info text */
    .white-info-text {
        color: white !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        padding: 8px !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        text-align: center !important;
        margin: 8px 0;
        font-size: 0.8rem;
    }
    
    /* Key Performance Indicators */
    .kpi-header {
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 5px 15px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 0.8rem;
        line-height: 1.3;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        margin-top: 1.5rem;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        color: white;
        font-size: 0.75rem;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: white;
        border-radius: 8px;
        font-size: 0.8rem;
    }
    
    /* ===== FIXED FILE UPLOADER ===== */
    div[data-testid="stFileUploader"] > div:first-child {
        background: rgba(255,255,255,0.95);
        border-radius: 12px;
        border: 2px dashed #667eea;
        padding: 12px !important;
        text-align: center;
    }
    
    div[data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 6px 16px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        display: inline-block !important;
        width: auto !important;
        min-width: 120px !important;
        margin: 0 auto !important;
    }
    
    div[data-testid="stFileUploader"] button:hover {
        transform: translateY(-1px);
        box-shadow: 0 3px 8px rgba(102,126,234,0.3);
    }
    
    div[data-testid="stFileUploader"] button p {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Hide duplicate text */
    div[data-testid="stFileUploader"] .st-emotion-cache-1v0mbdj p:first-child {
        display: none !important;
    }
    
    /* Keep file info text clean */
    div[data-testid="stFileUploader"] .st-emotion-cache-1v0mbdj p:last-child {
        margin: 3px 0 !important;
        font-size: 11px !important;
        color: #555 !important;
    }
    
    div[data-testid="stFileUploader"] small {
        display: block !important;
        margin-top: 5px !important;
        font-size: 10px !important;
        color: #888 !important;
    }
    
    /* Column spacing */
    .row-widget.stColumns {
        gap: 0.3rem;
        margin-bottom: 0.3rem;
    }
    
    .stMetric {
        padding: 0.3rem;
        margin: 0.2rem;
    }
    
    div[data-testid="column"] {
        padding: 0 0.2rem;
    }
    
    p, div, span, h1, h2, h3, h4 {
        line-height: 1.3;
    }
    
    .stMarkdown p {
        margin-bottom: 0.3rem;
    }
    
    hr {
        margin: 0.5rem 0;
        border-color: rgba(255,255,255,0.2);
    }
    
    /* Slider, checkbox, multiselect labels */
    .stSlider > div label,
    .stCheckbox label,
    .stMultiSelect label {
        color: white !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            padding: 0.2rem 0.4rem !important;
            font-size: 0.65rem !important;
        }
        .metric-number {
            font-size: 1.2rem;
        }
        .metric-label {
            font-size: 0.65rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown("""
    <div class="main-header">
        <h1>📶 Social Media Analytics Dashboard</h1>
        <p>Advanced Analytics & Performance Tracking Across All Platforms</p>
    </div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("## 🛠️ Dashboard Controls")
    st.markdown("---")
    
    uploaded_file = st.file_uploader(
        "📂 Upload CSV File", 
        type=["csv"],
        help="Upload CSV with columns: Platform, Followers, Likes"
    )
    
    st.markdown("---")
    st.markdown("## ⚙️ Visualization Settings")
    chart_height = st.slider("Chart Height", 300, 600, 400)
    show_values = st.checkbox("Show Values on Charts", value=True)
    
    st.markdown("---")
    st.markdown("## 🤔 Metrics Selection")
    metrics_to_show = st.multiselect(
        "Select metrics to display",
        ["Followers", "Likes", "Comments", "Engagement Rate (%)"],
        default=["Followers", "Likes", "Comments"]
    )
    
    st.markdown("---")
    st.markdown("### 💡 Pro Tip")
    st.info("Upload your own CSV file to see real-time analytics!")

# ========== DATA LOADING FUNCTION ==========
@st.cache_data
def load_data(file):
    if file is not None:
        try:
            df = pd.read_csv(file)
            df.columns = df.columns.str.strip()
            
            platform_col = None
            followers_col = None
            likes_col = None
            
            for col in df.columns:
                if 'platform' in col.lower():
                    platform_col = col
                if 'follower' in col.lower():
                    followers_col = col
                if 'like' in col.lower():
                    likes_col = col
            
            if platform_col and followers_col and likes_col:
                df.rename(columns={
                    platform_col: "Platform",
                    followers_col: "Followers",
                    likes_col: "Likes"
                }, inplace=True)
            else:
                st.error("❌ Could not find required columns.")
                return None
            
            if "Comments" not in df.columns:
                df["Comments"] = (df["Likes"] * 0.25).round().astype(int)
            
            if "Engagement Rate (%)" not in df.columns:
                df["Engagement Rate (%)"] = ((df["Likes"] + df["Comments"]) / df["Followers"] * 100).round(2)
            
            df["Total Engagement"] = df["Likes"] + df["Comments"]
            df["Engagement Score"] = (df["Engagement Rate (%)"] * df["Followers"] / 100).round()
            
            return df
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            return None
    return None

# Load data
df = load_data(uploaded_file)

if df is None:
    df = pd.DataFrame({
        "Platform": ["Instagram", "Facebook", "Twitter", "YouTube", "TikTok", "LinkedIn"],
        "Followers": [28000, 12000, 8000, 45000, 35000, 5000],
        "Likes": [4200, 1500, 1200, 3800, 6800, 450],
        "Comments": [1050, 380, 300, 950, 1700, 110],
        "Engagement Rate (%)": [15.2, 12.8, 18.8, 9.5, 21.5, 8.2]
    })
    df["Total Engagement"] = df["Likes"] + df["Comments"]
    df["Engagement Score"] = (df["Engagement Rate (%)"] * df["Followers"] / 100).round()
    
    if uploaded_file is None:
        st.markdown('<div class="white-info-text">💡 <strong>Using Sample Data</strong> - Upload your CSV for personalized analysis!</div>', unsafe_allow_html=True)

#  DATASET INFORMATION 
st.markdown('<p style="font-size: 0.9rem; font-weight: 700; color: #2c3e50; margin-bottom: 0.3rem; background: rgba(255,255,255,0.8); display: inline-block; padding: 5px 10px; border-radius: 8px;"> DATASET INFORMATION</p>', unsafe_allow_html=True)

with st.expander("▼ VIEW DATASET DETAILS", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Platforms", len(df))
    with col2:
        st.metric("👥 Total Followers", f"{df['Followers'].sum():,}")
    with col3:
        st.metric("┈➤🚪 Avg Engagement", f"{df['Engagement Rate (%)'].mean():.1f}%")
    with col4:
        st.metric("⭐ Best Platform", df.nlargest(1, "Engagement Score")["Platform"].iloc[0])
    
    st.markdown("#### Data Preview")
    st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)

# ========== KEY METRICS ==========
st.markdown('<p class="kpi-header">🗝 Key Performance Indicators</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_followers = df["Followers"].sum()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">👤 Total Followers</div>
            <div class="metric-number">{total_followers:,}</div>
            <div class="metric-label">Across all platforms</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    total_likes = df["Likes"].sum()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">❤️ Total Likes</div>
            <div class="metric-number">{total_likes:,}</div>
            <div class="metric-label">Engagement received</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    total_comments = df["Comments"].sum()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💬 Total Comments</div>
            <div class="metric-number">{total_comments:,}</div>
            <div class="metric-label">User interactions</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    avg_engagement = df["Engagement Rate (%)"].mean()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">┈➤🚪 Avg Engagement Rate</div>
            <div class="metric-number">{avg_engagement:.1f}%</div>
            <div class="metric-label">Platform average</div>
        </div>
    """, unsafe_allow_html=True)

# ========== TABS ==========
tab1, tab2, tab3, tab4 = st.tabs([
    "👀 Overview", 
    "🎢 Detailed Analytics", 
    "⚖ Platform Comparison",  
    "💬 Insights & Reports"
])

# ========== TAB 1: OVERVIEW ==========
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👥 Followers by Platform")
        fig = px.bar(df, x="Platform", y="Followers", 
                     color="Platform", 
                     text="Followers" if show_values else None,
                     color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(height=chart_height, showlegend=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("❤️ Engagement Metrics")
        fig = px.bar(df, x="Platform", y=["Likes", "Comments"], 
                     barmode="group",
                     color_discrete_sequence=["#FF6B6B", "#4ECDC4"])
        fig.update_layout(height=chart_height, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("🎢 Engagement Rate Analysis")
    fig = px.bar(df, x="Platform", y="Engagement Rate (%)",
                 color="Engagement Rate (%)",
                 color_continuous_scale="Viridis",
                 text="Engagement Rate (%)" if show_values else None)
    fig.update_layout(height=chart_height, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# ========== TAB 2: DETAILED ANALYTICS ==========
with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⁀➴ Engagement Rate Trends")
        fig = px.line(df, x="Platform", y="Engagement Rate (%)", markers=True, line_shape="spline")
        fig.update_layout(height=chart_height, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("◔ Market Share")
        fig = px.pie(df, values="Followers", names="Platform", hole=0.4)
        fig.update_layout(height=chart_height)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("📐 Metrics Correlation")
    numeric_cols = ["Followers", "Likes", "Comments", "Engagement Rate (%)"]
    if all(col in df.columns for col in numeric_cols):
        corr_matrix = df[numeric_cols].corr()
        fig = px.imshow(corr_matrix, text_auto=True, aspect="auto")
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("★ ★ ★ ★ ★ Performance Score")
    fig = px.bar(df, x="Platform", y="Engagement Score",
                 color="Engagement Score",
                 color_continuous_scale="Plasma",
                 text="Engagement Score" if show_values else None)
    fig.update_layout(height=chart_height, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# ========== TAB 3: PLATFORM COMPARISON ==========
with tab3:
    selected_platform = st.selectbox(" Select Platform", df["Platform"])
    platform_data = df[df["Platform"] == selected_platform].iloc[0]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👥 Followers", f"{platform_data['Followers']:,}")
    with col2:
        st.metric("❤️ Likes", f"{platform_data['Likes']:,}")
    with col3:
        st.metric("💬 Comments", f"{platform_data['Comments']:,}")
    with col4:
        st.metric("┈➤🚪 Engagement", f"{platform_data['Engagement Rate (%)']:.1f}%")
    
    st.subheader("𖣠 Performance Radar")
    metrics = ["Followers", "Likes", "Comments", "Engagement Rate (%)"]
    radar_df = df.copy()
    for metric in metrics:
        max_val = radar_df[metric].max()
        if max_val > 0:
            radar_df[metric] = (radar_df[metric] / max_val) * 100
    
    fig = go.Figure()
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c']
    for i, platform in enumerate(df["Platform"]):
        platform_data_radar = radar_df[radar_df["Platform"] == platform]
        fig.add_trace(go.Scatterpolar(
            r=[platform_data_radar[m].values[0] for m in metrics],
            theta=metrics, fill='toself', name=platform, line_color=colors[i % len(colors)]
        ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True, height=450)
    st.plotly_chart(fig, use_container_width=True)

# ========== TAB 4: INSIGHTS ==========
with tab4:
    st.subheader("💬 Performance Insights")
    
    col1, col2 = st.columns(2)
    with col1:
        top_followers = df.nlargest(1, "Followers")["Platform"].iloc[0]
        top_engagement = df.nlargest(1, "Engagement Rate (%)")["Platform"].iloc[0]
        
        # Using HTML/CSS to force black text color
        st.markdown(f"""
            <div style="background-color: #e8f4f8; padding: 10px; border-radius: 8px; margin: 5px 0; border-left: 4px solid #00b4d8;">
                <p style="color: black; margin: 0; font-size: 14px;">♛ <strong>Most Followers:</strong> {top_followers}</p>
            </div>
            <div style="background-color: #e8f4f8; padding: 10px; border-radius: 8px; margin: 5px 0; border-left: 4px solid #00b4d8;">
                <p style="color: black; margin: 0; font-size: 14px;">➤ <strong>Best Engagement:</strong> {top_engagement}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💡 Recommendations")
        avg_eng = df['Engagement Rate (%)'].mean()
        low_engagement = df[df['Engagement Rate (%)'] < avg_eng]['Platform'].tolist()
        if low_engagement:
            st.markdown(f"""
                <div style="background-color: #fff3cd; padding: 10px; border-radius: 8px; margin: 5px 0; border-left: 4px solid #ffc107;">
                    <p style="color: black; margin: 0; font-size: 14px;">🗫 <strong>Improve:</strong> {', '.join(low_engagement)}</p>
                </div>
            """, unsafe_allow_html=True)
        best = df.nlargest(1, 'Engagement Rate (%)')['Platform'].iloc[0]
        st.markdown(f"""
            <div style="background-color: #d4edda; padding: 10px; border-radius: 8px; margin: 5px 0; border-left: 4px solid #28a745;">
                <p style="color: black; margin: 0; font-size: 14px;">▶ <strong>Replicate:</strong> {best}'s strategy</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🡻 Export Reports")
    
    if st.button("📃 Generate Report"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report = pd.DataFrame({
            "Metric": ["Generated On", "Total Followers", "Avg Engagement", "Best Platform"],
            "Value": [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"{total_followers:,}", f"{avg_engagement:.2f}%", df.nlargest(1, "Engagement Rate (%)")["Platform"].iloc[0]]
        })
        csv = report.to_csv(index=False)
        st.download_button("Download Report", csv, f"report_{timestamp}.csv", "text/csv")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>Built with Streamlit | Social Media Analytics Dashboard </p>
    </div>
""", unsafe_allow_html=True)