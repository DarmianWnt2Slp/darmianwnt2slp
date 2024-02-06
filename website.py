import streamlit as st
from PIL import Image

page = st.sidebar.radio("首页",["简介","汉化作品","英汉词典","赞助区","照片处理","留言区","每日一问","问卷调查"])

# 图像处理
def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x,y] = (b, r, g)
    return img

# 1-1
def page1():
    st.write(":red[欢迎来到我的网站！在这里请文明使用每一项功能，感谢您的配合！！]")


#1-2
def page2():
    with open("screamingwall.mp3","rb") as f:
        bgm = f.read()
    tab1, tab2, tab3, tab4 = st.tabs([":green[Las Monjas]",":red[The Other Roles]",":orange[Town Of Us]","Town Of Host"])
    with tab1:
        st.audio(bgm, format = "mp3", start_time = 0)
        st.write(":green[Las Monjas v3.7.1]")
        st.link_button('下载链接', 'https://www.baidu.com/')
        st.write(":green[Las Monjas v3.7.0]")
        st.write(":green[Las Monjas v3.6.0]")
    with tab2:
        pass
    with tab3:
        pass
    with tab4:
        pass

#1-3
def page3():
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
                
    with open("check_out_times.txt", "r", encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    # st.write(str(words_dict))
    word = st.text_input("请输入想要查询的单词：")
    
    if word:
        if word in words_dict:
            st.write(word)
            st.write(words_dict[word][1])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open("check_out_times.txt", "w", encoding="utf-8") as f:
                message = ""
                for k, v in times_dict.items():
                    message += str(k) + "#" + str(v) +"\n"
                message = message[:-1]
                f.write(message)
            st.write("查询次数：", times_dict[n])
            if word == "lasmonjas":
                st.snow()
            elif word == "aarondamn":
                st.balloons()
        else:
            st.write("未查询到该单词！请检查拼写是否有误！")



#1-4
def page4():
    st.write('------------------------------------------------------------')
    st.write("--------------------百度--------------------")
    st.link_button('点击跳转','https://www.baidu.com/')
    st.write("--------------------Bilibili--------------------")
    st.link_button('点击跳转','https://www.bilibili.com/')
    st.write("--------------------原神--------------------")
    st.link_button('点击跳转','https://ys.mihoyo.com/')
    st.write("--------------------AmongUs模组--------------------")
    st.link_button('点击跳转','https://amonguscn.club/')
    st.write("--------------------图片资源--------------------")
    st.link_button('点击跳转','https://www.gettyimages.com/')
    st.write("--------------------设计资源--------------------")
    st.link_button('点击跳转','https://www.qijishow.com/')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['贴吧', 'Bilibili','原神','AmongUs','图片大全','设计资源'])
    if go == '贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == 'Bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
    elif go == '原神':
        st.link_button('支持米哈游', 'https://ys.mihoyo.com/')
    elif go == 'AmongUs':
        st.link_button('AmongUs模组资源网站', 'https://amonguscn.club/')
    elif go == '图片大全':
        st.link_button('全世界最大的图片资源网站', 'https://www.gettyimages.com/')
    elif go == '设计资源':
        st.link_button('设计资源网站', 'https://www.qijishow.com/')

#1-5
def page5():
    st.write(":orange[有建议或者反馈请在下方留言]")
    tab1, tab2, tab3, tab4 = st.tabs(["原图","效果1","效果2","效果3"])
    uploaded_file = st.file_uploader("图片上传", type=["png","jpg","jpeg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
    with tab1:
        if uploaded_file:
            st.image(img)
    with tab2:
        if uploaded_file:
            st.image(img_change(img, 2, 0, 1))
    with tab3:
        if uploaded_file:
            st.image(img_change(img, 1, 2, 0))
    with tab4:
        if uploaded_file:
            st.image(img_change(img, 0, 1, 2))
        
def page6():
    st.write("留言区")
    with open("leave_messages.txt", "r", encoding="utf-8") as f:
        message_list = f.read().split("\n")
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split("#")
    for i in message_list:
        if i[1] == "阿短":
            with st.chat_message("🌞"):
                st.write(i[1],":",i[2])
        elif i[1] == "编程猫":
            with st.chat_message("☕"):
                st.write(i[1],":",i[2])
    name = st.selectbox("我是...",["阿短","编程猫"])
    new_message= st.text_input("想要说的话...")
    if st.button("留言"):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open("leave_messages.txt", "w", encoding="utf-8") as f:
            message = ""
            for i in message_list:
                message += i[0] +"#" + i[1] +"#" + i[2] +"\n"
            message = message[:-1]
            f.write(message)

def page7():
    st.write("下面哪个小程序可以嵌入网页中？")
    col1, col2 = st.columns([1,1])
    col3, col4 = st.columns([1,1])
    with col1:
        cb1 = st.checkbox("A")
    with col2:
        cb2 = st.checkbox("B")
    with col3:
        cb3 = st.checkbox("C")
    with col4:
        cb4 = st.checkbox("D")
    b1 = st.button("提交答案") 
    if b1:
        if cb1 == False and cb2 == True and cb3 == False and cb4 == False:
            st.write("Correct!")
        else:
            st.write("Wrong!")

def page8():
    st.write("1.您对本网页资源配置的满意程度")
    col1, col2 = st.columns([1,1])
    col3, col4 = st.columns([1,1])
    with col1:
        cb1 = st.checkbox("A.非常满意")
    with col2:
        cb2 = st.checkbox("B.满意")
    with col3:
        cb3 = st.checkbox("C.一般")
    with col4:
        cb4 = st.checkbox("D.不满意")
    st.write("--------------------------------------------------------------------------------------------------------------")
    st.write("2.您对本网页服务质量的满意程度")
    col5, col6 = st.columns([1,1])
    col7, col8 = st.columns([1,1])
    with col5:
        cb5 = st.checkbox("A.非常满意")
    with col6:
        cb6 = st.checkbox("B.满意")
    with col7:
        cb7 = st.checkbox("C.一般")
    with col8:
        cb8 = st.checkbox("D.不满意")
    st.write("--------------------------------------------------------------------------------------------------------------")
    b1 = st.button("提交反馈")
    if b1:
        st.write("提交成功！")

if page == "简介":
    page1()
elif page == "汉化作品":
    page2()
elif page == "英汉词典":
    page3()
elif page == "赞助区":
    page4()
elif page == "照片处理":
    page5()
elif page == "留言区":
    page6()
elif page == "每日一问":
    page7()
elif page == "问卷调查":
    page8()
