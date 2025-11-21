"""
猜數字遊戲的單元測試 (Unit Tests for Guess Number Game)

使用 Python 的 unittest 模組，對遊戲的主要判斷邏輯建立多組測試案例，
驗證每個輸入會得到正確的回應。
"""

import unittest
from guess_number_game import GuessNumberGame, guess_number


class TestGuessNumberFunction(unittest.TestCase):
    """測試 guess_number 函數的基本判斷邏輯"""
    
    def test_guess_too_small(self):
        """測試猜測數字太小的情況"""
        # assert 用來判斷程式執行結果是否符合預期
        self.assertEqual(guess_number(5, 3), "太小")
        self.assertEqual(guess_number(100, 50), "太小")
        self.assertEqual(guess_number(10, 1), "太小")
    
    def test_guess_too_big(self):
        """測試猜測數字太大的情況"""
        self.assertEqual(guess_number(5, 10), "太大")
        self.assertEqual(guess_number(50, 100), "太大")
        self.assertEqual(guess_number(1, 10), "太大")
    
    def test_guess_correct(self):
        """測試猜測正確的情況"""
        self.assertEqual(guess_number(5, 5), "正確")
        self.assertEqual(guess_number(100, 100), "正確")
        self.assertEqual(guess_number(1, 1), "正確")
    
    def test_invalid_input_non_integer(self):
        """測試無效輸入（非整數）"""
        self.assertEqual(guess_number("5", 3), "錯誤：請輸入整數")
        self.assertEqual(guess_number(5, "3"), "錯誤：請輸入整數")
        self.assertEqual(guess_number(5.5, 3), "錯誤：請輸入整數")
    
    def test_edge_cases(self):
        """測試邊界情況"""
        # 測試負數
        self.assertEqual(guess_number(-10, -15), "太小")
        self.assertEqual(guess_number(-10, -5), "太大")
        self.assertEqual(guess_number(-10, -10), "正確")
        
        # 測試零
        self.assertEqual(guess_number(0, -1), "太小")
        self.assertEqual(guess_number(0, 1), "太大")
        self.assertEqual(guess_number(0, 0), "正確")


class TestGuessNumberGame(unittest.TestCase):
    """測試 GuessNumberGame 類別的完整功能"""
    
    def setUp(self):
        """在每個測試前執行，設置測試環境"""
        # 創建一個固定目標數字的遊戲實例用於測試
        self.game = GuessNumberGame(1, 100)
    
    def test_initialization(self):
        """測試遊戲初始化"""
        game = GuessNumberGame(1, 100)
        self.assertEqual(game.min_number, 1)
        self.assertEqual(game.max_number, 100)
        self.assertEqual(game.attempts, 0)
        self.assertFalse(game.game_over)
        # 確認目標數字在範圍內
        self.assertTrue(1 <= game.target_number <= 100)
    
    def test_guess_within_range(self):
        """測試在範圍內的猜測"""
        # 設定目標數字為 50
        self.game.target_number = 50
        
        # 測試猜太小
        result = self.game.guess(25)
        self.assertEqual(result, "太小")
        self.assertEqual(self.game.attempts, 1)
        
        # 測試猜太大
        result = self.game.guess(75)
        self.assertEqual(result, "太大")
        self.assertEqual(self.game.attempts, 2)
        
        # 測試猜正確
        result = self.game.guess(50)
        self.assertEqual(result, "正確")
        self.assertEqual(self.game.attempts, 3)
        self.assertTrue(self.game.game_over)
    
    def test_guess_out_of_range(self):
        """測試超出範圍的猜測"""
        result = self.game.guess(0)
        self.assertIn("請輸入", result)
        
        result = self.game.guess(101)
        self.assertIn("請輸入", result)
        
        result = self.game.guess(-5)
        self.assertIn("請輸入", result)
    
    def test_invalid_input_type(self):
        """測試無效的輸入類型"""
        result = self.game.guess("50")
        self.assertEqual(result, "請輸入整數")
        
        result = self.game.guess(50.5)
        self.assertEqual(result, "請輸入整數")
        
        result = self.game.guess(None)
        self.assertEqual(result, "請輸入整數")
    
    def test_game_over_state(self):
        """測試遊戲結束狀態"""
        self.game.target_number = 50
        
        # 猜對後遊戲結束
        self.game.guess(50)
        self.assertTrue(self.game.game_over)
        
        # 遊戲結束後不能再猜
        result = self.game.guess(25)
        self.assertEqual(result, "遊戲已結束")
    
    def test_attempts_counter(self):
        """測試嘗試次數計數"""
        # 設定目標數字，確保測試結果可預測
        self.game.target_number = 60
        
        self.assertEqual(self.game.get_attempts(), 0)
        
        self.game.guess(50)
        self.assertEqual(self.game.get_attempts(), 1)
        
        self.game.guess(75)
        self.assertEqual(self.game.get_attempts(), 2)
        
        self.game.guess(25)
        self.assertEqual(self.game.get_attempts(), 3)
    
    def test_reset_game(self):
        """測試遊戲重置功能"""
        # 玩一輪遊戲
        self.game.target_number = 50
        self.game.guess(25)
        self.game.guess(50)
        
        # 重置遊戲
        self.game.reset()
        
        # 確認狀態已重置
        self.assertEqual(self.game.attempts, 0)
        self.assertFalse(self.game.game_over)
        self.assertTrue(1 <= self.game.target_number <= 100)
    
    def test_custom_range(self):
        """測試自訂數字範圍"""
        game = GuessNumberGame(50, 150)
        self.assertEqual(game.min_number, 50)
        self.assertEqual(game.max_number, 150)
        self.assertTrue(50 <= game.target_number <= 150)
    
    def test_multiple_games(self):
        """測試多個遊戲實例互不影響"""
        game1 = GuessNumberGame(1, 10)
        game2 = GuessNumberGame(1, 10)
        
        # 設定不同的目標數字
        game1.target_number = 5
        game2.target_number = 8
        
        # 確認各自獨立運作
        self.assertEqual(game1.guess(5), "正確")
        self.assertFalse(game2.game_over)
        self.assertEqual(game2.guess(8), "正確")


class TestAssertExamples(unittest.TestCase):
    """展示 assert 指令的各種用法和最佳實踐"""
    
    def test_assert_equality(self):
        """assert 最基本的用法：判斷相等性"""
        # assertEqual 是 assert 的一種，用來確保兩個值相等
        result = guess_number(10, 5)
        self.assertEqual(result, "太小")
        
        # 這確保函數輸出符合預期，及早發現錯誤
        result = guess_number(10, 15)
        self.assertEqual(result, "太大")
    
    def test_assert_true_false(self):
        """assert 判斷布林值"""
        game = GuessNumberGame(1, 100)
        
        # assertTrue 和 assertFalse 用來檢查布林條件
        self.assertFalse(game.game_over)
        
        game.target_number = 50
        game.guess(50)
        self.assertTrue(game.game_over)
    
    def test_assert_in_collection(self):
        """assert 檢查元素是否在集合中"""
        valid_responses = ["太小", "太大", "正確"]
        result = guess_number(10, 5)
        
        # assertIn 確保結果是預期的選項之一
        self.assertIn(result, valid_responses)
    
    def test_assert_greater_less(self):
        """assert 比較大小"""
        game = GuessNumberGame(1, 100)
        
        # assertGreaterEqual 和 assertLessEqual 用於數值比較
        self.assertGreaterEqual(game.target_number, 1)
        self.assertLessEqual(game.target_number, 100)
    
    def test_assert_with_custom_message(self):
        """assert 加上自訂錯誤訊息"""
        game = GuessNumberGame(1, 100)
        game.target_number = 50
        
        result = game.guess(50)
        # 可以加上自訂訊息，讓測試失敗時更容易理解問題
        self.assertEqual(result, "正確", "猜對數字應該回傳'正確'")
    
    def test_assert_not_equal(self):
        """assert 判斷不相等"""
        result1 = guess_number(10, 5)
        result2 = guess_number(10, 15)
        
        # assertNotEqual 確保兩個值不同
        self.assertNotEqual(result1, result2)


if __name__ == "__main__":
    # 執行所有測試
    unittest.main(verbosity=2)
