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

        with open(self.state_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.best_score = data.get("best_score", 0)

        for item in data.get("quizzes", []):
            quiz = Quiz(
                item["question"],
                item["choices"],
                item["answer"]
            )
            self.quizzes.append(quiz)

        print(f"퀴즈 {len(self.quizzes)}개를 불러왔습니다.")
        print(f"현재 최고 점수: {self.best_score}")
    
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

        with open(self.state_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("퀴즈 데이터가 저장되었습니다.")
        
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
    game = QuizGame()
    game.run()
