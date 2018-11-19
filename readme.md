# Applied Data Analytics

The [Coleridge Initiative](https://coleridgeinitiative.org)'s Applied Data Analytics training program held at the University of Chicago in Summer 2018.

### Projects
This program built on top of the previous programs - especially the program on [Economic Development held in Kansas City, MO](https://github.com/Coleridge-Initiative/ada-2018-kcmo) - and the content centered on around two example projects:
1. Economic Development - predicting survivability of Firms
2. Economic Development - exploring metrics of economic activity

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
