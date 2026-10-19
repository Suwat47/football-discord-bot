name: Run Football Bot Daily

on:
  schedule:
    # ตั้งเวลารันอัตโนมัติทุกลีก ทุกวัน ตอน 12:00 น. และ 18:00 น. (เวลาไทย)
    - cron: '0 5,11 * * *'
  workflow_dispatch: # ปุ่มสำหรับกดสั่งรันด้วยตัวเองได้ตลอดเวลา

jobs:
  run-python-script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          pip install requests numpy scipy

      - name: Execute Bot
        run: python bot.py
