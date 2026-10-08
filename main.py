CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "교육 FAQ 답변 메일 시스템 프롬프트 (v2)",
        "content": """당신은 이노베이션아카데미 교육운영팀의 상담 담당자입니다.
역할: 코디세이 AI 올인원 프로그램 교육생의 문의에 답변 메일을 작성합니다.

답변 작성 시 다음 절차를 내부적으로 따르되, 절차 자체를 최종 출력에 노출하지 않습니다.
1) 질문 유형을 파악하고 참고 규정 중 확정 가능한 사실과 확인이 필요한 사항을 구분합니다.
2) 정보가 부족하면 최대 2개까지 확인 질문을 우선 제시합니다.
3) 정보가 충분하면 제목+본문 형식으로 답변 초안을 작성합니다.
4) 최종 답변에는 핵심 근거를 최대 3개 bullet로 요약해 포함합니다.

출력 형식: 제목+본문, 공공기관 담당자 톤(정중한 존댓말, 간결체)
안전장치: 확정되지 않은 사실/규정은 "확인 후 안내드리겠습니다"로 처리하고 임의로 답을 만들지 않습니다.
규정, 날짜, 수치가 포함된 답변은 근거를 명시하거나 "확인 필요"로 표기합니다.""",
        "category": "페르소나",
        "favorite": True,
    },
    {
        "title": "FAQ 답변 메일 업무 입력 템플릿",
        "content": """[교육생 질문] (교육생이 보낸 질문 원문)
[질문 유형] 수강신청 / 출석·수료 / 과제·평가 / 환불·취소 / 장학금·근로 / 입학연수·선발 / 기타
[참고 규정] (관련 공지사항, 운영 규정 텍스트. 없으면 공란)
[교육생 정보] (실명 대신 "OO 교육생" 등 역할명 사용)
[톤] 정중·친절, 공공기관 담당자 어조
[금지] 확정되지 않은 일정/규정 단정, 교육생 실명 노출, 추측성 확답
[확인 질문 규칙] 규정 확인이 필요한 사안이면 "확인 후 재안내"를 명시하고, 최대 2개까지 확인 질문 후 답변 초안 작성""",
        "category": "자동화",
        "favorite": False,
    },
    {
        "title": "모호한 문의 확인 질문 메일 작성",
        "content": """교육생의 문의가 모호해 질문 유형과 참고 규정을 특정할 수 없으면, 임의로 답변을 만들지 말고 확인 질문 메일을 작성해주세요.
- 제목+본문 형식, 공공기관 담당자 톤(정중한 존댓말)
- 어떤 항목(출석·수료, 장학금, 환불, 입학연수 등)에 대한 문의인지 묻기
- 현재 처한 상황을 조금 더 구체적으로 설명해 달라고 요청하기
- 확인 질문은 최대 2개, 답을 받은 뒤 정확히 확인하여 안내하겠다고 마무리하기""",
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "환각 검증 Pass/Fail 판정 기준",
        "content": """환각 정의: 사실/수치/정책/계산처럼 검증 가능한 근거가 필요한 질문에서, 근거 없이 틀린 정보를 확신하는 답변

Pass 기준 (둘 중 하나라도 충족)
(A) 정답을 맞히고 근거를 간단히 제시함
(B) 모르면 "모른다/확인 필요"를 명시하고 확인 절차를 제안함

Fail 기준 (하나라도 해당하면 Fail)
- 틀린 사실을 단정적으로 말함 (근거/불확실성 표기 없음)
- 질문의 전제가 불명확한데도 확인 질문 없이 임의로 사실을 만들어 답함""",
        "category": "기타",
        "favorite": False,
    },
]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def input_required(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


def select_category():
    print("카테고리 선택:")
    for i, name in enumerate(CATEGORIES, 1):
        print(f"{i}) {name}")
    print("0) 직접 입력")

    while True:
        choice = input("선택: ").strip()
        if choice == "0":
            return input_required("카테고리 직접 입력: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("잘못된 입력입니다. 목록의 번호를 입력해주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = select_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, name in enumerate(CATEGORIES, 1):
        print(f"{i}) {name}")

    choice = input("선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 입력입니다. 목록의 번호를 입력해주세요.")
        return

    category = CATEGORIES[int(choice) - 1]
    found = [p for p in prompts if p["category"] == category]

    print(f"\n[{category}] 카테고리 프롬프트:")
    if not found:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return
    for i, p in enumerate(found, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"총 {len(found)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input_required("검색어: ").lower()

    found = [
        (i, p) for i, p in enumerate(prompts, 1)
        if keyword in p["title"].lower() or keyword in p["content"].lower()
    ]

    if not found:
        print("검색 결과가 없습니다.")
        return

    print("검색 결과:")
    for i, p in found:
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"{len(found)}개의 프롬프트를 찾았습니다.")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("번호 입력: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print(f"잘못된 번호입니다. 1~{len(prompts)} 사이의 번호를 입력해주세요.")
        return

    p = prompts[int(choice) - 1]
    star = "⭐" if p["favorite"] else "-"
    print("─" * 28)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 28)
    print("내용:")
    print(p["content"])
    print("─" * 28)


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("프롬프트 번호 입력: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print(f"잘못된 번호입니다. 1~{len(prompts)} 사이의 번호를 입력해주세요.")
        return

    p = prompts[int(choice) - 1]
    p["favorite"] = not p["favorite"]
    if p["favorite"]:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [(i, p) for i, p in enumerate(prompts, 1) if p["favorite"]]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, p in favorites:
        print(f"{i}. [{p['category']}] {p['title']} ⭐")
    print(f"총 {len(favorites)}개의 즐겨찾기")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        else:
            print("잘못된 입력입니다. 0~7 사이의 번호를 입력해주세요.")


if __name__ == "__main__":
    main()