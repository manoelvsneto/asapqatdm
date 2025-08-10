# asapqatdm
Agile Software Architecture: Perceptions on Quality and Architectural Technical Debt Management

This repository contains files for both qualitative and quantitative analysis of responses from the study on Software Architecture, Quality, and Architectural Technical Debt Management. Files are organized according to the corresponding Research Questions (RQs).

Accepted paper at SBCARS 202:  
https://cbsoft.sbc.org.br/2025/sbcars/artigos/?lang=pt

---

## File Overview and Relation to Research Questions

### RQ1, RQ2, RQ3 – Participant Experience

- **experience_analysis.py**  
  Processes participant experience data, converts months to years, and generates descriptive statistics.  
  *Purpose:* Answers RQs about respondents' professional experience in different roles/contexts.

- **experience_data_years.csv**  
  Dataset with experience values converted to years.  
  *Purpose:* Used as input/output for the above script.

### RQ4 – Quality Attribute Prioritization

- **RQ4.CSV**  
  Raw dataset of participants’ selection of quality attributes.  
  *Purpose:* Input for prioritization analysis.

- **rq4.py**  
  Processes RQ4.CSV to generate AHP (Analytic Hierarchy Process) ranking and bar chart of normalized weights.  
  *Purpose:* Answers RQ4 about which quality attributes are prioritized.

- **rq4.ipynb**  
  Jupyter Notebook version of the RQ4 analysis for interactive exploration.

### RQ5 – Strategies for Handling Architectural Technical Debt

- **rq5_answers.md**  
  Textual responses to the open-ended question about managing architectural technical debt.

- **rq5_details.md**  
  Additional details/context from participant responses.  
  *Purpose:* Input for qualitative coding and pattern identification.

### RQ6 – Architecture Evaluation Methods

- **rq6_answers.md**  
  Textual responses on how participants evaluate architecture.

- **rq6.ipynb**  
  Jupyter Notebook for processing and analyzing RQ6 responses.

### RQ7 – Architectural Technical Debt Management

- **rq7_answers.md**  
  Original textual responses for RQ7.

- **Q7_Category-Respondent-Response_Network.csv**  
  Qualitative network mapping Category → Respondent → Response.  
  *Purpose:* Used for network visualizations and co-occurrence analysis.

### RQ8 – Architecture Evaluation

- **rq8_answers.md**  
  Original textual responses for RQ8.

- **Q8_Category-Respondent-Response_Network.csv**  
  Qualitative network for RQ8 categories.


