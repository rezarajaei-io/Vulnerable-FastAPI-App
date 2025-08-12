# Vulnerable FastAPI App (DefenSys Testbed)

A simple, lightweight, and intentionally vulnerable web application built with FastAPI. This project serves as a reliable testbed for the [DefenSys Security Scanner](https://github.com/rezarajaei-io/DefenSys) and other security tools.

---

## 🎯 Why This Project Exists

Developing security tools requires a consistent and predictable environment to test against. While powerful options like the OWASP BWA exist, they often come with significant overhead. This project was created to solve several key problems:

* **Avoiding Heavy Setups:** Eliminates the need for heavy virtual machines (like VirtualBox) or complex Docker configurations, which can be resource-intensive on some development machines.
* **Providing a Stable Target:** Publicly available vulnerable sites can go offline or change unexpectedly. This application provides a stable, always-available target that you control.
* **Saving Time:** Instead of searching for suitable vulnerable targets for each scanner, this app provides a centralized collection of common, clear-cut vulnerabilities.
* **Full Control:** It gives us a controlled environment where we know exactly what the expected outcome of a scan should be, making it perfect for validating our scanner's logic.

---

## 🔬 Vulnerable Endpoints

This application exposes the following intentionally vulnerable endpoints for testing:

* **Reflected Cross-Site Scripting (XSS)**
    * **URL:** `http://127.0.0.1:8000/xss`
    * **Parameter:** `query`
    * **Example:** `http://127.0.0.1:8000/xss?query=<script>alert(1)</script>`

* **SQL Injection (SQLi)**
    * **URL:** `http://127.0.0.1:8000/sqli`
    * **Parameter:** `id`
    * **Example:** `http://127.0.0.1:8000/sqli?id=1' OR 1=1 --`

* **OS Command Injection**
    * **URL:** `http://127.0.0.1:8000/commandi`
    * **Parameter:** `ip`
    * **Example:** `http://127.0.0.1:8000/commandi?ip=8.8.8.8; whoami`

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.7+
-   pip

### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rezarajaei-io/Vulnerable-FastAPI-App.git](https://github.com/rezarajaei-io/Vulnerable-FastAPI-App.git)
    cd Vulnerable-FastAPI-App
    ```

2.  **Install the required packages:**
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

3.  **Run the application:**
    ```bash
    uvicorn vulnerable_app:app --reload
    ```

The application will now be running at `http://127.0.0.1:8000`.

---

## ⚠️ Disclaimer

This is an **insecure by design** application. It is intended for educational and testing purposes **only**. **DO NOT** deploy this application in a production or publicly accessible environment.
