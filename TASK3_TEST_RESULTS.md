# 任務三：執行測試，觀察綠燈與紅燈結果

## 測試結果記錄

### 綠燈（通過）測試結果

執行完整的單元測試，所有測試案例都通過：

```bash
python3 -m unittest test_safe_division.py -v
```

**測試結果：**
```
test_boundary_values (test_safe_division.TestSafeDivision.test_boundary_values)
Test division with boundary values. ... ok
test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero is handled properly. ... ok
test_negative_division (test_safe_division.TestSafeDivision.test_negative_division)
Test division with negative numbers. ... ok
test_normal_division (test_safe_division.TestSafeDivision.test_normal_division)
Test normal division cases with positive numbers. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

**綠燈說明：**
- ✅ 所有 4 個測試案例都通過
- ✅ `safe_division` 函式能正確處理各種情境：
  - 正常的數值相除（10 ÷ 2 = 5.0）
  - 負數相除（-10 ÷ 2 = -5.0）
  - 邊界值相除（0 ÷ 5 = 0.0）
  - **除以零的狀況（返回 None，不會當機）**

### 紅燈（失敗）測試結果

當將 `safe_division.py` 中處理除以零的程式碼註解掉後：

**修改前的程式碼：**
```python
def safe_division(a, b):
    # Handle division by zero
    if b == 0:
        return None
    return a / b
```

**修改後的程式碼（註解掉除以零處理）：**
```python
def safe_division(a, b):
    # Handle division by zero
    # if b == 0:
    #     return None
    return a / b
```

**執行測試後的結果：**
```
test_boundary_values (test_safe_division.TestSafeDivision.test_boundary_values)
Test division with boundary values. ... ok
test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero is handled properly. ... ERROR
test_negative_division (test_safe_division.TestSafeDivision.test_negative_division)
Test division with negative numbers. ... ok
test_normal_division (test_safe_division.TestSafeDivision.test_normal_division)
Test normal division cases with positive numbers. ... ok

======================================================================
ERROR: test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero is handled properly.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division.py", line 38, in test_division_by_zero
    self.assertIsNone(safe_division(10, 0))
  File "safe_division.py", line 25, in safe_division
    return a / b
ZeroDivisionError: division by zero

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=1)
```

**紅燈說明：**
- ❌ 除以零的測試案例失敗
- ❌ 程式直接拋出 `ZeroDivisionError` 異常
- ❌ 測試結果顯示 `FAILED (errors=1)`
- ✅ 其他 3 個測試案例仍然通過（因為它們不涉及除以零）

## 測試案例說明

### 1. test_normal_division（正常數值相除）
- 測試 10 ÷ 2 = 5.0
- 測試 20 ÷ 4 = 5.0
- 測試 100 ÷ 10 = 10.0
- 測試 1 ÷ 2 = 0.5

### 2. test_negative_division（負數相除）
- 測試 -10 ÷ 2 = -5.0
- 測試 10 ÷ -2 = -5.0
- 測試 -10 ÷ -2 = 5.0
- 測試 -100 ÷ 4 = -25.0

### 3. test_boundary_values（邊界值相除）
- 測試 0 ÷ 5 = 0.0
- 測試 1 ÷ 1 = 1.0
- 測試 0.1 ÷ 0.1 = 1.0
- 測試 1 ÷ 3 ≈ 0.333...

### 4. test_division_by_zero（除以零）
- 測試 10 ÷ 0 應返回 None
- 測試 0 ÷ 0 應返回 None
- 測試 -10 ÷ 0 應返回 None
- 測試 100 ÷ 0 應返回 None

## 結論

透過這個任務，我們成功示範了：

1. **綠燈（測試通過）**：當 `safe_division` 函式正確處理除以零的情況時，所有測試都通過，程式不會當機。

2. **紅燈（測試失敗）**：當移除除以零處理的程式碼後，測試失敗並拋出 `ZeroDivisionError` 異常，這證明了單元測試的重要性。

這個練習展示了單元測試如何幫助我們：
- 驗證程式碼的正確性
- 及早發現潛在的錯誤
- 確保邊界條件被妥善處理
- 防止程式在生產環境中崩潰
