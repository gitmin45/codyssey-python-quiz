import json
import os
import tempfile
import unittest
from unittest.mock import patch

from main import Quiz, QuizGame

class TestQuiz(unittest.TestCase):
    """Quiz 클래스의 정답 판별 기능을 테스트한다."""

    def test_check_answer_correct(self):
        quiz = Quiz("Python의 출력 함수는?", ["input()", "print()", "open()", "type()"], 2)

        self.assertTrue(quiz.check_answer(2))

    def test_check_answer_incorrect(self):
        quiz = Quiz("Python의 출력 함수는?", ["input()", "print()", "open()", "type()"], 2)

        self.assertFalse(quiz.check_answer(1))


class TestQuizGame(unittest.TestCase):
    """QuizGame의 JSON 저장 및 불러오기 기능을 테스트한다."""

    def test_save_and_load_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            state_path = os.path.join(temp_dir, "state.json")

            game = QuizGame.__new__(QuizGame)
            game.state_file = state_path
            game.best_score = 3
            game.quizzes = [
                Quiz("테스트 질문", ["보기1", "보기2", "보기3", "보기4"], 2)
            ]

            with patch("builtins.print"):
                game.save_data()

                loaded_game = QuizGame.__new__(QuizGame)
                loaded_game.state_file = state_path
                loaded_game.best_score = 0
                loaded_game.quizzes = []
                loaded_game.load_data()

            self.assertEqual(loaded_game.best_score, 3)
            self.assertEqual(len(loaded_game.quizzes), 1)
            self.assertEqual(loaded_game.quizzes[0].question, "테스트 질문")
            self.assertEqual(loaded_game.quizzes[0].answer, 2)

    def test_invalid_json_data_resets_to_defaults(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            state_path = os.path.join(temp_dir, "state.json")

            invalid_data = {
                "best_score": 0,
                "quizzes": [
                    {
                        "question": "잘못된 질문",
                        "choices": ["A", "B", "C", "D"],
                        "answer": 9
                    }
                ]
            }

            with open(state_path, "w", encoding="utf-8") as file:
                json.dump(invalid_data, file)

            game = QuizGame.__new__(QuizGame)
            game.state_file = state_path
            game.best_score = 0
            game.quizzes = []

            with patch("builtins.print"):
                game.load_data()

            self.assertEqual(len(game.quizzes), 6)
            self.assertTrue(all(1 <= quiz.answer <= 4 for quiz in game.quizzes))


if __name__ == "__main__":
    unittest.main()
