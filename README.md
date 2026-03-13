# Smart Study Planner 📚

A simple web application built using **Python and Flask** that helps students generate a balanced study plan based on their available study hours and subjects.

This project focuses on solving a common problem faced by students: **how to divide study time effectively across multiple subjects**.

---

## Problem Statement

Students often struggle to decide **how much time they should spend on each subject** when they have limited study hours. Poor time distribution can lead to stress and inefficient study sessions.

---

## Solution

The **Smart Study Planner** allows users to:

* Enter their subjects
* Enter available study hours
* Select subject priority

The application then **automatically generates a study plan** with suggested time allocation and break recommendations.

---

## Features

* Generate a study plan based on available hours
* Priority-based subject planning
* Automatic break time suggestion
* Visual progress bars for study time
* Clean and simple user interface

---

## Tech Stack

* **Python**
* **Flask**
* **HTML**
* **CSS**

---

## Project Structure

```
smart_study_planner
│
├── app.py
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/smart-study-planner.git
```

2. Navigate to the project folder

```
cd smart-study-planner
```

3. Install Flask

```
pip install flask
```

4. Run the application

```
python app.py
```

5. Open your browser and go to

```
http://127.0.0.1:5000
```

---

## Example

Input:

```
Subjects: Maths, Physics, Python
Available Hours: 6
Priority: High
```

Output:

```
Maths → 2 hours
Physics → 2 hours
Python → 2 hours
Suggested Break Time → 0.3 hours
```

---

## Learning Outcomes

Through this project I learned:

* Basics of **Flask web development**
* Handling **user input from forms**
* Connecting **Python backend with HTML frontend**
* Building simple productivity tools

---

## Future Improvements

* Automatic **hour-by-hour study timetable**
* Integration with **Google Calendar**
* AI-based study recommendations
* Exam date tracking

---

## Author

**Swarupa Shinde**

First Year B.Tech CSE (AI) Student
Exploring Python, AI and Web Development 🚀
