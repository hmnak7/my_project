
from flask import Flask, render_template, url_for

app = Flask(__name__)

# --------- Portfolio Data (edit here) ---------
data = {
    "profile": {
        "name": "이현민",
        "title": "데이터 분석가",
        "bio": "파이썬, 엑셀, SQL을 활용해 데이터를 분석하고 시각화하는 것을 좋아합니다. 부트캠프에서 실전 프로젝트를 진행하며 성장하고 있어요.",
        "location": "Seoul, Korea",
        "email": "hmnak7@naver.com",
        "contact": "010-2429-7923",
        "github": "https://github.com/yourname",
        "linkedin": "https://www.linkedin.com/in/yourname"
    },
    "skills": [
        {"name": "Python", "level": 30},
        # {"name": "Pandas", "level": 80},
        {"name": "Excel (MOS Master)", "level": 90},
        # {"name": "SQL", "level": 70},
        # {"name": "Matplotlib", "level": 65},
        {"name": "Flask", "level": 60},
    ],
    "projects": [
        {
            "title": "출석률 캘린더 웹앱",
            "summary": "수업 출석 데이터를 달력으로 시각화하여 결석 패턴을 한눈에 파악.",
            "tags": ["Python", "Pandas", "시각화"],
            "link": "https://example.com/attendance-app",
            "image": "calendar.png"
        },
        {
            "title": "장바구니 리스트 CLI",
            "summary": "콘솔에서 항목 추가/삭제/조회가 가능한 장바구니 관리 프로그램.",
            "tags": ["Python"],
            "link": "https://example.com/cart-cli",
            "image": "cart.png"
        },
        {
            "title": "식료품 영수증 계산기",
            "summary": "품목별 금액 합계 및 할인 적용을 자동 계산하는 간단 앱.",
            "tags": ["Python"],
            "link": "https://example.com/grocery-receipt",
            "image": "receipt.png"
        }
    ],
    "experience": [
        {
            "company": "KRX 지원 준비",
            "role": "비서/데이터 지원",
            "period": "2025",
            "details": [
                "문서 자동화와 데이터 정리로 보고 효율 향상",
                "엑셀/파워포인트 템플릿 표준화 경험"
            ]
        }
    ],
    "education": [
        {
            "school": "인하공업전문대학 비서학과",
            "degree": "비서학 (MOS Master 포함)",
            "period": "—"
        },
        {
            "school": "국비지원 데이터 분석 부트캠프",
            "degree": "데이터 분석 과정",
            "period": "2025.06 — 진행중"
        }
    ]
}

# --------- Routes ---------
@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=data)

# Optional: simple resume/overview page
@app.route('/about')
def about():
    return render_template('about.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
