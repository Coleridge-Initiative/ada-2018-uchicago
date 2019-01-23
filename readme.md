# Applied Data Analytics

The [Coleridge Initiative](https://coleridgeinitiative.org)'s Applied Data Analytics training program held at the University of Chicago in Summer 2018.

### Projects
This program built on top of the previous programs - especially the program on [Economic Development held in Kansas City, MO](https://github.com/Coleridge-Initiative/ada-2018-kcmo) - and the content centered on around two example projects:
1. Economic Development - predicting survivability of Firms
2. Economic Development - exploring metrics of economic activity

### Training program agenda
- July 18 - Program introduction
  - 9:00-10:30 Welcome & Introductions
  - 10:30-11 Break
  - 11-12:00 NYU's Administrative Data Research Facility (ADRF) - Security training, data agreements, and brief demo
  - 12:00-1:00 Lunch
  - 1:00-1:30 Hands introduction to ADRF
  - 1:30-4:00 Projects and scoping
- July 19 - Data exploration & Visualization
  - 9:00-10:30 Introduction to Databases
  - 10:30-10:45 Break
  - 10:45-12:00 Hands on exploration of datasets
  - 12:00-1:00 Lunch
  - 1:00-2:30 Data visualization (lecture)
  - 2:30-4:00 Data visualization (exercises)
- July 20 - Record Linkage
  - 9:00-9:30 Measurement and Description
  - 9:30-10:45 Record Linkage
  - 10:45-11:00 Break
  - 11:00-12:00 Record Linkage
  - 12:00-1:00 Lunch
  - 1:00-4:00 Hands on data exploration in Python
- July 23 - Introduction to Machine Learning
  - 10:00-11:30 Introduction to Machine Learning
  - 11:30-12:00 Break
  - 12:00-1:00 Machine Learning
  - 1:00-2:00 Lunch
  - 2:00-4:00 Machine Learning model evaluation
  - 4:00-5:00 Project discussion and data exploration
- July 24 - Text Analysis and Network Analysis
  - 10:00-11:30 Introduction to Network Analysis
  - 11:30-11:45 Break
  - 11:45-1:00 Network Analysis
  - 1:00-2:00 Lunch
  - 2:00 - 3:45 Text Analysis
  - 3:45 - 5:00 Text Analysis
- Sept 5 - Machine Learning Deep Dive
  - 10:00 - 10:30: Welcome back, Recap of Week 1, and Goals for this week
  - 10:30 - 11:00: Machine Learning Recap
  - 11:00 - 1:00: Machine Learning Lecture
  - 1:00 - 2:00: Lunch
  - 2:00 - 3:00: Machine Learning notebook
  - 3:00 - 5:00: Project work
- Sept 6 - Inference
  - 10:00 - 11:30 Inference lecture
  - 11:30 - 12:00 Break
  - 12:00 - 1:00 Inference notebook
  - 1:00 - 2:00 Lunch
  - 2:00 - 5:00 Project work
- Sept 7: Machine Learning in Practice
  - 10:00 - 11:00 Group discussion of team projects
  - 11:00 - 11:15 Break
  - 11:15 - 1:00 Machine Learning in Practice
  - 1:00 - 2:00 Lunch
  - 2:00 - 5:00 Project work
- Sep 10: Privacy and Confidentiality
  - 10:00 - 11:30 Privacy and confidentiality lecture
  - 11:30 - 11:45 Break
  - 11:45 - 1:00 ADRF Disclosure review & Export requests
  - 1:00 - 2:00 Lunch
  - 2:00 - 5:00 Project work
- Sep 11: Ethics & Interim presentations
  - 10:00 - 11:30 Ethics, Bias, and Fairness in Machine Learning Systems
  - 11:30 - 11:45 Break
  - 11:45 - 1:00 Project work
  - 1:00 - 2:00 Lunch
  - 2:00 - 3:00 Interim presentations and instructor comments/feedback (~10 minutes total per team)
  - 3:00 - 5:00 Project work

#### Presentations Friday, September 28
- 11:00 - 11:30 Team 1: WIA Youth Employment Outcomes
- 11:30 - 12:00 Team 2: Firm Survivability in Illinois
- 12:00 - 12:30 Team 6: Employer survivability
- 12:30 - 1:00 Team 4: 1-year survivability of small businesses in Illinois
- 1:00 - 1:30 Team 3: Predicting which firms will have high-turnover of low-wage workers
- 1:30 - 2:00 Team 5: Firm survivability across IL Economic Development Regions

### Datasets
The primary datasets used in the program were all stored in the PostgreSQL database called `appliedda` on the [ADRF](https://coleridgeinitiative.org/computing); the datasets are:
1. Quarterly Census of Employment and Wages (QCEW) - this is a federally mandated program, and it is also used in conjunction with the Unemployment Insurance program at the Census Bureau to produce the Longitudinal Employer Household Dynamics datasets. There are two data tables associated with the QCEW dataset and this program had access to both for IL and MO:
  + Business data - in the program database the tables are `kcmo_lehd.mo_qcew_employers` and `il_des_kcmo.il_qcew_employers`
  + Job data -  in the program database the tables are `kcmo_lehd.mo_wage` and `il_des_kcmo.il_wage`
2. Illinois Department of Corrections - this data is from administering State prisons and includes tables for:
  + Admissions to prison - `il_doc_kcmo.ildoc_admit`
  + Exits from prison - `il_doc_kcmo.ildoc_exit`
  + and some auxiliary tables for code definitions and parolees
3. Illinois Department of Human Services - the class will also have access to case data from IDHS on administering TANF, SNAP, and cash assistance programs; these data are in the `il_dhs` schema

### Folder structure:
- `notebooks_business_vitality` has example notebooks used in the in-person training sessions, notebooks are geared more towards the project of predicting Firm survivability
- `notebooks_dashboard` shows an initial set of notebooks working up to a dashboard. As no teams in this program elected to do a dashboard project the example notebooks were only created for the first week
- `additional_content` has notebooks used in previous programs for extra examples or to demonstrate content not covered in this program (eg APIs)
- `cheat_sheets` has a collection of reference material, generally created by others outside of the Applied Data Analytics program context
- `data_prep` has a couple notebooks used to prepare the sample data for the program
