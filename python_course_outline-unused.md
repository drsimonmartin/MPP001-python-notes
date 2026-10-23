# Python Programming for Engineering Students
## 7-Week Self-Taught Course Outline

**Format:** Largely self-directed study with a 2-hour weekly computing lab session for exercises and staff-supported guidance.

**Philosophy:** Syntax is scaffolding, not the goal. The real aim is developing *computational thinking* and the ability to design and implement algorithms for engineering problems.

---

## Course Structure Overview

| Week | Topic | Lab Focus |
|------|-------|-----------|
| 1 | Foundations and computational thinking | First programs: unit conversion, simple calculations |
| 2 | Data structures and algorithmic thinking | Data wrangling: read, clean, query CSV datasets |
| 3 | Numerical methods with NumPy | Engineering maths: implement bisection, trapezoid rule |
| 4 | Visualisation and iteration strategies | Plot and analyse: stress-strain, signal data, curve fitting |
| 5 | Simulation and modelling physical systems | Simulate a system: projectile, cooling, fatigue failure |
| 6 | Data analysis and pipeline design | Experimental data: analyse and model real test results |
| 7 | Capstone: from brief to working solution | Open-ended project: submit working solution + reflection |

---

## Week 1 — Foundations and Computational Thinking

**Self-study content:**
- Python setup (Anaconda/VS Code or Jupyter)
- Variables and types
- Conditionals and loops
- Writing simple functions

**Key principle:** The very first examples should use engineering quantities — converting between unit systems, checking whether a stress value exceeds a yield strength — so students immediately see Python as a tool, not an abstract exercise.

**Lab session:** Students write a small collection of short programs from scratch:
- A unit converter
- A simple beam load calculator
- A grading threshold checker

---

## Week 2 — Data Structures and Algorithmic Thinking

**Self-study content:**
- Lists, dictionaries, and tuples
- File I/O
- Introduction to searching and sorting algorithms

**Key principle:** Before touching Python code, students should sketch out a bubble sort or linear search on paper, trace through it by hand, and only then implement it. Data structures are taught in the context of storing and querying engineering data.

**Lab session:** Reading CSV files (experimental results, material property tables) and writing code to search and reorganise them.

---

## Week 3 — Numerical Methods with NumPy

**Self-study content:**
- NumPy arrays, vectorised operations, and broadcasting
- Root-finding: bisection method and Newton-Raphson
- Numerical integration: trapezoid and Simpson's rules

**Key principle:** Algorithms students should derive and understand before implementing. This is where Python starts to feel genuinely powerful for engineering students.

**Lab session:** Solve a specific engineering problem — for example:
- Finding where a stress function equals yield stress
- Calculating the area under a load-displacement curve

---

## Week 4 — Visualisation and Iteration Strategies

**Self-study content:**
- Matplotlib: publication-quality engineering plots
- Stress-strain curves, frequency response, time-series sensor data
- Iteration design: `for` vs `while`, convergence criteria
- Introduction to recursion (factorial → recursive subdivision)

**Lab session:** Plotting and interpreting real-looking datasets, including:
- Adding annotations and dual axes
- Formatting plots for technical reports

---

## Week 5 — Simulation and Modelling Physical Systems

**Self-study content:**
- Euler integration for ODEs
- Projectile motion, Newton's cooling law, spring-mass-damper systems
- Monte Carlo methods (estimating π as warm-up, then reliability/uncertainty estimation)

**Key principle:** The governing equation comes first, the code second. The emphasis is on *translating a physical model into an algorithm*.

**Lab session:** Students receive a physical scenario and write the simulation from scratch.

---

## Week 6 — Data Analysis and Pipeline Design

**Self-study content:**
- Pandas for larger datasets
- Descriptive statistics, correlation
- Linear and polynomial regression
- Designing reusable analysis pipelines

**Key principle:** Code should be structured as a logical sequence of steps from raw data to conclusion, where each step is a function — readable and reusable.

**Lab session:** Using a realistic dataset (fatigue test results, tensile test records, or sensor logs) to:
- Characterise the data
- Fit a model
- Draw and report a conclusion

---

## Week 7 — Capstone: From Brief to Working Solution

**Self-study content:**
- Code quality: docstrings and commenting
- Unit testing with `pytest`
- Version control basics (Git)
- Reading and understanding other people's code

**Lab session (assessed):** Students receive an open-ended engineering problem brief and produce a working solution with brief documentation explaining their algorithmic approach.

**Submission:** Working solution + written reflection on algorithmic design decisions.

---

## Design Recommendations

### Assessment
Weight assessment toward the capstone (week 7) and one mid-course checkpoint (week 4 or 5), rather than weekly quizzes, to reduce cognitive overhead during self-study.

### Self-Study Material Structure
Each week's materials should follow a consistent format:

1. Concept explanation
2. Worked example
3. Directed exercise
4. Open challenge (no single right answer — requires a design decision)

### Lab Session Guidance
Lab sessions work best when staff circulate and ask *"what did you try first?"* rather than immediately providing solutions. The goal is to build tolerance for uncertainty and the habit of breaking a problem down before coding.

### Pseudocode-First Rule
For weeks 3–6, consider requiring students to write out their algorithm in plain English or as a flowchart before any lab exercise is marked complete. This builds the bridge between problem understanding and implementation.
