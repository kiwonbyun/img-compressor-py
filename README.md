# 이미지 압축 프로그램

1. Repository Clone

2. 필수 소프트웨어 설치

   - **Python 설치**: 이 프로젝트를 실행하기 위해서는 Python이 설치되어 있어야 합니다. [Python 공식 사이트](https://www.python.org/downloads/)에서 Python을 다운로드하고 설치하세요.
   - 터미널에서 PyInstaller 설치:
     ```
     pip install pyinstaller
     ```

3. 실행파일로 만들기

   - 터미널에서 실행:
     ```
     pyinstaller --onefile --windowed image-compresser.py
     ```

4. dist 폴더에서 실행파일 실행
