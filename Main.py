import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import plotly.express as px


df = pd.read_excel(r'C:\Users\hengli.chen\Desktop\客群分析\儀錶板\底稿.xlsx')
df2 = pd.read_excel(r'C:\Users\hengli.chen\Desktop\客群分析\儀錶板\達成率底稿.xlsx', sheet_name='分公司_業績達成率')
df3 = pd.read_excel(r'C:\Users\hengli.chen\Desktop\客群分析\儀錶板\達成率底稿.xlsx', sheet_name='區部_業績達成率')

df4 = pd.read_excel(r'C:\Users\hengli.chen\Desktop\客群分析\儀錶板\達成率底稿.xlsx', sheet_name='分公司_收入達成率')
df5 = pd.read_excel(r'C:\Users\hengli.chen\Desktop\客群分析\儀錶板\達成率底稿.xlsx', sheet_name='區部_收入達成率')

date= str('1028')




def main():
    st.set_page_config(page_title="客群儀表板", layout="wide")
    st.title("歡迎來到客群儀表板")
    st.write(
    """
    傳統上我們習慣以報表，來監控客群與商品的營運表現
    """
    """
    希望透過這個儀表板，讓 PM、輔銷或是前線營業員，能看到商品與客群，階段性的趨勢表現，而不僅限於單點
    """
    """
    同時，也能省去繁雜的報表產製跟寄送作業。
    """)
    st.sidebar.header("請由此篩選條件：")
    st.markdown(
    """
    <style>
    <style>
    .metric-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px; ##邊框圓角
        background-color:#FFC0CB;
    }
    .metric-text {
        font-size: 25px; /* 調整這裡的數值來改變文字大小 */
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        padding: 2px;
        text-decoration: underline;
    }
    .metric-value {
        font-size: 24px; /* 調整這裡的數值來改變數值大小 */
        color: #007bff;
        margin-bottom: 10px;
        padding: 2px;
    }
    .metric-change {
        font-size: 16px; /* 調整這裡的數值來改變變化百分比大小 */
        color: #28a745;
        margin-bottom: 10px;
        padding: 10px;
    }
    .title {
    background-color: #99CCFF; /* 設置子標題的背景顏色 */
    padding: 15px;
    border-radius: 5px;
    font-size: 30px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 20px;
    }
    .subtitle {
    background-color: #B0E0E6; /* 設置子標題的背景顏色 */
    padding: 15px;
    border-radius: 5px;
    font-size: 30px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 20px;
    }
    .subsubtitle {
    padding: 15px;
    border-radius: 5px;
    font-size: 25px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 20px;
    }
    .divider {
        border-top: 5px solid #bbb;
        margin: 20px 0;
    }
    .vertical-line {
        border-left: 5px solid #bbb;
        height: 100%;
        position: absolute;
        left: 50%;
        margin-left: -1px;
        top: 0;
    }
    </style>
    """,unsafe_allow_html=True)

    
    

    ## 左側選單
    area=st.sidebar.multiselect('區部',  df['區部_高頻回歸_DS'].unique())
    branches=st.sidebar.multiselect('分公司',  df['分公司_高頻回歸_DS'].unique())


    financial_products = ['海外股票', '海外債', '基金', '境外結構型商品', '境內結構型商品', '保險']
    Financial_Products = st.sidebar.multiselect('財管商品', financial_products)


    with st.sidebar:
     st.title("關於")
     st.info("用於快速掌握各客群於財管商品之交易狀況與趨勢，以及財管商品之達成率")

    with st.sidebar:
     st.title("Copyright")
     st.markdown(
        """
        <style>
        .custom-text {
            background-color: transparent;
            color: black;
        }
        </style>
        <div class="custom-text">客群分析科 陳亨利 (61702)</div>
        """
        , unsafe_allow_html=True
    )


    
    
    st.markdown('---')  # 這行會加一個分隔線
    st.markdown('<div class="title"> 區部達成率</div>', unsafe_allow_html=True)

    products = ['整體財管商品','海外股票', '海外債', '基金', '結構型商品', '壽險']
    Products = st.multiselect('為檢視達成率，請由下先篩選財管商品，然後再選擇左方區部與分公司', products)


    col1, col2 = st.columns(2)
    col1.markdown(f'<div class="metric-container"><div class="metric-text">業績達成率</div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="metric-container"><div class="metric-text">收入達成率</div>', unsafe_allow_html=True)

    if Products:
        with col1:
            for product in Products:
                if area:
                    for selected_area in area:
                        filtered_df3 = df3[(df3['區部'] == selected_area)]
                        if not filtered_df3.empty:
                            value = float(filtered_df3[product].values) * 100
                            col1.metric(label=f"{selected_area} {product} ", value=f'{value:.0f}%')
                        else:
                            col1.metric(label=f"{selected_area} {product}", value="沒有找到符合條件的數據")
        with col2:
            for product in Products:
                if area:
                    for selected_area in area:
                        filtered_df5 = df5[(df5['區部'] == selected_area)]
                        if not filtered_df5.empty:
                            value = float(filtered_df5[product].values) * 100
                            col2.metric(label=f"{selected_area} {product}", value=f'{value:.0f}%')
                        else:
                            col2.metric(label=f"{selected_area} {product}", value="沒有找到符合條件的數據")




    st.markdown('<div class="subtitle"> 分公司達成率</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.markdown(f'<div class="metric-container"><div class="metric-text">業績達成率</div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="metric-container"><div class="metric-text">收入達成率</div>', unsafe_allow_html=True)

    with col1:
            for product in Products:
                if branches:
                    for selected_branch in branches:
                        filtered_df2 = df2[(df2['分公司'] == selected_branch)]
                        if not filtered_df2.empty:
                            value = float(filtered_df2[product].values) * 100
                            col1.metric(label=f"{selected_branch} {product}", value=f'{value:.0f}%')
                        else:
                            col1.metric(label=f"{selected_branch} {product}", value="沒有找到符合條件的數據")
    with col2:
            for product in Products:
                if branches:
                    for selected_branch in branches:
                        filtered_df4 = df4[(df4['分公司'] == selected_branch)]
                        if not filtered_df4.empty:
                            value = float(filtered_df4[product].values) * 100
                            col2.metric(label=f"{selected_branch} {product}", value=f'{value:.0f}%')
                        else:
                            col2.metric(label=f"{selected_branch} {product}", value="沒有找到符合條件的數據")

    # st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # col1, col2, col3, col4 = st.columns(4)

    
    # col1.markdown('<div class="metric-text">富裕客群</div>', unsafe_allow_html=True)    
    # col1.markdown('<div class="metric-text">客群人數</div><div class="metric-value"></div>', unsafe_allow_html=True)
    # col1.markdown('<div class="metric-text">實動人數</div><div class="metric-value"></div>', unsafe_allow_html=True)


    # col2.markdown('<div class="metric-text">價值Plus客群</div>', unsafe_allow_html=True)
    # col2.markdown('<div class="metric-text">客群人數</div><div class="metric-value"></div>', unsafe_allow_html=True)
    # col2.markdown('<div class="metric-text">實動人數</div><div class="metric-value"></div>', unsafe_allow_html=True)
    
    # col3.markdown('<div class="metric-text">價值一般</div', unsafe_allow_html=True)
    # col3.markdown('<div class="metric-text">客群人數</div><div class="metric-value"></div>', unsafe_allow_html=True)
    # col3.markdown('<div class="metric-text">實動人數</div><div class="metric-value"></div>', unsafe_allow_html=True)

    # col4.markdown('<div class="metric-text">潛力客群</div>', unsafe_allow_html=True)
    # col4.markdown('<div class="metric-text">客群人數</div><div class="metric-value"></div>', unsafe_allow_html=True)
    # col4.markdown('<div class="metric-text">實動人數</div><div class="metric-value"></div>', unsafe_allow_html=True)

    # st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


    st.markdown(
    """
    <style>
    .custom-header {
        padding: 15px;ㄐ
        border-radius: 5px;
        font-size: 30px; /* 調整這裡的數值來改變字體大小 */
        text-align: center; /* 置中對齊 */
        font-weight: bold; 
        color:#000000; /* 設置字體顏色 */
        background-color: #87CEEB; /* 設置背景顏色為淺灰色 */
        margin-bottom: 20px; /* 下邊距 */
    }
    </style>
    """,
    unsafe_allow_html=True
                        )

    st.markdown('---')  # 這行會加一個分隔線
    st.write("""
            <p><i class="fas fa-arrow-left"> 請由左側篩選條件</i></p>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
            """, unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["交易量", "實動戶","收入","收益率"])
    
    with tab1 : 

        st.markdown('<div class="custom-header">交易量 </div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        if '海外股票' in Financial_Products:
            with col1:
                if area:
                    for selected_area in area:
                        st.subheader(f'{selected_area}-海外股票交易量')
                        stock_data = df[df['區部_高頻回歸_DS']== selected_area]
                        stock_data = stock_data[['區部_高頻回歸_DS', '客群類別', '海外股票交易量_202409', '海外股票交易量_202408', '海外股票交易量_202407', '海外股票交易量_202406', '海外股票交易量_202405', '海外股票交易量_202404', '海外股票交易量_202403', '海外股票交易量_202402', '海外股票交易量_202401']]
                        stock_data = stock_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外股票交易量')
                        stock_data['月份'] = stock_data['月份'].str.replace('海外股票交易量_', '')
                        
                        stock_data.reset_index(inplace=True) ## 解決 Multiindex 問題
                        fig = px.line(stock_data.groupby(['月份', '客群類別'])['海外股票交易量'].sum().reset_index(), x='月份', y='海外股票交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)

                if branches:
                    for selected_branch in branches:
                        st.subheader(f'{selected_branch}-海外股票交易量')
                        stock_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                        stock_data = stock_data[['分公司_高頻回歸_DS', '客群類別', '海外股票交易量_202409', '海外股票交易量_202408', '海外股票交易量_202407', '海外股票交易量_202406', '海外股票交易量_202405', '海外股票交易量_202404', '海外股票交易量_202403', '海外股票交易量_202402', '海外股票交易量_202401']]
                        stock_data = stock_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外股票交易量')
                        stock_data['月份'] = stock_data['月份'].str.replace('海外股票交易量_', '')

                        stock_data.reset_index(inplace=True)
                        fig = px.line(stock_data.groupby(['月份', '客群類別'])['海外股票交易量'].sum().reset_index(), x='月份', y='海外股票交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


        if '海外債' in Financial_Products:
            with col2:
                if area:
                    for selected_area in area:
                        st.subheader(f'{selected_area}-海外債交易量')
                        bond_data = df[df['區部_高頻回歸_DS']== selected_area]
                        bond_data = bond_data[['區部_高頻回歸_DS', '客群類別', '海外債交易量_202409', '海外債交易量_202408', '海外債交易量_202407', '海外債交易量_202406', '海外債交易量_202405', '海外債交易量_202404', '海外債交易量_202403', '海外債交易量_202402', '海外債交易量_202401']]
                        bond_data = bond_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外債交易量')
                        bond_data['月份'] = bond_data['月份'].str.replace('海外債交易量_', '')

                        bond_data.reset_index(inplace=True)
                        fig = px.line(bond_data.groupby(['月份', '客群類別'])['海外債交易量'].sum().reset_index(), x='月份', y='海外債交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)

                if branches:
                    for selected_branch in branches:
                        st.subheader(f'{selected_branch}-海外債交易量')
                        bond_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                        bond_data = bond_data[['分公司_高頻回歸_DS', '客群類別', '海外債交易量_202409', '海外債交易量_202408', '海外債交易量_202407', '海外債交易量_202406', '海外債交易量_202405', '海外債交易量_202404', '海外債交易量_202403', '海外債交易量_202402', '海外債交易量_202401']]
                        bond_data = bond_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外債交易量')
                        bond_data['月份'] = bond_data['月份'].str.replace('海外債交易量_', '')

                        bond_data.reset_index(inplace=True)
                        fig = px.line(bond_data.groupby(['月份', '客群類別'])['海外債交易量'].sum().reset_index(), x='月份', y='海外債交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


        if '基金' in Financial_Products:
            with col1:
                if area:
                    for selected_area in area:
                        st.subheader(f'{selected_area}-基金交易量')
                        fund_data = df[df['區部_高頻回歸_DS']== selected_area]
                        fund_data = fund_data[['區部_高頻回歸_DS', '客群類別', '基金交易量_202409', '基金交易量_202408', '基金交易量_202407', '基金交易量_202406', '基金交易量_202405', '基金交易量_202404', '基金交易量_202403', '基金交易量_202402', '基金交易量_202401']]
                        fund_data = fund_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='基金交易量')
                        fund_data['月份'] = fund_data['月份'].str.replace('基金交易量_', '')

                        fund_data.reset_index(inplace=True)
                        fig = px.line(fund_data.groupby(['月份', '客群類別'])['基金交易量'].sum().reset_index(), x='月份', y='基金交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)

                if branches:
                    for selected_branch in branches:
                        st.subheader(f'{selected_branch}-基金交易量')
                        fund_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                        fund_data = fund_data[['分公司_高頻回歸_DS', '客群類別', '基金交易量_202409', '基金交易量_202408', '基金交易量_202407', '基金交易量_202406', '基金交易量_202405', '基金交易量_202404', '基金交易量_202403', '基金交易量_202402', '基金交易量_202401']]
                        fund_data = fund_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='基金交易量')
                        fund_data['月份'] = fund_data['月份'].str.replace('基金交易量_', '')

                        fund_data.reset_index(inplace=True)
                        fig = px.line(fund_data.groupby(['月份', '客群類別'])['基金交易量'].sum().reset_index(), x='月份', y='基金交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


        if '境外結構型商品' in Financial_Products:
            with col2:
                if area:
                    for selected_area in area:
                        st.subheader(f'{selected_area}-境外結構型交易量')
                        FSN_data = df[df['區部_高頻回歸_DS']== selected_area]
                        FSN_data = FSN_data[['區部_高頻回歸_DS', '客群類別', '境外結構交易量_202409', '境外結構交易量_202408', '境外結構交易量_202407', '境外結構交易量_202406', '境外結構交易量_202405', '境外結構交易量_202404', '境外結構交易量_202403', '境外結構交易量_202402', '境外結構交易量_202401']]
                        FSN_data = FSN_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境外結構交易量')
                        FSN_data['月份'] = FSN_data['月份'].str.replace('境外結構交易量_', '')

                        FSN_data.reset_index(inplace=True)
                        fig = px.line(FSN_data.groupby(['月份', '客群類別'])['境外結構交易量'].sum().reset_index(), x='月份', y='境外結構交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


                if branches:
                    for selected_branch in branches:
                        st.subheader(f'{selected_branch}-境外結構型交易量')
                        FSN_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                        FSN_data = FSN_data[['分公司_高頻回歸_DS', '客群類別', '境外結構交易量_202409', '境外結構交易量_202408', '境外結構交易量_202407', '境外結構交易量_202406', '境外結構交易量_202405', '境外結構交易量_202404', '境外結構交易量_202403', '境外結構交易量_202402', '境外結構交易量_202401']]
                        FSN_data = FSN_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境外結構交易量')
                        FSN_data['月份'] = FSN_data['月份'].str.replace('境外結構交易量_', '')
                        
                        FSN_data.reset_index(inplace=True)
                        fig = px.line(FSN_data.groupby(['月份', '客群類別'])['境外結構交易量'].sum().reset_index(), x='月份', y='境外結構交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


        if '境內結構型商品' in Financial_Products:
            with col1:
                if area:
                    for selected_area in area:
                        st.subheader(f'{selected_area}-境內結構型交易量')
                        SN_data = df[df['區部_高頻回歸_DS']== selected_area]
                        SN_data = SN_data[['區部_高頻回歸_DS', '客群類別', '境內結構交易量_202409', '境內結構交易量_202408', '境內結構交易量_202407', '境內結構交易量_202406', '境內結構交易量_202405', '境內結構交易量_202404', '境內結構交易量_202403', '境內結構交易量_202402', '境內結構交易量_202401']]
                        SN_data = SN_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境內結構交易量')
                        SN_data['月份'] = SN_data['月份'].str.replace('境內結構交易量_', '')

                        SN_data.reset_index(inplace=True)
                        fig = px.line(SN_data.groupby(['月份', '客群類別'])['境內結構交易量'].sum().reset_index(), x='月份', y='境內結構交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


                if branches:
                    for selected_branch in branches:
                        st.subheader(f'{selected_branch}-境內結構型交易量')
                        SN_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                        SN_data = SN_data[['分公司_高頻回歸_DS', '客群類別', '境內結構交易量_202409', '境內結構交易量_202408', '境內結構交易量_202407', '境內結構交易量_202406', '境內結構交易量_202405', '境內結構交易量_202404', '境內結構交易量_202403', '境內結構交易量_202402', '境內結構交易量_202401']]
                        SN_data = SN_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境內結構交易量')
                        SN_data['月份'] = SN_data['月份'].str.replace('境內結構交易量_', '')

                        SN_data.reset_index(inplace=True)
                        fig = px.line(SN_data.groupby(['月份', '客群類別'])['境內結構交易量'].sum().reset_index(), x='月份', y='境內結構交易量', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


        if '保險' in Financial_Products:
            with col2:
                if area:
                    for selected_area in area:
                        st.subheader(f'{selected_area}-保險銷售額')
                        Insurance_data = df[df['區部_高頻回歸_DS']== selected_area]
                        Insurance_data = Insurance_data[['區部_高頻回歸_DS', '客群類別', '保費_202409', '保費_202408', '保費_202407', '保費_202406', '保費_202405', '保費_202404', '保費_202403', '保費_202402', '保費_202401']]
                        Insurance_data = Insurance_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='保費')
                        Insurance_data['月份'] = Insurance_data['月份'].str.replace('保費_', '')

                        Insurance_data.reset_index(inplace=True)
                        fig = px.line(Insurance_data.groupby(['月份', '客群類別'])['保費'].sum().reset_index(), x='月份', y='保費', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)

                if branches:
                    for selected_branch in branches:
                        st.subheader(f'{selected_branch}-保險銷售額')
                        Insurance_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                        Insurance_data = Insurance_data[['分公司_高頻回歸_DS', '客群類別', '保費_202409', '保費_202408', '保費_202407', '保費_202406', '保費_202405', '保費_202404', '保費_202403', '保費_202402', '保費_202401']]
                        Insurance_data = Insurance_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='保費')
                        Insurance_data['月份'] = Insurance_data['月份'].str.replace('保費_', '')

                        Insurance_data.reset_index(inplace=True)
                        fig = px.line(Insurance_data.groupby(['月份', '客群類別'])['保費'].sum().reset_index(), x='月份', y='保費', color='客群類別')
                        fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                        fig.update_xaxes(title_text='', tickformat='%Y%m')
                        st.plotly_chart(fig)


        st.markdown(
        """
        <style>
        .custom-subheader {
            padding: 15px;
            border-radius: 5px;
            font-size: 30px; /* 調整這裡的數值來改變字體大小 */
            text-align: center; /* 置中對齊 */
            font-weight: bold; 
            color:#000000; /* 設置字體顏色 */
            background-color: #AFEEEE; 
            margin-bottom: 20px; /* 下邊距 */
        }
        </style>
        """,
        unsafe_allow_html=True
                            )

    with tab2 : 
        st.markdown('<div class="custom-subheader">實動戶 </div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

#海外股實動戶

    if '海外股票' in Financial_Products:
        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area}-海外股票實動戶')
                    stock_data = df[df['區部_高頻回歸_DS']== selected_area]
                    stock_data = stock_data[['區部_高頻回歸_DS', '客群類別', '海股戶數_202408', '海股戶數_202407', '海股戶數_202406', '海股戶數_202405', '海股戶數_202404', '海股戶數_202403', '海股戶數_202402', '海股戶數_202401']]
                    stock_data = stock_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外股票實動戶')
                    stock_data['月份'] = stock_data['月份'].str.replace('海股戶數_', '')

                    stock_data.reset_index(inplace=True)
                    fig = px.line(stock_data.groupby(['月份', '客群類別'])['海外股票實動戶'].sum().reset_index(), x='月份', y='海外股票實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)                  

            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch}-海外股票實動戶')
                    stock_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                    stock_data = stock_data[['分公司_高頻回歸_DS', '客群類別', '海股戶數_202408', '海股戶數_202407', '海股戶數_202406', '海股戶數_202405', '海股戶數_202404', '海股戶數_202403', '海股戶數_202402', '海股戶數_202401']]
                    stock_data = stock_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外股票實動戶')
                    stock_data['月份'] = stock_data['月份'].str.replace('海股戶數_', '')

                    stock_data.reset_index(inplace=True)
                    fig = px.line(stock_data.groupby(['月份', '客群類別'])['海外股票實動戶'].sum().reset_index(), x='月份', y='海外股票實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)          

#海外債實動戶

    if '海外債' in Financial_Products:
        with col2:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area}-海外債實動戶')
                    bond_data = df[df['區部_高頻回歸_DS']== selected_area]
                    bond_data = bond_data[['區部_高頻回歸_DS', '客群類別', '海外債戶數_202408', '海外債戶數_202407', '海外債戶數_202406', '海外債戶數_202405', '海外債戶數_202404', '海外債戶數_202403', '海外債戶數_202402', '海外債戶數_202401']]
                    bond_data = bond_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外債實動戶')
                    bond_data['月份'] = bond_data['月份'].str.replace('海外債戶數_', '')

                    bond_data.reset_index(inplace=True)
                    fig = px.line(bond_data.groupby(['月份', '客群類別'])['海外債實動戶'].sum().reset_index(), x='月份', y='海外債實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)


            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch}-海外債實動戶')
                    bond_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                    bond_data = bond_data[['分公司_高頻回歸_DS', '客群類別', '海外債戶數_202408', '海外債戶數_202407', '海外債戶數_202406', '海外債戶數_202405', '海外債戶數_202404', '海外債戶數_202403', '海外債戶數_202402', '海外債戶數_202401']]
                    bond_data = bond_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='海外債實動戶')
                    bond_data['月份'] = bond_data['月份'].str.replace('海外債戶數_', '')

                    bond_data.reset_index(inplace=True)
                    fig = px.line(bond_data.groupby(['月份', '客群類別'])['海外債實動戶'].sum().reset_index(), x='月份', y='海外債實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)


#基金實動戶

    if '基金' in Financial_Products:
        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area}-基金實動戶')
                    fund_data = df[df['區部_高頻回歸_DS']== selected_area]
                    fund_data = fund_data[['區部_高頻回歸_DS', '客群類別', '基金戶數_202408', '基金戶數_202407', '基金戶數_202406', '基金戶數_202405', '基金戶數_202404', '基金戶數_202403', '基金戶數_202402', '基金戶數_202401']]
                    fund_data = fund_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='基金實動戶')
                    fund_data['月份'] = fund_data['月份'].str.replace('基金戶數_', '')

                    fund_data.reset_index(inplace=True)
                    fig = px.line(fund_data.groupby(['月份', '客群類別'])['基金實動戶'].sum().reset_index(), x='月份', y='基金實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch} _ 基金實動戶')
                    fund_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                    fund_data = fund_data[['分公司_高頻回歸_DS', '客群類別', '基金戶數_202408', '基金戶數_202407', '基金戶數_202406', '基金戶數_202405', '基金戶數_202404', '基金戶數_202403', '基金戶數_202402', '基金戶數_202401']]
                    fund_data = fund_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='基金實動戶')
                    fund_data['月份'] = fund_data['月份'].str.replace('基金戶數_', '')

                    fund_data.reset_index(inplace=True)
                    fig = px.line(fund_data.groupby(['月份', '客群類別'])['基金實動戶'].sum().reset_index(), x='月份', y='基金實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)


#境外結構型實動戶

    if '境外結構型商品' in Financial_Products:
        with col2:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area}-境外結構型實動戶')
                    FSN_data = df[df['區部_高頻回歸_DS']== selected_area]
                    FSN_data = FSN_data[['區部_高頻回歸_DS', '客群類別', '境外結構戶數_202408', '境外結構戶數_202407', '境外結構戶數_202406', '境外結構戶數_202405', '境外結構戶數_202404', '境外結構戶數_202403', '境外結構戶數_202402', '境外結構戶數_202401']]
                    FSN_data = FSN_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境外結構實動戶')
                    FSN_data['月份'] = FSN_data['月份'].str.replace('境外結構戶數_', '')

                    FSN_data.reset_index(inplace=True)
                    fig = px.line(FSN_data.groupby(['月份', '客群類別'])['境外結構實動戶'].sum().reset_index(), x='月份', y='境外結構實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)


            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch}-境外結構型實動戶')
                    FSN_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                    FSN_data = FSN_data[['分公司_高頻回歸_DS', '客群類別', '境外結構戶數_202408', '境外結構戶數_202407', '境外結構戶數_202406', '境外結構戶數_202405', '境外結構戶數_202404', '境外結構戶數_202403', '境外結構戶數_202402', '境外結構戶數_202401']]
                    FSN_data = FSN_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境外結構實動戶')
                    FSN_data['月份'] = FSN_data['月份'].str.replace('境外結構戶數_', '')

                    FSN_data.reset_index(inplace=True)
                    fig = px.line(FSN_data.groupby(['月份', '客群類別'])['境外結構實動戶'].sum().reset_index(), x='月份', y='境外結構實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)
    
#境內結構型實動戶

    if '境內結構型商品' in Financial_Products:
        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area}-境內結構型實動戶')
                    SN_data = df[df['區部_高頻回歸_DS']== selected_area]
                    SN_data = SN_data[['區部_高頻回歸_DS', '客群類別', '境內結構戶數_202408', '境內結構戶數_202407', '境內結構戶數_202406', '境內結構戶數_202405', '境內結構戶數_202404', '境內結構戶數_202403', '境內結構戶數_202402', '境內結構戶數_202401']]
                    SN_data = SN_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境內結構實動戶')
                    SN_data['月份'] = SN_data['月份'].str.replace('境內結構戶數_', '')

                    SN_data.reset_index(inplace=True)
                    fig =px.line(SN_data.groupby(['月份', '客群類別'])['境內結構實動戶'].sum().reset_index(), x='月份', y='境內結構實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch}-境內結構型實動戶')
                    SN_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                    SN_data = SN_data[['分公司_高頻回歸_DS', '客群類別', '境內結構戶數_202408', '境內結構戶數_202407', '境內結構戶數_202406', '境內結構戶數_202405', '境內結構戶數_202404', '境內結構戶數_202403', '境內結構戶數_202402', '境內結構戶數_202401']]
                    SN_data = SN_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='境內結構實動戶')
                    SN_data['月份'] = SN_data['月份'].str.replace('境內結構戶數_', '')

                    SN_data.reset_index(inplace=True)
                    fig = px.line(SN_data.groupby(['月份', '客群類別'])['境內結構實動戶'].sum().reset_index(), x='月份', y='境內結構實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)


#保險實動戶  

    if '保險' in Financial_Products:
        with col2:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area}-保險實動戶')
                    Insurance_data = df[df['區部_高頻回歸_DS']== selected_area]
                    Insurance_data = Insurance_data[['區部_高頻回歸_DS', '客群類別', '保險戶數_202408', '保險戶數_202407', '保險戶數_202406', '保險戶數_202405', '保險戶數_202404', '保險戶數_202403', '保險戶數_202402', '保險戶數_202401']]
                    Insurance_data = Insurance_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='保險實動戶')
                    Insurance_data['月份'] = Insurance_data['月份'].str.replace('保險戶數_', '')
                    
                    Insurance_data.reset_index(inplace=True)
                    fig = px.line(Insurance_data.groupby(['月份', '客群類別'])['保險實動戶'].sum().reset_index(), x='月份', y='保險實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch}-保險實動戶')
                    Insurance_data = df[df['分公司_高頻回歸_DS']== selected_branch]
                    Insurance_data = Insurance_data[['分公司_高頻回歸_DS', '客群類別', '保險戶數_202408', '保險戶數_202407', '保險戶數_202406', '保險戶數_202405', '保險戶數_202404', '保險戶數_202403', '保險戶數_202402', '保險戶數_202401']]
                    Insurance_data = Insurance_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='保險實動戶')
                    Insurance_data['月份'] = Insurance_data['月份'].str.replace('保險戶數_', '')

                    Insurance_data.reset_index(inplace=True)
                    fig = px.line(Insurance_data.groupby(['月份', '客群類別'])['保險實動戶'].sum().reset_index(), x='月份', y='保險實動戶', color='客群類別')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)




    st.markdown(
    """
    <style>
    .custom-customer {
        padding: 15px;
        border-radius: 5px;
        font-size: 30px; /* 調整這裡的數值來改變字體大小 */
        text-align: center; /* 置中對齊 */
        font-weight: bold; 
        color:#000000; /* 設置字體顏色 */
        background-color: #B0C4DE; 
        margin-bottom: 20px; /* 下邊距 */
    }
    </style>
    """,
    unsafe_allow_html=True
                        )

    st.markdown('---')  # 這行會加一個分隔線
    st.markdown('<div class="custom-customer">客群成長趨勢 </div>', unsafe_allow_html=True)
    st.write("""
            <p><i class="fas fa-arrow-left"> 請由左側篩選條件</i></p>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
            """, unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["富裕", "價值Plus","價值一般","潛力"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area} - 富裕客群數')
                    stock_data = df[df['區部_高頻回歸_DS'] == selected_area]

                    stock_data = stock_data[['區部_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')

                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')
                    stock_data=stock_data[stock_data['客群類別']=='富裕']          

                    fig = px.area(stock_data.groupby('月份')['人數'].sum())
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)
        with col2:
            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch} - 富裕客群數')
                    stock_data = df[df['分公司_高頻回歸_DS'] == selected_branch]
                    stock_data = stock_data[['分公司_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')
                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')
                    stock_data=stock_data[stock_data['客群類別']=='富裕']

                    fig = px.line(stock_data, x='月份', y='人數')
                    fig.update_layout(xaxis_title='', yaxis_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)      
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area} - 價值Plus客群數')
                    stock_data = df[df['區部_高頻回歸_DS'] == selected_area]

                    stock_data = stock_data[['區部_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')

                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')
                    stock_data=stock_data[stock_data['客群類別']=='價值Plus']          
                           
                    fig = px.area(stock_data.groupby('月份')['人數'].sum())
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)
        with col2:   
            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch} -價值Plus客群數')
                    stock_data = df[df['分公司_高頻回歸_DS'] == selected_branch]
                    stock_data = stock_data[['分公司_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')
                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')

                    stock_data=stock_data[stock_data['客群類別']=='價值Plus']
                    fig = px.line(stock_data, x='月份', y='人數')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

    with tab3:
        col1, col2 = st.columns(2)

        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area} - 價值一般客群數')
                    stock_data = df[df['區部_高頻回歸_DS'] == selected_area]

                    stock_data = stock_data[['區部_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')

                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')
                    stock_data=stock_data[stock_data['客群類別']=='價值一般']          
                           
                    fig = px.area(stock_data.groupby('月份')['人數'].sum())
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)
        with col2:
            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch} -價值一般客群數')
                    stock_data = df[df['分公司_高頻回歸_DS'] == selected_branch]
                    stock_data = stock_data[['分公司_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')
                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')
                    stock_data=stock_data[stock_data['客群類別']=='價值一般']
                    fig = px.line(stock_data, x='月份', y='人數')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            if area:
                for selected_area in area:
                    st.subheader(f'{selected_area} -潛力客群數')
                    stock_data = df[df['區部_高頻回歸_DS'] == selected_area]

                    stock_data = stock_data[['區部_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['區部_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')

                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')
                    stock_data=stock_data[stock_data['客群類別']=='潛力']          
                           
                    fig = px.area(stock_data.groupby('月份')['人數'].sum())
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

        with col2:
            if branches:
                for selected_branch in branches:
                    st.subheader(f'{selected_branch} -潛力客群數')
                    stock_data = df[df['分公司_高頻回歸_DS'] == selected_branch]
                    stock_data = stock_data[['分公司_高頻回歸_DS', '客群類別', '戶數_202408', '戶數_202407', '戶數_202406', '戶數_202405', '戶數_202404', '戶數_202403', '戶數_202402']]
                    stock_data = stock_data.melt(id_vars=['分公司_高頻回歸_DS', '客群類別'], var_name='月份', value_name='人數')
                    stock_data['月份'] = stock_data['月份'].str.replace('戶數_', '')

                    stock_data=stock_data[stock_data['客群類別']=='潛力']
                    fig = px.line(stock_data, x='月份', y='人數')
                    fig.update_layout(xaxis_title='', yaxis_title='', legend_title='客群類別')
                    fig.update_xaxes(title_text='', tickformat='%Y%m')
                    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

    

