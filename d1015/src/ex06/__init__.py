"""대화 기억: 앞의 질문과 답을 messages 에 쌓아 함께 보낸다.

uv run python ex05_memory.py   (끝낼 때 /bye)
"""

import ollama

MODEL = "qwen3.5:9b"

def main():
    messages = [{
        "role": "system",
        # 학교 정보 출처: https://www.wku.ac.kr/ 및 /about/school-info/intro.html
        "content": (
            "한국어로 짧고 친절하게 답한다. 학교 질문에는 아래 원광대학교 정보를 참고한다.\n"
            "[원광대학교 기본 정보]\n"
            "- 학교명: 원광대학교(Wonkwang University, WKU).\n"
            "- 위치: 전북특별자치도 익산시에 있는 종합대학이다.\n"
            "- 개교: 1946년이며, 전신은 유일학림이다.\n"
            "- 주소: 우편번호 54538, 전북특별자치도 익산시 익산대로 460.\n"
            "- 교훈: 지덕겸수(지식과 덕성을 함께 닦음), 도의실천(도덕과 의리를 실천함).\n"
            "- 공식 홈페이지: https://www.wku.ac.kr/\n"
            "- 입학 안내: https://ipsi.wku.ac.kr/\n"
            "- 중앙도서관: https://elibrary.wku.ac.kr/\n"
            "등록금, 장학금, 입시 일정, 학사 일정 등 바뀔 수 있는 정보는 "
            "최신 공식 공지 확인을 안내한다. 제공된 정보에 없는 내용을 모르면 "
            "모른다고 답하고, 확인하지 않은 내용을 지어내지 않는다."
        ),
    }]

    print("앞의 질문과 답을 함께 보내 대화를 이어 갑니다. 종료: /bye")
    while True:
        text = input("나> ").strip()
        if text == "/bye":
            break
        if not text:
            continue
        messages.append({"role": "user", "content": text})
        request = messages  # 기억 끄기 비교: [messages[0], messages[-1]] (규칙과 이번 질문만)
        print(f"(보내는 메시지 {len(request)}개)")
        response = ollama.chat(model=MODEL, messages=request, think=False)
        answer = response.message.content or ""
        print("AI>", answer)
        messages.append({"role": "assistant", "content": answer})  # 답도 쌓아야 다음에 기억한다

if __name__ == "__main__":
    main()
