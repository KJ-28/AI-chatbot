import logging
from openai import OpenAI
from config import API_KEY, MODEL_NAME
from database import save_message, load_history,save_memory
from pipeline import run_pipeline


# 创建AI客户端

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)




# AI回答函数
def ai_answer(question):

    # ========= 第一步 =========
    # 先把用户的问题保存到数据库
    try:

        save_message("user", question)

    except Exception as e:

        logging.error(
            f"保存用户消息失败：{type(e).__name__} - {e}"
        )


    # ========= 第二步 =========
    # 从数据库读取完整聊天记录
    try:

        history = load_history()

    except Exception as e:

        logging.error(
            f"读取聊天记录失败：{type(e).__name__} - {e}"
        )

        history = []


    # ========= 第三步 =========
    # 把聊天记录发送给ds
    try:
        prompt = run_pipeline(question)
        response = client.chat.completions.create(

            model=MODEL_NAME,
            
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ] + history,

            stream=True
        )


    except Exception as e:

        logging.error(
            f"DeepSeek API调用失败：{type(e).__name__} - {e}"
        )
        print("KK：抱歉，AI服务暂时不可用")

        return ""


    # ========= 第四步 =========
    # 获取AI回答
    answer = ""
    print("KK:", end="")
    for chunk in response:

        content = chunk.choices[0].delta.content

        if content:

            print(content, end="", flush=True)

            answer += content
    print()  # 换行


    # ========= 第五步 =========
    # 把AI回答保存到数据库
    try:

        save_message("assistant", answer)


    except Exception as e:

        logging.error(
            f"保存聊天记录失败：{type(e).__name__} - {e}"
        )
    # ========= 第六步 =========
    # 返回AI回答
    return answer



def ai_stream(question):

    # 保存用户消息
    try:
        save_message("user", question)
    except Exception as e:
        logging.error(
            f"保存用户消息失败：{type(e).__name__} - {e}"
        )


    # 获取历史
    try:
        history = load_history()
    except Exception as e:
        logging.error(
            f"读取历史失败：{type(e).__name__} - {e}"
        )
        history = []


    # 调用模型
    try:
        prompt = run_pipeline(question)
        response = client.chat.completions.create(
            model=MODEL_NAME,
            
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ] + history,
            stream=True
        )

    except Exception as e:

        logging.error(
            f"DeepSeek Streaming调用失败：{type(e).__name__} - {e}"
        )

        yield "抱歉，AI服务暂时不可用"

        return


    answer = ""

    for chunk in response:

        content = chunk.choices[0].delta.content

        if content:

            answer += content

            yield content


    # 保存AI回答
    try:

        save_message("assistant", answer)

    except Exception as e:

        logging.error(
            f"保存AI回答失败：{type(e).__name__} - {e}"
        )