# RISK ANALYSIS

## 1. Technical Risks

| Risk                 | Impact            | Mitigation                   | Level  |
| -------------------- | ----------------- | ---------------------------- | ------ |
| Model input mismatch | Prediction fail   | Validate features before run | High   |
| Large dataset slow   | Performance issue | Limit file size              | Medium |
| Model error          | System crash      | Exception handling           | High   |

---

## 2. Data Risks

| Risk                | Impact           | Mitigation        | Level  |
| ------------------- | ---------------- | ----------------- | ------ |
| Missing data        | Wrong insights   | Validation step   | High   |
| No numeric features | Cannot run model | Show warning      | High   |
| Duplicate data      | Bias results     | Remove duplicates | Medium |

---

## 3. Security Risks

| Risk          | Impact             | Mitigation          | Level  |
| ------------- | ------------------ | ------------------- | ------ |
| Weak password | Account breach     | Password rules      | Medium |
| OTP abuse     | Unauthorized reset | Expire OTP          | Medium |
| SQL injection | Data leak          | Parameterized query | High   |

---

## 4. Business Risks

| Risk                  | Impact        | Mitigation           | Level  |
| --------------------- | ------------- | -------------------- | ------ |
| Wrong prediction      | Bad decision  | Explain model output | High   |
| User misunderstanding | Misuse system | UI guidance          | Medium |
| Low adoption          | System unused | Improve UX           | Medium |

---

## 5. Operational Risks

| Risk               | Impact                | Mitigation           | Level  |
| ------------------ | --------------------- | -------------------- | ------ |
| Email service down | Cannot reset password | Retry / fallback     | Medium |
| Server crash       | Downtime              | Logging & monitoring | High   |
