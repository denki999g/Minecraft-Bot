# 1. 파이썬 버전에 맞게 수정 (예: 3.11, 3.12)
FROM python:3.11-slim

# 2. uv 바이너리만 쏙 빼오기
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 3. 의존성 파일만 먼저 복사 (캐시 최적화)
# uv.lock이 없다면 명령어로 uv lock을 쳐서 생성해 주는 게 좋아!
COPY pyproject.toml uv.lock ./

# 4. 패키지 설치
RUN uv sync --frozen --no-dev --no-install-project

# 5. 내 파이썬 코드 전체 복사
COPY . .

# 6. 프로젝트 자체 설치 마무리
RUN uv sync --frozen --no-dev

# 7. 실행은 깔끔하게 uv run으로! (메인 파일명 맞춰서 수정)
CMD ["uv", "run", "main.py"]