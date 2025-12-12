# Fake News Categorization Using Machine Learning - Accenture 



---

### 👥 **Team Members**



| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Stephanie Argueta| @ssva179      | GPT-3.5-turbo model development and evaluation, Streamlit App, model training, performance analysis results interpretation                    |
| Aditi Dheer      | @aditi-dheer  | Data collection, exploratory data analysis (EDA), dataset documentation, **Logistic Regression** model development & evaluation, performance analysis, model training, results interpretation  |
| Amie Feng        | @amiefeng     | DeBERTa model development & evaluation, performance analysis, model training, results interpretation           |
| Jibek Kelgenbaeva| @kjibek       | Dataset cleaning, DeBERTa model development & evaluation, performance analysis, model training, results interpretation           |
| Zunaer Sharang   | @zunaersharang| Model evaluation, performance analysis, results interpretation           |



---

## 🎯 **Project Highlights**

- Built a three-model Fake News Detection System using  `Logistic Regression`, `DeBERTa`, and a `GPT-3.5-turbo` to evaluate credibility and classify articles as  `TRUE` or `FAKE`.
- Achieved at least  `~90%` accuracy across all models, demonstrating strong performance and the potential for AI-driven misinformation detection solutions.
- Generated actionable insights to inform business decisions at `Accenture`.
- Implemented scalable ML techniques including traditional ML and transformers to address industry constraints or expectations.

---

## 👩🏽‍💻 **Setup and Installation**
> **Note:** All notebooks were originally developed in Google Colab. You can run them locally or open them directly in Colab for convenience.


To get started, clone the repository to your local machine:

- `git clone https://github.com/Accenture-AI-Studio/fake-news.git`
- `cd fake-news`

### **Set Up Python Environment**

Create and activate a Python virtual Environment

**On macOS/Linux:**
- `python3 -m venv venv`
- `source venv/bin/activate`

**On Windows:**
- `python3 -m venv venv`
-  `venv\Scripts\activate`

**Install Dependencies**
- `pip install -r requirements.txt`

### **Access the Dataset**
The dataset used in this project is publicly avaliable on Kaggle
Download the dataset from the link below and place the CSV files in the appropriate place.

**Kaggle Dataset Link:**
👉 https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets/data

### **Run Notebooks and Scripts**
Launch Jupyter Notebook and navigate to the appropriate directory to begin analysis:
- `juputer notebook`

Then open the notebooks(e.g. Logistic_Regression_Model.ipynb, FakeNewsDetectionwithGPT.ipynb, Cleaned_Dataset_Deberta.ipynb) located in the repository. 

---

## 🏗️ **Project Overview**

This project was conducted through the Break Through Tech AI Program as part of AI Studio. From September to December 2025, we collaborated on a Challenge Project presented by Accenture and concluded the project with a final presentation to company stakeholders.

Our team’s objective was to build a binary classifier capable of labeling articles as true or fake and to evaluate the trustworthiness of each article using a customized trust score. To achieve this, we implemented multiple AI approaches, including traditional machine learning models, a transformer-based DeBERTa model, and a GPT classifier. 

Effective misinformation detection has significant real-world relevance, as inaccurate information can influence public opinion, decision-making, and organizational risk. By developing these models this project demonstrates how AI can support stakeholders identify unreliable content and strengthen information integrity.

---

## 📊 **Data Exploration**

**You might consider describing the following (as applicable):**

* The dataset(s) used: origin, format, size, type of data
* Data exploration and preprocessing approaches
* Insights from your Exploratory Data Analysis (EDA)
* Challenges and assumptions when working with the dataset(s)

**Potential visualizations to include:**

* Plots, charts, heatmaps, feature visualizations, sample dataset images

---

## 🧠 **Model Development**

***We implemented and evaluated three models to approach fake news detection**

**1. Logistic Regression(Baseline)**
- TF-IDF vectorization of article text
- Logistic Regression classifier implemented using scikit-learn
- Served as a strong, interpretable baseline
  
**2. DeBERTa Transformer**
- Fine-tuned a pre-trained DeBERTa model on the labeled dataset
- Tokenization and batching performed using HuggingFace Transformers
- Used embeddings to capture semantic relationships in text
  
**3. GPT-Based Prompt Approach**
- Used GPT-3.5-turbo via API calls
- Designed structured prompts to elicit credibility reasoning and classification
- Explored LLM performance without direct parameter fine-tuning
  
We evaliated all moders using standard evaluation metrics like accuracy and F1 scores to assess peformance and generalization.

---

## 📈 **Results & Key Findings**

-Findings suggest that AI can reliably support automated moderation and flag misleading articles. 
- All three models achieved strong classification performance, with accuracy and F1 scores consistently around or above ~90%.
- The Logistic Regression model served as a strong and interpretable baseline, demonstrating that traditional ML techniques remain competitive for text classification tasks. (~99%)
- The fine-tuned DeBERTa model showed the most stable generalization across article types, benefiting from contextual language representations.  (~99%)
- The GPT-based prompt approach demonstrated promising reasoning capabilities, but exhibited higher difference in predictions compared to the fine-tuned models. (~90%)
- Model performance was strongly influenced by the characteristics of the training dataset, highlighting the importance of data quality and curation when building specialized classifiers, which we attribute to the very high accuracy.

**Model Comparisons:**

![Evaluation Metrics](image.png)

---

## 🚀 **Next Steps**

- Diversify training data by incorporating additional datasets (include broader sources, stylistic writing, time period, and news topics) to increase fact-checking and decrease leakage and improve overall generalization. 
- Find weaknesses in our models by performing in-depth error checking and reasoning. 

---
## 👾 **TRY OUR DEMO**
- Try our interactive website, where you can paste an article and see how our model will classify it.  

👉 [Live Demo](https://fake-newss.streamlit.app)

![Demo Website](web.png) 

---

## 📝 **License**

This project is licensed under the MIT License.

---

## 📄 **References** 
Kaggle Fake News Dataset: (https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets/data)


---

## 🙏 **Acknowledgements** 

We would like to thank our Break Through Tech AI Studio Coach Vasu Kaker and Challenge Advisor Lipika Mukherjee from Accenture for their guidance and feedback throughout the project, as well as other industry professionals who provided valuable context and evaluation during project reviews.

