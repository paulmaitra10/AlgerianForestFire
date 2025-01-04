<h1 align="center" id="title">🌳🔥Algerian Forest Fire Prediction</h1>


<p id="description">This project predicts the Fire Weather Index (FWI) a key indicator used to estimate forest fire risks. Multiple machine learning models were explored with the Random Forest Regressor achieving the best performance with a 97.75% accuracy score.</p>
<br>

<h2>🔥Introduction</h2>
<p>The Algerian Forest Fire Prediction project aims to predict the Fire Weather Index (FWI) using machine learning techniques. The FWI is computed from weather conditions like temperature, humidity, wind speed, and precipitation. Multiple models were evaluated, and Random Forest Regressor provided the best accuracy.</p>
<br>

<h2>📊Dataset</h2>
<p>The dataset includes 244 instances that regroup a data of two regions of Algeria,namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.
122 instances for each region.

The period from June 2012 to September 2012. The dataset includes 11 attribues and 1 output attribue (class) The 244 instances have been classified into fire(138 classes) and not fire (106 classes) classes.</p>
<br>
<h2>⚙️Installation Steps:</h2>

<p>1. Clone this repository</p>

```
git clone https://github.com/yourusername/algerian-forest-fire-prediction.git
```

<p>2. Navigate to the project directory</p>

```
cd algerian-forest-fire-prediction
```

<p>3. Install the required packages</p>

```
pip install -r requirements.txt
```

<p>4. Test the model locally</p>

```
python app/app.py
```

  <br>

  <h2>📁Project Structure</h2>

* <b>dataset/</b>: Contains the dataset in CSV format.

* <b>models/</b>: Saved model file (after training).

* <b>notebooks/</b>: Jupyter notebooks for exploratory data analysis and model training.
* <b>src/</b>: Contains all the Python scripts, including model training and evaluation.

* <b>app.py/</b>: Deployment code, including Flask or other web frameworks.

* <b>README.md</b>: This file.

* <b>requirements.txt</b>: List of dependencies required to run the project.

<br>
<h2>🤖 Models Used</h2>

The following machine learning models were implemented:

*   Linear Regression
*   Support Vector Machine (SVR)
*   Decision Tree Regressor
*   Random Forest Regressor (Best model)

<br>
<p>Performance metrics like Mean Squared Error (MSE), R² score, and accuracy were used to evaluate the models.</p>
<br>
<h2>🔍 Feature Selection</h2>

<p>Although the dataset included multiple features, only the most important ones were used for prediction. Feature importance was determined using machine learning techniques, ensuring that the most relevant meteorological variables were considered to optimize the model’s performance.</p>

<br>



<br>
<h2>✅ Conclusion</h2>

<p>his project showcases how machine learning techniques can predict the Fire Weather Index with high accuracy, helping in forest fire risk prediction. The Random Forest Regressor was identified as the best-performing model in this project.</p>
<br>
