# 課後行動計畫：QA 實踐與自我挑戰

這個專案是「第三單元：QA 實踐與自我挑戰」的學習成果，包含一個完整的猜數字遊戲及其單元測試。

## 📁 專案結構

```
1234/
├── guess_number_game.py          # 猜數字遊戲主程式
├── test_guess_number_game.py     # 單元測試檔案
├── QA_ACTION_PLAN.md             # QA 行動計畫文件
├── COPILOT_BUG_EXPERIENCE.md     # Copilot 除錯經驗分享
└── README.md                     # 本文件
```

## 🎮 猜數字遊戲

一個互動式的猜數字遊戲，玩家需要猜測程式隨機產生的數字。

### 功能特色

- ✅ 隨機產生目標數字
- ✅ 智慧型回應（太大、太小、正確）
- ✅ 輸入驗證（類型檢查、範圍檢查）
- ✅ 嘗試次數追蹤
- ✅ 遊戲狀態管理
- ✅ 可自訂數字範圍

### 執行遊戲

```bash
python guess_number_game.py
```

## 🧪 單元測試

使用 Python 的 `unittest` 模組建立完整的測試套件。

### 測試涵蓋範圍

- **基本判斷邏輯測試** (11 個測試案例)
  - 猜測太小、太大、正確的判斷
  - 無效輸入處理
  - 邊界條件測試

- **完整遊戲類別測試** (9 個測試案例)
  - 初始化驗證
  - 範圍檢查
  - 遊戲流程控制
  - 狀態管理
  - 多實例測試

- **Assert 用法展示** (6 個測試案例)
  - assertEqual, assertTrue/False
  - assertIn/NotIn
  - assertGreater/Less
  - 自訂錯誤訊息

### 執行測試

```bash
# 執行所有測試
python -m unittest test_guess_number_game

# 詳細輸出
python -m unittest test_guess_number_game -v

# 執行單一測試類別
python -m unittest test_guess_number_game.TestGuessNumberFunction -v
```

### 測試結果

```
Ran 20 tests in 0.002s
OK ✓
```

## 📚 學習文件

### 1. QA_ACTION_PLAN.md
包含：
- QA 宣言與承諾
- 單元測試設計方法
- Assert 指令學習與最佳實踐
- 測試覆蓋範圍說明
- 學習心得與下一步行動

### 2. COPILOT_BUG_EXPERIENCE.md
包含：
- Copilot 協助除錯的真實案例
- 發現邊界條件遺漏的經驗
- 遊戲狀態管理的改進
- Copilot 在 QA 流程中的價值
- 未來應用想像

## 🎯 學習成果

通過這個專案，我學會了：

1. ✅ **編寫高品質的單元測試**
   - 涵蓋正常情況、邊界情況、錯誤情況
   - 使用 setUp 方法初始化測試環境
   - 編寫清晰的測試文檔字串

2. ✅ **掌握 Assert 的各種用法**
   - assertEqual、assertTrue、assertIn 等
   - 理解何時使用哪種 assert 方法
   - 加入自訂錯誤訊息提高可讀性

3. ✅ **實踐測試驅動開發（TDD）**
   - 先思考測試案例，再實作功能
   - 透過測試發現潛在問題
   - 重構時有測試保護

4. ✅ **程式碼品質保證**
   - 輸入驗證的重要性
   - 狀態管理的正確性
   - 防禦性編程思維

## 🚀 下一步計畫

- [ ] 學習測試覆蓋率工具（coverage.py）
- [ ] 探索整合測試和端對端測試
- [ ] 研究 mock 和 stub 等進階測試技巧
- [ ] 為更多專案補充單元測試
- [ ] 學習持續整合（CI）的測試自動化

## 📝 作業要求完成度

- ✅ QA 宣言：已完成（見 QA_ACTION_PLAN.md）
- ✅ 為舊專案加上單元測試：已完成（猜數字遊戲 + 測試）
- ✅ 學習 assert 指令：已完成（20+ 個測試案例示範）
- ✅ 分享 Copilot 抓 Bug 經驗：已完成（見 COPILOT_BUG_EXPERIENCE.md）

---

**日期：** 2025-11-21  
**作者：** QA 實踐者