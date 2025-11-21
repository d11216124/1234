#!/bin/bash

echo "=========================================="
echo "任務三：單元測試綠燈與紅燈示範"
echo "Task 3: Green Light vs Red Light Demo"
echo "=========================================="
echo ""

echo "第一部分：綠燈測試（所有測試通過）"
echo "Part 1: Green Light (All Tests Pass)"
echo "=========================================="
echo ""
echo "執行命令：python3 -m unittest test_safe_division.py -v"
echo "Running: python3 -m unittest test_safe_division.py -v"
echo ""
python3 -m unittest test_safe_division.py -v
GREEN_EXIT_CODE=$?
echo ""
echo "結果：測試通過 ✅"
echo "Result: Tests PASSED ✅"
echo ""
echo "=========================================="
echo ""

echo "第二部分：紅燈測試（除以零處理被註解）"
echo "Part 2: Red Light (Division by Zero Handler Removed)"
echo "=========================================="
echo ""
echo "執行命令：python3 -m unittest test_safe_division_broken.py -v"
echo "Running: python3 -m unittest test_safe_division_broken.py -v"
echo ""
python3 -m unittest test_safe_division_broken.py -v 2>&1
RED_EXIT_CODE=$?
echo ""
echo "結果：測試失敗 ❌ (ZeroDivisionError)"
echo "Result: Tests FAILED ❌ (ZeroDivisionError)"
echo ""
echo "=========================================="
echo ""

echo "總結 Summary:"
echo "----------------------------------------"
echo "綠燈測試 (Green Light): Exit Code = $GREEN_EXIT_CODE (0 = 成功/Success)"
echo "紅燈測試 (Red Light):   Exit Code = $RED_EXIT_CODE (1 = 失敗/Failed)"
echo "=========================================="
echo ""
echo "詳細測試結果請參閱 TASK3_TEST_RESULTS.md"
echo "For detailed results, see TASK3_TEST_RESULTS.md"
