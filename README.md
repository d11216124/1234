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