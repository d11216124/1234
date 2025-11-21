# 任務三：執行測試，觀察綠燈與紅燈結果

## Task 3: Execute Tests and Observe Green Light vs Red Light Results

這個專案展示單元測試中的綠燈（測試通過）與紅燈（測試失敗）場景。

This project demonstrates green light (tests pass) vs red light (tests fail) scenarios in unit testing.

## 專案結構 / Project Structure

```
.
├── safe_division.py              # 正確的 safe_division 函式（處理除以零）
├── safe_division_broken.py       # 錯誤版本（未處理除以零）
├── test_safe_division.py         # 綠燈測試（所有測試通過）
├── test_safe_division_broken.py  # 紅燈測試（除以零測試失敗）
├── run_task3_demo.sh            # 示範腳本
├── TASK3_TEST_RESULTS.md        # 詳細測試結果文件
└── README.md                     # 本文件
```

## 快速開始 / Quick Start

### 方法一：運行完整示範腳本
```bash
./run_task3_demo.sh
```

### 方法二：分別運行測試

#### 綠燈測試（所有測試通過）
```bash
python3 -m unittest test_safe_division.py -v
```

#### 紅燈測試（除以零測試失敗）
```bash
python3 -m unittest test_safe_division_broken.py -v
```

## 測試案例 / Test Cases

### 1. test_normal_division（正常數值相除）
- 測試正常的除法運算
- 例如：10 ÷ 2 = 5.0

### 2. test_negative_division（負數相除）
- 測試包含負數的除法運算
- 例如：-10 ÷ 2 = -5.0

### 3. test_boundary_values（邊界值相除）
- 測試邊界情況
- 例如：0 ÷ 5 = 0.0

### 4. test_division_by_zero（除以零）
- **關鍵測試**：驗證除以零是否被妥善處理
- 正確實作應返回 None
- 錯誤實作會拋出 ZeroDivisionError

## 學習重點 / Key Learnings

1. **綠燈（通過）**：當程式正確處理所有情境（包括除以零），所有測試通過
2. **紅燈（失敗）**：當移除錯誤處理程式碼，測試會失敗並暴露問題
3. **單元測試的重要性**：幫助我們及早發現錯誤，確保程式碼品質

## 詳細結果

請參閱 [TASK3_TEST_RESULTS.md](TASK3_TEST_RESULTS.md) 查看完整的測試結果和說明。
# 1234

## 任務一：防呆 safe_division 函式

這個專案實作了一個 Python `safe_division` 函式，能夠防止除以零的錯誤。

### 功能特點

- ✅ 防止除以零錯誤
- ✅ 支援整數和浮點數
- ✅ 完整的型別註解 (Type Hints)
- ✅ 完善的文件說明
- ✅ 通過所有測試

### 使用方法

```python
from safe_division import safe_division

# 正常除法
result = safe_division(10, 2)  # 返回: 5.0

# 除以零的情況 (返回 None)
result = safe_division(10, 0)  # 返回: None

# 浮點數除法
result = safe_division(7.5, 2.5)  # 返回: 3.0
```

### 檔案說明

- `safe_division.py` - 主要函式實作
- `demo.py` - 示範程式
- `.gitignore` - 排除 Python 快取檔案

### 執行示範

```bash
python3 demo.py
```

### 執行測試

```bash
python3 -m doctest safe_division.py -v
```
