# DataWeka

# Application of Data Science to Discover the Relationship Between Dental Caries and Diabetes

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Tool](https://img.shields.io/badge/tool-Weka-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

This project applies data science and machine learning techniques to analyze clinical dental records and uncover patterns linking dental caries and diabetes. The study was conducted using 193 anonymized patient records from the "Luz y Vida" Dental Clinic at Universidad de Montemorelos, Mexico.

## 🧠 Objectives

- Automate the analysis of clinical dental data
- Identify the relationship between diabetes and dental caries using clustering techniques
- Evaluate the use of data science methodologies in healthcare research

## 🛠️ Technologies Used

- **Weka**: Machine learning tool for data mining and clustering
- **IBM Data Science Methodology**: 10-stage process for structured data analysis
- **Manual data digitization**: Transcription of paper-based dental records into structured digital format

## 📊 Methodology

- Applied **K-Means clustering** to find patterns among patient features
- Selected 7 features from the records relevant to dental caries and diabetes
- Ran 5 experiments varying the number of clusters and evaluated results using within-cluster sum of squared errors (WCSS)
- Collaborated with dentists to validate the clinical relevance of the discovered patterns

## 🔍 Key Findings

- Diabetic patients tend to show a higher number of decayed and missing teeth
- The presence of systemic health conditions, such as endocrine disorders, correlates with poorer oral health
- Younger patients showed fewer signs of decay and lower diabetes incidence

## 📈 Dataset

- 193 clinical records from various locations in Mexico and the USA
- Digitized and anonymized for analysis
- Public dataset (if available): [Google Sheets Dataset](https://docs.google.com/spreadsheets/d/1prAv_cj6nFpZejotYje4gpfqjT291vM_tpu9cLTZSGg/edit?usp=sharing)

## 🖼️ Visual Results

![KMeans Clustering Example](assets/kmeans_clusters_example.png)
*Example of clustering results using Weka (K-Means).*  

## 👤 Roles and Contributions

- Data cleaning and digitization
- Feature selection and clustering analysis
- Report writing and documentation of results

## 🧩 Future Work

- Develop a software tool for digital clinical record management
- Expand dataset with more patient features (e.g., nutrition and exercise habits)
- Apply similar methodology to other oral-systemic health relationships

## 📚 Reference Publication

Alférez, G. H., Jiménez, J., Hernández Navarro, H., et al. (2021). *Application of Data Science to Discover the Relationship between Dental Caries and Diabetes in Dental Records*. Universidad de Montemorelos. [ResearchGate](https://www.researchgate.net/publication/352262095)

---

Feel free to clone this repository, contribute with your insights, or reach out for collaboration!

> “Data is not just numbers; it’s stories waiting to be discovered.”
