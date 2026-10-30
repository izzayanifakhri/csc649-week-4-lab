# Tech Stack Evaluation

## Project
AI-based Scam Risk Assessmemt System 

## Requirements that drive the decision
Functional requirements (what the system does):
- The system shall allow users to submit suspicious text messages for analysis.
- The system shall allow users to upload screenshots of suspicious messages.
- The system shall analyse submitted content and display a scam risk assessment.
- The system shall provide an explanation of the assessment result.
Non-functional requirements (how the system should perform):
- The system should provide results within a reasonable response time.
- The system should protect users' personal information and submitted messages.

## Options
- Option A: Static website using HTML, CSS and JavaScript, hosted on GitHub Pages.
- Option B: Python web application using Flask, Scikit-learn and SQLite, hosted on a cloud platform.
- Option C: Python web application using Django, Scikit-learn and PostgreSQL, hosted on a cloud platform.

## Decision matrix

| Criterion | Weight | Reason |
|---|---|---|
| Fits my requirements | 5 | The system needs ML and image processing capabilities. |
| Skills I already have | 4 | You have some programming experience, but are still developing your Python skills. |
| Time to build before my deadline | 5 | You need a manageable technology stack. |
| Free hosting and tools | 3 | Keeping development costs low is important. |
| Performance and security needs | 4 | Messages and screenshots may contain personal information. |
| Room to grow later | 3 | The system may gain additional features in the future. |

| Criterion                        | Weight | A score | B score | C score |
|----------------------------------|--------|---------|---------|---------|
| Fits my requirements             | 5      | 1       | 5       | 5       |
| Skills I already have            | 4      | 3       | 3       | 2       |
| Time to build before my deadline | 5      | 5       | 4       | 2       |
| Free hosting and tools           | 3      | 5       | 4       | 3       |
| Performance and security needs   | 4      | 2       | 4       | 4       |
| Room to grow later               | 3      | 2       | 4       | 5       |
| **Total (weighted)**             |        | **71**  | **97**  | **83**  |

## Decision record
- **Context:** The project is an Intelligent Scam Risk Assessment System that analyses suspicious messages and screenshots to identify potential scams. The project requires machine learning, image processing and a web-based interface. Development time, programming skills and cost are also important considerations.
- **Decision:** Option B – Python web application using Flask, Scikit-learn and SQLite, hosted on a cloud platform.
- **Reasons:** Flask supports Python integration, making it suitable for implementing machine learning models using Scikit-learn. SQLite provides a simple database solution for managing system data.
Option B achieved the highest weighted score of 97, showing that it provides a good balance between project requirements, development time and available skills.
- **Consequences:** Flask makes it easier to integrate machine learning models into the web application and provides flexibility for future development. However, additional work is needed to implement user authentication, security features and image processing.
- **Risks and next review:** The main risks include limited experience with Python, difficulties in integrating image processing and machine learning, and possible limitations of free cloud hosting. The technology stack will be reviewed during the development phase if the chosen technologies cannot meet the project requirements.
