# 課後行動計畫：QA 實踐與自我挑戰

## 第三單元學習成果

### 1. QA 宣言 (QA Declaration)

> **我的 QA 信念與承諾：**
>
> "我承諾在開發的每個階段都重視程式品質，確保每個功能都有充分的測試覆蓋。我相信好的測試不僅能發現 bug，更能作為程式碼的活文件，幫助團隊理解和維護系統。我會：
> - 為每個核心功能編寫單元測試
> - 在修改程式碼前先執行測試，確保不破壞既有功能
> - 使用 assert 和測試框架來驗證程式行為
> - 持續學習和改進測試技巧，追求更高的程式碼品質"

---

### 2. 為舊專案加上單元測試

#### 專案選擇：猜數字遊戲 (Guess Number Game)

**主要功能：** 判斷玩家猜測的數字是太大、太小還是正確

**測試設計方法：**

1. **基本判斷邏輯測試** (`TestGuessNumberFunction`)
   - 測試「太小」的判斷：當猜測值 < 目標值
   - 測試「太大」的判斷：當猜測值 > 目標值
   - 測試「正確」的判斷：當猜測值 = 目標值
   - 測試無效輸入：非整數輸入的處理
   - 測試邊界情況：負數、零等特殊值

2. **完整遊戲類別測試** (`TestGuessNumberGame`)
   - 測試初始化：驗證遊戲狀態正確設定
   - 測試範圍檢查：超出範圍的輸入應被拒絕
   - 測試遊戲流程：多次猜測後的狀態變化
   - 測試結束條件：猜對後遊戲應結束
   - 測試計數功能：正確記錄嘗試次數
   - 測試重置功能：能夠重新開始遊戲

3. **Assert 用法展示** (`TestAssertExamples`)
   - 展示各種 assert 方法的使用時機
   - 提供最佳實踐範例

**測試檔案：** `test_guess_number_game.py`

**執行方式：**
```bash
python test_guess_number_game.py
```

或使用更詳細的輸出：
```bash
python -m unittest test_guess_number_game -v
```

---

### 3. 學習 assert 指令

#### Assert 的最佳使用情境

**Assert 最好用的情境：自動比對實際輸出與理想結果，及早發現錯誤**

#### 常用的 Assert 方法

1. **assertEqual(a, b)**
   ```python
   # 確保函數回傳正確的結果
   self.assertEqual(guess_number(5, 3), "太小")
   ```
   - 用途：檢查兩個值是否相等
   - 情境：驗證函數輸出是否符合預期

2. **assertTrue / assertFalse**
   ```python
   # 確保遊戲狀態正確
   self.assertFalse(game.game_over)  # 遊戲還沒結束
   ```
   - 用途：檢查布林條件
   - 情境：驗證狀態標記、條件判斷

3. **assertIn / assertNotIn**
   ```python
   # 確保回應是有效的選項之一
   valid_responses = ["太小", "太大", "正確"]
   self.assertIn(result, valid_responses)
   ```
   - 用途：檢查元素是否在集合中
   - 情境：驗證回傳值屬於預期範圍

4. **assertGreater / assertLess / assertGreaterEqual / assertLessEqual**
   ```python
   # 確保數字在合理範圍內
   self.assertGreaterEqual(game.target_number, 1)
   self.assertLessEqual(game.target_number, 100)
   ```
   - 用途：數值大小比較
   - 情境：驗證數值範圍、邊界條件

5. **assertRaises**
   ```python
   # 確保錯誤情況會拋出例外
   with self.assertRaises(ValueError):
       invalid_function_call()
   ```
   - 用途：檢查是否正確拋出例外
   - 情境：驗證錯誤處理機制

#### Assert 的核心價值

- **自動化驗證**：不需要手動檢查每個輸出，測試框架自動比對
- **快速回饋**：程式碼修改後立即知道是否破壞原有功能
- **文件作用**：測試案例說明了程式應該如何運作
- **重構安全網**：有了完整的測試，可以放心重構程式碼
- **及早發現問題**：在開發階段就發現 bug，而不是等到上線

---

### 4. 單元測試實作成果

#### 檔案結構
```
1234/
├── guess_number_game.py          # 猜數字遊戲主程式
├── test_guess_number_game.py     # 單元測試檔案
├── QA_ACTION_PLAN.md             # 本文件
└── COPILOT_BUG_EXPERIENCE.md     # Copilot 除錯經驗分享
```

#### 測試覆蓋範圍

本專案為猜數字遊戲建立了 **20 個測試案例**，涵蓋：

✅ 基本判斷邏輯（太大、太小、正確）  
✅ 輸入驗證（類型檢查、範圍檢查）  
✅ 遊戲狀態管理（計數、結束條件）  
✅ 邊界情況（負數、零、極值）  
✅ 錯誤處理（無效輸入、遊戲結束後的操作）  
✅ 進階功能（重置、自訂範圍、多實例）  
✅ Assert 用法展示

#### 測試結果

執行測試確保所有功能正常運作：
```bash
python -m unittest test_guess_number_game -v
```

預期輸出：所有測試通過 ✓

---

### 5. 學習心得

通過這次實作，我深刻體會到：

1. **測試驅動開發的價值**：先寫測試可以幫助我們更清楚地思考功能需求
2. **Assert 的強大**：簡單的 assert 語句就能建立強大的品質保證機制
3. **測試的投資報酬率**：花時間寫測試，能在未來節省更多除錯時間
4. **測試即文件**：好的測試案例就是最好的使用說明

### 6. 下一步行動

- [ ] 為更多舊專案補充單元測試
- [ ] 學習整合測試和端對端測試
- [ ] 探索測試覆蓋率工具（如 coverage.py）
- [ ] 研究測試驅動開發（TDD）的實踐方法
- [ ] 學習 mock 和 stub 等進階測試技巧

---

**日期：** 2025-11-21  
**作者：** QA 實踐者  
**版本：** 1.0
