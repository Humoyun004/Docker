# Yaratoyotgan Doker Image ni, Python Imagedan Python:3.11 versiya sini base qilib olayapman.
FROM python:3.11-alpine

# Bu yerda 3ta muhut o'zgaruvchilari uchun, har biriga value ni kritib ketayapman.
ENV first_name="Humoyun"
ENV last_name="Akbaraliev"
ENV age='19'

# Konteyner ichida ishchi katalogni ornatayapman, komandalar barchasi manashuni ichida sodir bo'ladi.
WORKDIR /app

# main.py file ni container ichidagi ishchi kataloga ko'chirayaypman.
COPY main.py /app/

# Bu yerda main.py script ini Python orqali ishga tushurayapman, python interpretatoriga `main.py` attribute qilib berib ketayapman.
CMD ["python", "main.py"]

# Keyingi ish terminalda Image yaratib olish:
    # 1. docker build -t task2 .
    # 2. docker run task2
