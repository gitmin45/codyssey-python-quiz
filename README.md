# Python 콘솔 퀴즈 게임

## 1. 프로젝트 개요

Python을 활용하여 제작한 콘솔 기반 객관식 퀴즈 게임입니다.

사용자는 화면에 표시되는 객관식 문제를 풀고, 새로운 퀴즈를 추가하거나 등록된 퀴즈 목록을 확인할 수 있습니다. 퀴즈 데이터와 최고 점수는 JSON 파일에 저장되어 프로그램을 다시 실행해도 유지됩니다.

## 2. 주제 선정 이유

Python의 기본 문법과 객체지향 프로그래밍을 학습하고, 이를 실제로 활용할 수 있는 프로젝트를 만들기 위해 퀴즈 게임을 주제로 선정했습니다.

특히 클래스, 반복문, 조건문, 리스트, 사용자 입력 처리, 파일 입출력 및 JSON 데이터 관리 등 Python의 핵심 기능을 직접 구현하고 연습하는 데 목적이 있습니다.

## 3. 개발 환경

| 항목 | 사용 기술 |
|---|---|
| 운영체제 | Windows 11 / WSL Ubuntu |
| 프로그래밍 언어 | Python 3.14.4 |
| 버전 관리 | Git |
| 원격 저장소 | GitHub |
| 데이터 저장 | JSON |
| 편집 도구 | Visual Studio Code |

## 4. 주요 기능

### 퀴즈 풀기
- 등록된 객관식 문제 출제
- 사용자 답변 입력 및 정답 확인
- 전체 문제에 대한 점수 계산
- 최고 점수 갱신 및 저장

### 퀴즈 추가
- 새로운 질문 입력
- 객관식 선택지 4개 등록
- 정답 번호 입력 및 검증
- 추가한 문제를 JSON 파일에 저장

### 퀴즈 목록 및 점수 확인
- 등록된 퀴즈 전체와 질문·선택지 확인
- 현재까지 기록된 최고 점수 확인

### 데이터 저장 및 불러오기
- JSON 파일을 이용한 퀴즈 데이터 관리
- 프로그램 재실행 시 기존 퀴즈와 최고 점수 불러오기

## 5. 프로젝트 파일 구조

```text
codyssey-python-quiz/
├── .gitignore
├── README.md
├── main.py
├── state.json
└── screenshots/
    └── 개발 및 실행 과정 캡처 이미지
```

| 파일 및 폴더 | 설명 |
|---|---|
| `.gitignore` | Git 버전 관리에서 제외할 파일 및 폴더 설정 |
| `README.md` | 프로젝트 소개 및 사용 방법 설명 |
| `main.py` | 퀴즈 게임의 전체 실행 프로그램 |
| `state.json` | 퀴즈 문제와 최고 점수 데이터 저장 |
| `screenshots/` | 개발 및 실행 과정의 화면 캡처 보관 |

## 6. 클래스 구성

### `Quiz` 클래스
퀴즈 한 문제의 정보를 관리합니다.
- 질문(`question`)
- 선택지(`choices`)
- 정답(`answer`)
- 문제 및 선택지 출력
- 사용자 답변의 정답 여부 확인

### `QuizGame` 클래스
퀴즈 게임 전체 기능을 관리합니다.
- 퀴즈 데이터 불러오기
- 메뉴 출력 및 실행
- 퀴즈 출제 및 채점
- 새로운 퀴즈 추가
- 퀴즈 목록 표시
- 최고 점수 관리
- JSON 파일 저장

## 7. 데이터 파일 설명

`state.json` 파일은 퀴즈와 최고 점수를 저장하는 JSON 형식의 데이터 파일입니다.

```json
{
    "best_score": 6,
    "quizzes": [
        {
            "question": "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
            "choices": ["input()", "print()", "open()", "type()"],
            "answer": 2
        }
    ]
}
```

- `best_score`: 현재까지의 최고 점수
- `quizzes`: 퀴즈 문제 목록
- `question`: 질문 내용
- `choices`: 객관식 선택지
- `answer`: 정답 번호(1~4)

## 8. 실행 방법

① 프로젝트 폴더로 이동

```bash
cd ~/codyssey-python-quiz
```

② Python 버전 확인

```bash
python3 --version
```

③ 프로그램 실행

```bash
python3 main.py
```

④ 프로그램 메뉴

```text
===== Python 퀴즈 게임 =====
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

원하는 메뉴 번호를 입력하여 기능을 사용할 수 있습니다.

## 9. 프로젝트 진행 및 학습 내용

이번 프로젝트를 통해 다음 내용을 학습하고 실습했습니다.
- Python 클래스와 객체 생성
- 조건문과 반복문 활용
- 리스트 및 문자열 처리
- 사용자 입력값 검증
- JSON 파일 읽기 및 쓰기
- Git 저장소 생성 및 커밋
- 기능별 브랜치 관리
- GitHub 원격 저장소 활용
- Pull Request 생성 및 `main` 브랜치 병합
- `git checkout`, `git pull`, `git clone` 명령 실습

## 10. 프로그램 실행 및 테스트 결과

다음 항목을 실제 실행하여 정상 동작을 확인했습니다.

| 테스트 항목 | 테스트 결과 |
|---|---|
| Python 프로그램 실행 | 정상 실행 |
| 퀴즈 목록 확인 | 6개 문제 출력 확인 |
| 퀴즈 추가 | 신규 문제 추가 및 저장 확인 |
| 퀴즈 풀기 | 6문제 정답 처리 확인 |
| 점수 계산 | 6점 획득 확인 |
| 최고 점수 갱신 | 최고 점수 6점 저장 확인 |
| JSON 데이터 저장 | `state.json` 저장 확인 |
| 프로그램 재실행 | 퀴즈 6개 및 최고 점수 6점 불러오기 확인 |
| GitHub 병합 | Pull Request #1을 `main`에 병합 확인 |
| 원격 저장소 동기화 | `git pull origin main` 실행 확인 |
| 저장소 복제 | `git clone`으로 별도 폴더에 복제 확인 |

테스트 결과, 퀴즈 데이터와 최고 점수가 JSON 파일에 정상적으로 저장되며 프로그램을 다시 실행해도 유지되는 것을 확인했습니다. GitHub의 기능 브랜치를 Pull Request로 `main`에 병합하고, 로컬 저장소에서 최신 내용을 가져오는 과정도 확인했습니다.

## 11. 개발 및 실행 증빙 스크린샷

아래 이미지는 `screenshots/` 폴더에 보관된 실제 작업 캡처입니다. GitHub에서 README 이미지가 표시되도록 상대 경로로 연결했습니다.

### 11-1. 개발 환경 및 Git 저장소 준비

**Python 및 Git 개발 환경 확인 — `01_environment.png`**

![Python 및 Git 개발 환경](screenshots/01_environment.png)

**Git 사용자 정보 설정 — `02_git_config.png.png`**

![Git 사용자 정보 설정](screenshots/02_git_config.png.png)

**GitHub 원격 저장소 생성 — `03_github_repository.png`**

![GitHub 원격 저장소 생성](screenshots/03_github_repository.png)

### 11-2. 프로젝트 및 기능 브랜치 구성

**기능 브랜치 생성 및 Git 작업 확인 — `05_feature_branch.png`**

![기능 브랜치 생성](screenshots/05_feature_branch.png)

**VS Code 작업공간 — `09_vscode_workspace.png`**

![VS Code 작업공간](screenshots/09_vscode_workspace.png)

**main.py 코드 작성 — `10_main_py_editor.png`**

![main.py 코드](screenshots/10_main_py_editor.png)

**Quiz 클래스 구현 — `08_quiz_class.png`**

![Quiz 클래스](screenshots/08_quiz_class.png)

**Quiz 클래스 테스트 — `11_quiz_class_test.png`**

![Quiz 클래스 테스트](screenshots/11_quiz_class_test.png)

**QuizGame 데이터 불러오기 테스트 — `12_quizgame_load_test.png`**

![QuizGame 데이터 불러오기](screenshots/12_quizgame_load_test.png)

### 11-3. 데이터 처리 및 오류 수정

**JSON 데이터 검증 — `07_json_validation.png`**

![JSON 데이터 검증](screenshots/07_json_validation.png)

**들여쓰기 오류 점검 — `12_indentation_error_check.png`**

![들여쓰기 오류 점검](screenshots/12_indentation_error_check.png)

**JSON 데이터 복구 — `12_state_json_recovery.png`**

![JSON 데이터 복구](screenshots/12_state_json_recovery.png)

**퀴즈 데이터 재불러오기 — `13_quiz_reload_success.png`**

![퀴즈 데이터 재불러오기](screenshots/13_quiz_reload_success.png)

**최고 점수 유지 확인 — `14_best_score_persistence.png`**

![최고 점수 유지](screenshots/14_best_score_persistence.png)

### 11-4. 퀴즈 기능 실행 결과

**퀴즈 프로그램 메뉴 — `06_quiz_menu.png`**

![퀴즈 프로그램 메뉴](screenshots/06_quiz_menu.png)

**퀴즈 목록 화면 — `07_quiz_list.png`**

![퀴즈 목록 화면](screenshots/07_quiz_list.png)

**메뉴 입력 흐름 수정 및 복구 — `09_quiz_menu_recovery.png`**

![메뉴 입력 흐름 복구](screenshots/09_quiz_menu_recovery.png)

**퀴즈 실행 화면 — `06_quiz_execution.png`**

![퀴즈 실행 화면](screenshots/06_quiz_execution.png)

**퀴즈 추가 코드 — `17_add_quiz_code.png`**

![퀴즈 추가 코드](screenshots/17_add_quiz_code.png)

**퀴즈 추가 결과 — `18_add_quiz_result.png`**

![퀴즈 추가 결과](screenshots/18_add_quiz_result.png)

**퀴즈 목록 갱신 — `19_quiz_list_updated.png`**

![퀴즈 목록 갱신](screenshots/19_quiz_list_updated.png)

**JSON 파일 저장 결과 — `20_quiz_json_saved.png`**

![JSON 저장 결과](screenshots/20_quiz_json_saved.png)

**퀴즈 풀이 및 점수 결과 — `21_quiz_play.png`**

![퀴즈 풀이 결과](screenshots/21_quiz_play.png)

### 11-5. GitHub 커밋 및 병합 과정

**GitHub 커밋 이력 — `22_github_history.png`**

![GitHub 커밋 이력](screenshots/22_github_history.png)

**로컬 README 편집 화면 — `23_README.md.png`**

![로컬 README 편집](screenshots/23_README.md.png)

**GitHub README 표시 화면 — `24_README.png`**

![GitHub README](screenshots/24_README.png)

**Pull Request 생성 — `25_pull_request.png`**

![Pull Request 생성](screenshots/25_pull_request.png)

**Pull Request 병합 완료 — `26_pull_request_merged.png`**

![Pull Request 병합 완료](screenshots/26_pull_request_merged.png)

**로컬 main 브랜치 전환 — `27_checkout_main.png`**

![main 브랜치 전환](screenshots/27_checkout_main.png)

**git pull 및 커밋 그래프 확인 — `28_git_pull_log.png`**

![git pull 및 커밋 그래프](screenshots/28_git_pull_log.png)

**GitHub 저장소 clone — `29_git_clone.png`**

![GitHub 저장소 clone](screenshots/29_git_clone.png)

**추가 Git clone 과정 캡처 — `04_git_clone.png`**

![Git clone 과정](screenshots/04_git_clone.png)

## 12. 향후 개선 방향

- 무작위 퀴즈 출제 기능
- 출제 문제 수 선택 기능
- 퀴즈 힌트 제공
- 등록된 퀴즈 삭제 기능
- 점수 기록 관리 기능

---

- **프로젝트명:** `codyssey-python-quiz`
- **프로젝트 유형:** Python 콘솔 기반 객관식 퀴즈 게임
- **개발 목적:** Python 기초 문법 및 Git/GitHub 활용 실습
- **GitHub 저장소:** https://github.com/gitmin45/codyssey-python-quiz
