import random
import json

# 카테고리와 지역 샘플
categories = ["부동산", "형사", "민사", "가사", "노동", "기타"]
regions = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

# 변호사 이름 생성 도구
first_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황"]
second_names = ["민지", "서준", "하늘", "지우", "예린", "도윤", "유진", "시우", "채원", "지민", "태현", "서연", "우진", "다은", "현우", "예준"]

# 설명 템플릿 문장들
description_sentences = {
    "부동산": [
        "전세보증금 및 임대차 분쟁에 대한 풍부한 경험을 보유하고 있습니다.",
        "부동산 계약서 검토 및 등기 문제 해결이 가능합니다.",
        "건물 명도, 토지 분쟁 사건 다수 진행했습니다."
    ],
    "형사": [
        "형사사건 전반에 걸쳐 실무 경험이 많습니다.",
        "강력 사건, 성범죄, 명예훼손 사건 다수 처리했습니다.",
        "수사 초기 대응부터 재판까지 전과정 대응합니다."
    ],
    "민사": [
        "손해배상, 계약 위반, 채무불이행 사건 등 폭넓은 민사 경험 보유.",
        "민사소송 절차에 능통하며 신속한 해결을 도모합니다.",
        "분쟁 조정과 화해 유도로 원만한 해결을 지향합니다."
    ],
    "가사": [
        "이혼, 양육권, 위자료 등 가족법 관련 사건 전문.",
        "가정폭력 피해자 상담 및 법률 지원 경험 다수.",
        "민감한 사안에 공감하며 신중하고 정확하게 처리합니다."
    ],
    "노동": [
        "부당해고 및 임금체불 사건에 풍부한 해결 사례를 보유.",
        "직장 내 괴롭힘, 근로계약 관련 분쟁을 전문적으로 처리합니다.",
        "노동위원회 및 법원 대응까지 일관된 전략을 제공합니다."
    ],
    "기타": [
        "다양한 분야의 사건을 종합적으로 분석하고 대응합니다.",
        "의뢰인의 상황에 맞는 맞춤형 법률 서비스를 제공합니다.",
        "초기 상담부터 사후 관리까지 전 과정을 지원합니다."
    ]
}

# 생성
lawyers = []
for i in range(1000):
    selected_categories = random.sample(categories, k=3)  # 최소 3개 카테고리
    region = random.choice(regions)
    name = random.choice(first_names) + random.choice(second_names) + " 변호사"
    contact = f"010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    
    desc_lines = []
    for cat in selected_categories:
        desc_lines.extend(random.sample(description_sentences[cat], k=1))
    description = "\n".join(desc_lines)

    lawyers.append({
        "name": name,
        "categories": selected_categories,
        "region": region,
        "contact": contact,
        "description": description
    })

# 저장
file_path = "lawyers_1000_multi_category.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(lawyers, f, ensure_ascii=False, indent=2)

file_path
