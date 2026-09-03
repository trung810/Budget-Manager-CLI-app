# 📊 Terminal-Based Budget Manager

A lightweight, terminal-based personal finance tracker built with Python and Windows Batch scripting. It automatically processes daily transactions, distributes income across customizable percentage allocations, persists balances across sessions, and displays current category totals directly in your console.

---

## ⚡ Features

* **Quick Logging**: Log expenses and income in a simple, standardized text format.
* **Automated Income Allocation**: Distributes incoming funds into budget categories based on configurable percentage rules (e.g., 50/30/20 rule).
* **Persistent Balances**: Stores cumulative account/category balances in a lightweight `cache.txt` file.
* **Interactive Terminal Loop**: Run, view, edit, or reset balances without manually restarting scripts.
* **Windows One-Click Automation**: Uses a `.bat` script to automate file opening, Python processing, and terminal reporting.

---

## 📁 File Structure

```text
├── BudgetManager.py   # Core application logic & terminal interface
├── ClearCache.py      # Utility script to reset all category balances to zero
├── DailyUpdate.txt    # Input template for recording daily income/expenses
├── cache.txt          # Persistent database storing cumulative balances
└── RunBudget.bat      # Windows batch file to run the interactive loop