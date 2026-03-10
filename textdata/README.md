# 🧠 AI Self-Healing Automation Framework

## 🚀 Project Title
**AI-Based Self-Healing Test Automation Framework using Playwright**

---

# 📌 Project Overview

This project is an **intelligent UI automation framework** that can **automatically detect and fix broken locators** when UI changes occur.

It is built using **Python and Playwright**, and uses **DOM analysis + similarity scoring** to find and heal elements dynamically.

---

❗ Problem Statement

In real-time applications:

- UI elements frequently change (ID, class, structure)
- Automation scripts fail even though functionality works
- Maintenance effort becomes very high
- CI/CD pipelines break due to false failures

---

💡 Our Solution

We built a **Self-Healing Automation Framework** that:

1. Detects locator failure
2. Captures current DOM
3. Finds best matching element using similarity scoring
4. Generates a new locator
5. Retries the action
6. Updates JSON locator file automatically
7. Generates a clean HTML report

---

## ✨ Key Features

- 🔍 Automatic locator healing
- 📊 Similarity score calculation
- 📁 JSON auto-update with healed locators
- 🌐 DOM snapshots (Before & After)
- 📄 HTML execution report
- 🧪 Playwright UI automation
- ⚡ Handles dynamic UI changes

---

## 🏗️ Project Structure

SELFHEALING_LOCATORS/
│
├── engine/
│   ├── __init__.py
│   ├── ai_engine.py              # AI similarity scoring logic
│   ├── dom_capture.py            # Capture DOM snapshots
│   ├── dom_parser.py             # Parse DOM elements
│   ├── healer.py                 # Self-healing core logic
│   └── locator_generator.py      # Generate new locator
│
├── textdata/
│   └── inputdata.json            # Stores element locators
│
├── utils/
│   ├── __init__.py
│   └── reporter.py               # HTML report generator
│
├── locator_utils.py              # Converts locator types (id, css, xpath)
├── login_page.py                 # Page Object Model for login
├── test_file.py                  # Test execution file
│
├── original_dom.html             # DOM before UI change
├── updated_dom.html              # DOM after UI change
├── healing_report.html           # Final execution report
│
└── README.md                     # Project documentation

---

## ⚙️ Technologies Used

- Python
- Playwright
- JSON
- HTML/CSS
- DOM Parsing
- Similarity Algorithm (Score-based healing)

---

## 🧪 How It Works

### Example Scenario

Before UI change:

#user-name


After UI change:

#fail


Framework execution:


[INFO] Trying original locator → FAILED
[INFO] Healing started
Best match found with score: 0.593
New locator generated: #fail
Retry action → SUCCESS
JSON updated
Report generated


---

## 📊 Sample Execution Report

| Element      | Status  | Original Locator | Healed Locator | Score |
|-------------|--------|------------------|---------------|-------|
| username     | HEALED | #user-name       | #fail         | 0.593 |
| password     | PASS   | #password        | -             | -     |
| login_button | PASS   | #login-button    | -             | -     |

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install playwright
playwright install
2️⃣ Run the Test
python test_login.py
3️⃣ View Report

Open the file:

reporter.html

in your browser.

🔄 Auto JSON Update

When healing succeeds, locator gets updated automatically in:

textdata/inputdata.json
🌐 DOM Snapshot Feature

The framework captures:

original_dom.html → before UI change

updated_dom.html → after UI change

This helps visualize element changes clearly.

🎯 Real-Time Use Cases

1.Regression Testing

2.CI/CD pipelines

3.Agile UI applications

4.Frequently changing frontends

5.Enterprise QA automation

🚀 Future Enhancements:

AI/ML model-based locator prediction

XPath & CSS hybrid healing

Dashboard analytics

CI integration (Jenkins/GitHub Actions)

Screenshot comparison support

👩‍💻 Authors:

Kotha Vijaya Lakshmi
shinagam Deepika
Medikonda Harshitha

  Conclusion:

This framework helps in:

1.Reducing automation maintenance
2.Improving test stability
3.Avoiding false failures 
4.Enabling smart testing

💬 Pitch Line:

“This is not just automation… this is self-healing intelligent automation that adapts when the UI changes.”


