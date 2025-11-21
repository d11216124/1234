"""
猜數字遊戲 (Guess Number Game)

這是一個簡單的猜數字遊戲，包含主要的遊戲邏輯判斷功能。
玩家需要猜測一個隨機產生的數字，程式會告訴玩家猜的數字是太大、太小還是正確。
"""

import random


class GuessNumberGame:
    """猜數字遊戲類別"""
    
    def __init__(self, min_number=1, max_number=100):
        """
        初始化遊戲
        
        Args:
            min_number: 最小數字範圍
            max_number: 最大數字範圍
        """
        self.min_number = min_number
        self.max_number = max_number
        self.target_number = random.randint(min_number, max_number)
        self.attempts = 0
        self.game_over = False
    
    def guess(self, number):
        """
        判斷玩家猜的數字
        
        Args:
            number: 玩家猜的數字
            
        Returns:
            str: 回應訊息（"太小"、"太大"、"正確" 或錯誤訊息）
        """
        if self.game_over:
            return "遊戲已結束"
        
        # 驗證輸入
        if not isinstance(number, int):
            return "請輸入整數"
        
        if number < self.min_number or number > self.max_number:
            return f"請輸入 {self.min_number} 到 {self.max_number} 之間的數字"
        
        self.attempts += 1
        
        if number < self.target_number:
            return "太小"
        elif number > self.target_number:
            return "太大"
        else:
            self.game_over = True
            return "正確"
    
    def get_attempts(self):
        """取得嘗試次數"""
        return self.attempts
    
    def reset(self):
        """重置遊戲"""
        self.target_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.game_over = False


def guess_number(target, guess):
    """
    簡單的猜數字判斷函數（用於示範單元測試）
    
    Args:
        target: 目標數字
        guess: 猜測的數字
        
    Returns:
        str: 判斷結果
    """
    if not isinstance(target, int) or not isinstance(guess, int):
        return "錯誤：請輸入整數"
    
    if guess < target:
        return "太小"
    elif guess > target:
        return "太大"
    else:
        return "正確"


def main():
    """主程式：執行猜數字遊戲"""
    print("=== 歡迎來到猜數字遊戲 ===")
    game = GuessNumberGame(1, 100)
    print(f"請猜一個 {game.min_number} 到 {game.max_number} 之間的數字")
    
    while not game.game_over:
        try:
            user_input = input("請輸入你的猜測: ")
            number = int(user_input)
            result = game.guess(number)
            print(result)
            
            if result == "正確":
                print(f"恭喜你！你用了 {game.get_attempts()} 次猜對了！")
        except ValueError:
            print("請輸入有效的整數！")
        except KeyboardInterrupt:
            print("\n遊戲結束！")
            break


if __name__ == "__main__":
    main()
