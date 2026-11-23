import json

class Quiz:
    """퀴즈 한 문제의 정보를 관리하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        """질문과 선택지를 화면에 출력한다."""
        print("\n" + self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        """사용자가 입력한 답이 정답인지 확인한다."""
        return user_answer == self.answer

class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.state_file = "state.json"
        self.best_score = 0
        self.quizzes = []

        self.load_data()

    def load_data(self):
        """JSON 파일에서 퀴즈 데이터를 읽어온다."""

        # 기본 퀴즈 데이터
        default_data = {
            "best_score": 0,
            "quizzes": [
                {
                    "question": "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
                    "choices": ["input()", "print()", "open()", "type()"],
                    "answer": 2
                },
                {
                    "question": "Python에서 문자열을 나타내는 자료형은?",
                    "choices": ["int", "float", "str", "bool"],
                    "answer": 3
                },
                {
                    "question": "반복문에서 사용하는 키워드는?",
                    "choices": ["if", "for", "def", "class"],
                    "answer": 2
                },
                {
                    "question": "리스트를 만들 때 사용하는 괄호는?",
                    "choices": ["( )", "{ }", "[ ]", "< >"],
                    "answer": 3
                },
                {
                    "question": "Python에서 함수를 정의할 때 사용하는 키워드는?",
                    "choices": ["make", "function", "def", "return"],
                    "answer": 3
                },
                {
                    "question": "Python에서 주석을 나타내는 기호는?",
                    "choices": ["//", "#", "/*", "--"],
                    "answer": 2
                }
            ]
        }

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("JSON 데이터 형식이 올바르지 않습니다.")

            if not isinstance(data.get("quizzes"), list):
                raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

            best_score = data.get("best_score", 0)

            if type(best_score) is not int or best_score < 0:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            self.best_score = best_score
            self.quizzes = []

            for item in data["quizzes"]:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 항목의 형식이 올바르지 않습니다.")

                question = item.get("question")
                choices = item.get("choices")
                answer = item.get("answer")

                # 질문 데이터 검증
                if not isinstance(question, str) or not question.strip():
                    raise ValueError("질문 내용이 비어 있거나 올바르지 않습니다.")

                # 선택지 데이터 검증
                if not isinstance(choices, list) or len(choices) != 4:
                    raise ValueError("선택지는 반드시 4개여야 합니다.")

                if not all(
                    isinstance(choice, str) and choice.strip()
                    for choice in choices
                ):
                    raise ValueError("선택지 내용이 비어 있거나 올바르지 않습니다.")

                # 정답 번호 검증
                if type(answer) is not int or not 1 <= answer <= 4:
                    raise ValueError("정답 번호는 1부터 4까지의 숫자여야 합니다.")

                quiz = Quiz(question, choices, answer)
                self.quizzes.append(quiz)

            print(f"퀴즈 {len(self.quizzes)}개를 불러왔습니다.")
            print(f"현재 최고 점수: {self.best_score}")

        except FileNotFoundError:
            print("데이터 파일이 없습니다. 기본 퀴즈를 생성합니다.")
            self.best_score = default_data["best_score"]
            self.quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in default_data["quizzes"]
            ]
            self.save_data()

        except (json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
            print(f"데이터 파일에 문제가 있습니다: {error}")
            print("기본 퀴즈 데이터로 초기화합니다.")

            self.best_score = default_data["best_score"]
            self.quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in default_data["quizzes"]
            ]
            self.save_data()

        except OSError as error:
            print(f"데이터 파일을 읽을 수 없습니다: {error}")
            print("기본 퀴즈 데이터로 실행합니다.")

            self.best_score = default_data["best_score"]
            self.quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in default_data["quizzes"]
            ]
    
    def run(self):
        """퀴즈 게임 메뉴를 실행한다."""
        while True:
            print("\n===== Python 퀴즈 게임 =====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            choice = input("메뉴를 선택하세요: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                print("\n===== 퀴즈 목록 =====")

                if not self.quizzes:
                    print("등록된 퀴즈가 없습니다.")
                else:
                    for number, quiz in enumerate(self.quizzes, start=1):
                        print(f"\n[{number}] {quiz.question}")

                        for choice_number, choice_text in enumerate(
                            quiz.choices, start=1
                        ):
                            print(f"  {choice_number}. {choice_text}")

                print(f"\n총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")

            elif choice == "4":
                print(f"현재 최고 점수: {self.best_score}")
            elif choice == "5":
                print("퀴즈 게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 숫자를 입력해 주세요.")
                
    def add_quiz(self):
        """새로운 퀴즈를 입력받아 저장한다."""

        print("\n===== 퀴즈 추가 =====")

        # 1. 질문 입력
        while True:
            question = input("질문을 입력하세요: ").strip()

            if question:
                break

            print("질문은 비워둘 수 없습니다. 다시 입력해 주세요.")

        # 2. 선택지 4개 입력
        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"선택지 {number}을 입력하세요: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("선택지는 비워둘 수 없습니다. 다시 입력해 주세요.")

        # 3. 정답 번호 입력 및 검증
        while True:
            answer_input = input("정답 번호를 입력하세요 (1~4): ").strip()

            try:
                answer = int(answer_input)

                if 1 <= answer <= 4:
                    break

                print("1부터 4까지의 숫자를 입력해 주세요.")

            except ValueError:
                print("숫자로 입력해 주세요.")

        # 4. Quiz 객체 생성 및 목록에 추가
        quiz = Quiz(question, choices, answer)
        self.quizzes.append(quiz)

        # 5. JSON 파일에 저장
        self.save_data()

        print("새로운 퀴즈가 추가되었습니다!")
        
    def save_data(self):
        """퀴즈 데이터와 최고 점수를 JSON 파일에 저장한다."""
        data = {
            "best_score": self.best_score,
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ]
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("퀴즈 데이터가 저장되었습니다.")

        except OSError as error:
            print(f"데이터 파일 저장 중 오류가 발생했습니다: {error}")

        except TypeError as error:
            print(f"저장할 데이터 형식에 문제가 있습니다: {error}")

        
    def play_quiz(self):
        """등록된 퀴즈를 풀고 점수를 계산한다."""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print("\n===== 퀴즈 풀기 시작 =====")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{number}/{len(self.quizzes)}]")
            quiz.display()

            while True:
                user_input = input("정답 번호를 입력하세요 (1~4): ").strip()

                try:
                    user_answer = int(user_input)
                except ValueError:
                    print("숫자로 입력해 주세요.")
                    continue

                if user_answer < 1 or user_answer > len(quiz.choices):
                    print(f"1~{len(quiz.choices)} 사이의 숫자를 입력하세요.")
                    continue

                break

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n===== 퀴즈 결과 =====")
        print(f"총 문제 수: {len(self.quizzes)}")
        print(f"정답 수: {score}")
        print(f"오답 수: {len(self.quizzes) - score}")

        if score > self.best_score:
            self.best_score = score
            self.save_data()
            print("축하합니다! 최고 점수가 갱신되었습니다.")

        print(f"이번 점수: {score}점")
        print(f"최고 점수: {self.best_score}점")

        self.save_data()
        

if __name__ == "__main__":
    try:
        game = QuizGame()
        game.run()

    except KeyboardInterrupt:
        print("\n\n사용자 요청으로 프로그램을 안전하게 종료합니다.")

    except EOFError:
        print("\n\n입력이 종료되어 프로그램을 안전하게 종료합니다.")
