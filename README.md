# Fake News Categorization Using Machine Learning - Accenture 



---

### 👥 **Team Members**



| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Stephanie Argueta| @ssva179      | GPT model development and evaluation, Streamlit App, model training, results interpretation                    |
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

**You might consider describing the following (as applicable):**

* Performance metrics (e.g., Accuracy, F1 score, RMSE)
* How your model performed
* Insights from evaluating model fairness

**Potential visualizations to include:**

* Confusion matrix, precision-recall curve, feature importance plot, prediction distribution, outputs from fairness or explainability tools

---

## 🚀 **Next Steps**

**You might consider addressing the following (as applicable):**

* What are some of the limitations of your model?
* What would you do differently with more time/resources?
* What additional datasets or techniques would you explore?

---

## 📝 **License**

If applicable, indicate how your project can be used by others by specifying and linking to an open source license type (e.g., MIT, Apache 2.0). Make sure your Challenge Advisor approves of the selected license type.

**Example:**
This project is licensed under the MIT License.

---

## 📄 **References** (Optional but encouraged)

Cite relevant papers, articles, or resources that supported your project.

---

## 🙏 **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor, host company representatives, TA, and others who supported your project.

