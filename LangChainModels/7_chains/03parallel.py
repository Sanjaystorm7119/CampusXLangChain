from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

template1 = PromptTemplate(template="generate short and simple notes on \n {text}",input_variables=['text'])
template2 = PromptTemplate(template="generate 5 questions and answers from the following text \n {text}",input_variables=['text'])
template3 = PromptTemplate(template="merge the provided notes and quiz into single doc \n notes -> {notes} and quiz -> {quiz}",input_variables=['notes','quiz'])

model1 = GoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes" : template1 | model1 | parser,
    "quiz" : template2 | model2 | parser
}
)

merge_chain = template3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Scikit-learn (often written scikit-learn or sklearn) is a popular open-source Python library for machine learning. It provides efficient tools for data preprocessing, model training, evaluation, and selection.

⭐ What Scikit-learn Is Used For

Classification (e.g., SVM, Random Forest, Logistic Regression)

Regression (e.g., Linear Regression, Gradient Boosting)

Clustering (e.g., K-Means, DBSCAN)

Dimensionality reduction (e.g., PCA, t-SNE)

Model selection & evaluation (grid search, cross-validation)

Data preprocessing (scaling, encoding, imputation)

📦 Install
pip install scikit-learn

🔧 Simple Example
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate
preds = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))
"""

res = chain.invoke({"text":text})
print(res)
chain.get_graph().print_ascii()