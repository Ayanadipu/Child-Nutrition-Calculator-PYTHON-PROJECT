# Child Nutrition Calculator (Python GUI)

A simple **Python GUI application** that calculates a child's **BMI, daily calorie consumption, and minimum calorie requirement** based on their age and food intake.  
The application helps determine whether a child’s **nutrition intake is adequate or indicates undernourishment**.

Built using **Python and Tkinter**.

---

## Features

- Input child details:
  - Name
  - Age
  - Gender
  - Height (cm)
  - Weight (kg)

- Enter daily food intake (grams):
  - Milk
  - Egg
  - Rice
  - Lentils
  - Vegetable
  - Meat

- Calculates:
  - **BMI (Body Mass Index)**
  - **Minimum daily calorie requirement**
  - **Daily calorie consumption**

- Displays nutrition status:
  - Undernourished
  - Adequate calorie intake

---

## Technologies Used

- Python
- Tkinter (Python GUI library)

---

## Project Structure

```
Child-Nutrition-Calculator-PYTHON-PROJECT
│
├── child_nutrition_calculator.py
└── README.md
```

---

## How the Program Works

1. User enters child details (name, age, gender, height, weight).
2. User enters food intake quantities in grams.
3. The program:
   - Calculates **BMI**
   - Determines **minimum calorie requirement** based on age
   - Calculates **total calories consumed**
4. The results are displayed in a popup window.

---

## Age Based Calorie Requirement

| Age Group | Minimum Daily Calories |
|-----------|-----------------------|
| 0 – 2 years | 800 calories |
| 2 – 4 years | 1400 calories |
| 4 – 8 years | 1800 calories |

---

## BMI Formula

```
BMI = weight (kg) / height (m)^2
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/Child-Nutrition-Calculator-PYTHON-PROJECT.git
```

### 2. Navigate to the Project Folder

```
cd Child-Nutrition-Calculator-PYTHON-PROJECT
```

### 3. Run the Application

```
python child_nutrition_calculator.py
```

---

## Example Output

The program displays:

- Calculated BMI
- Minimum daily calorie requirement
- Daily calorie consumption
- Child nutrition status

---

## Future Improvements

- Add more food categories
- Improve GUI design
- Add graphical nutrition charts
- Save reports for multiple children
- Add input validation

---

## Author

Developed as a **Python project for learning GUI development and basic health calculations**.
