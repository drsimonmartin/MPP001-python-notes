# Python Programming for Engineers (MSc Conversion Programme)
## Suggested Real-World Datasets and Laboratory Applications

### Module Context

This module is designed for MSc engineering students who possess strong engineering knowledge but have limited prior programming experience. Programming concepts are introduced through authentic engineering problems drawn from materials engineering, biomedical engineering and automotive engineering. The emphasis is on computational thinking, data handling and engineering analysis rather than computer science theory.

The datasets below are recommended for use throughout the six laboratory sessions and subsequent Gradescope Code Runner assessments.

---

# Dataset Selection Principles

Datasets should:

- Be based on real engineering measurements.
- Contain enough data for meaningful analysis.
- Be small enough for students with limited programming experience.
- Support progressively more advanced programming concepts.
- Be available under open licences where possible.
- Be easy to distribute through the VLE and Gradescope.

---

# Materials Engineering Datasets

## 1. Concrete Compressive Strength Dataset (UCI Machine Learning Repository)

### Description

A dataset containing measurements of concrete mixtures and their corresponding compressive strengths.

Variables include:

- Cement content
- Water content
- Fly ash content
- Aggregate composition
- Age of concrete
- Measured compressive strength

The dataset contains approximately 1,000 samples and is widely used for engineering education and materials informatics applications. 【1-7f8f34】【2-e1edbc】

### Educational Value

Students can investigate:

- Average material properties
- Data variability
- Engineering tolerances
- Quality control processes

### Example Programming Tasks

#### Lab 3 (Loops)

Calculate:

- Average strength
- Maximum strength
- Minimum strength

#### Lab 4 (Lists)

Count how many concrete samples exceed a design specification.

#### Lab 6 (Mini Project)

Develop a quality control tool that:

- Reads data
- Calculates statistics
- Identifies failed samples
- Reports pass rate

### Dataset Link

https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength

---

## 2. Materials Project Database

### Description

An open database of engineering materials containing information on:

- Density
- Crystal structure
- Elastic modulus
- Band gap
- Formation energy

Widely used in computational materials science and materials informatics. 【3-e0a8a3】

### Educational Value

A simplified subset can be used for:

- Material selection exercises
- Ranking materials
- Multi-criteria engineering decisions

### Example Programming Tasks

Students write programs to identify:

- The lightest material above a strength threshold
- The stiffest material within a density constraint
- The lowest-cost material meeting design requirements

### Dataset Link

https://materialsproject.org/

---

## 3. Ashby Materials Property Tables

### Description

Small educational datasets containing:

- Material name
- Density
- Yield strength
- Young’s modulus
- Material cost

### Educational Value

Provides a direct link between programming and engineering design.

### Example Programming Tasks

Students:

- Rank candidate materials
- Calculate performance indices
- Select materials based on design requirements

---

# Biomedical Engineering Datasets

## 4. PhysioNet Physiological Signal Databases

### Description

PhysioNet provides open physiological datasets including:

- ECG measurements
- Heart rate
- Blood pressure
- Respiratory rate
- Oxygen saturation

These datasets are widely used for biomedical engineering education and research. 【4-9a2a7b】【5-25154b】

### Educational Value

Students learn how programming can support:

- Clinical monitoring
- Signal analysis
- Decision support systems

### Example Programming Tasks

#### Lab 2 (Selection)

Classify patient heart rates:

- Low
- Normal
- High

#### Lab 3 (Loops)

Calculate:

- Average heart rate
- Maximum heart rate
- Time spent outside safe limits

#### Lab 4 (Lists)

Count abnormal readings in a dataset.

### Dataset Link

https://physionet.org/

---

## 5. VitalDB

### Description

VitalDB contains physiological measurements collected during surgical procedures, including:

- Heart rate
- Blood pressure
- Oxygen saturation
- Temperature

The dataset contains high-resolution physiological records from thousands of patients. 【6-4b46cd】【7-804752】

### Educational Value

Students gain exposure to authentic biomedical monitoring data.

### Example Programming Tasks

Students analyse:

- Mean patient heart rate
- Maximum blood pressure
- Numbers of alarm events

### Dataset Link

https://vitaldb.net/dataset/

---

## 6. UCI Heart Disease Dataset

### Description

Contains clinical measurements including:

- Age
- Blood pressure
- Cholesterol
- Heart disease diagnosis

Widely used in teaching data analysis and classification. 【3-e0a8a3】

### Educational Value

Ideal for threshold-based decision making.

### Example Programming Tasks

Students:

- Calculate average patient characteristics
- Count high-risk patients
- Implement simple risk classifications

### Dataset Link

https://archive.ics.uci.edu/

---

# Automotive Engineering Datasets

## 7. Auto MPG Dataset (UCI Machine Learning Repository)

### Description

A classic dataset describing vehicle fuel economy.

Variables include:

- MPG
- Engine displacement
- Horsepower
- Weight
- Model year

The dataset contains data for 398 vehicles. 【8-c12b9f】【9-9a95ec】

### Educational Value

Students can perform meaningful engineering calculations using familiar automotive concepts.

### Example Programming Tasks

#### Lab 4 (Lists)

Calculate:

- Average fuel economy
- Most efficient vehicle
- Least efficient vehicle

#### Lab 6 (Mini Project)

Develop a vehicle fleet analysis tool.

### Dataset Link

https://archive.ics.uci.edu/dataset/9/auto+mpg

---

## 8. Electric Vehicle Energy Consumption Data

### Description

Simplified datasets can include:

- Vehicle identifier
- Battery capacity
- Distance travelled
- Energy consumption

### Educational Value

Links programming to modern automotive engineering challenges.

### Example Programming Tasks

Students calculate:

- Remaining vehicle range
- Fleet efficiency
- Charging requirements

---

## 9. Formula Student Telemetry Data

### Description

Typical variables include:

- Vehicle speed
- Battery voltage
- Motor temperature
- Lap time

### Educational Value

Provides highly engaging engineering data.

### Example Programming Tasks

Students:

- Detect overheating events
- Calculate average speed
- Determine fastest lap
- Generate warning messages

---

# Recommended Dataset Usage Across the Module

| Lab | Programming Topic | Engineering Dataset |
|------|------|------|
| 1 | Variables, arithmetic, input/output | Synthetic engineering calculations |
| 2 | Selection and decision making | PhysioNet heart-rate data |
| 3 | Loops and repetition | EV battery monitoring or patient monitoring data |
| 4 | Lists and data processing | Concrete Strength and Auto MPG datasets |
| 5 | Functions and modular programming | Reusable functions operating on previous datasets |
| 6 | Integrated engineering project | Concrete Strength, VitalDB or Auto MPG dataset |

---

# Recommended Core Dataset Set

To minimise preparation effort while maximising engineering relevance, the following three datasets provide excellent coverage across the entire module:

### Materials Engineering

**Concrete Compressive Strength Dataset**
https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength
【1-7f8f34】【2-e1edbc】

### Biomedical Engineering

**PhysioNet Physiological Monitoring Datasets**
https://physionet.org/
【4-9a2a7b】【5-25154b】

### Automotive Engineering

**Auto MPG Dataset**
https://archive.ics.uci.edu/dataset/9/auto+mpg
【8-c12b9f】【9-9a95ec】

Together, these datasets provide authentic engineering data that supports all six laboratory sessions while remaining accessible to students with limited programming experience.
