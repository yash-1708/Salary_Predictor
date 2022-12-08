import flask
from flask_cors import CORS
from flask import request
import pickle
from pathlib import Path
import pandas as pd
import json
import warnings
warnings.filterwarnings('ignore')

HERE = Path(__file__).parent
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


def feature_lookup(val):

    x = {"experience_level": {'MI': 2, 'SE': 3, 'EN': 0, 'EX': 1},

         "employee_residence": {'AE': 0, 'AR': 1, 'AT': 2, 'AU': 3, 'BE': 4, 'BG': 5, 'BO': 6, 'BR': 7, 'CA': 8, 'CH': 9, 'CL': 10, 'CN': 11, 'CO': 12, 'CZ': 13, 'DE': 14, 'DK': 15, 'DZ': 16, 'EE': 17, 'ES': 18, 'FR': 19, 'GB': 20, 'GR': 21, 'HK': 22, 'HN': 23, 'HR': 24, 'HU': 25, 'IE': 26, 'IN': 27, 'IQ': 28, 'IR': 29, 'IT': 30, 'JE': 31, 'JP': 32, 'KE': 33, 'LU': 34, 'MD': 35, 'MT': 36, 'MX': 37, 'MY': 38, 'NG': 39, 'NL': 40, 'NZ': 41, 'PH': 42, 'PK': 43, 'PL': 44, 'PR': 45, 'PT': 46, 'RO': 47, 'RS': 48, 'RU': 49, 'SG': 50, 'SI': 51, 'TN': 52, 'TR': 53, 'UA': 54, 'US': 55, 'VN': 56},

         "company_location": {'AE': 0, 'AS': 1, 'AT': 2, 'AU': 3, 'BE': 4, 'BR': 5, 'CA': 6, 'CH': 7, 'CL': 8, 'CN': 9, 'CO': 10, 'CZ': 11, 'DE': 12, 'DK': 13, 'DZ': 14, 'EE': 15, 'ES': 16, 'FR': 17, 'GB': 18, 'GR': 19, 'HN': 20, 'HR': 21, 'HU': 22, 'IE': 23, 'IL': 24, 'IN': 25, 'IQ': 26, 'IR': 27, 'IT': 28, 'JP': 29, 'KE': 30, 'LU': 31, 'MD': 32, 'MT': 33, 'MX': 34, 'MY': 35, 'NG': 36, 'NL': 37, 'NZ': 38, 'PK': 39, 'PL': 40, 'PT': 41, 'RO': 42, 'RU': 43, 'SG': 44, 'SI': 45, 'TR': 46, 'UA': 47, 'US': 48, 'VN': 49},

         "avg_salaries": {'3D Computer Vision Researcher': 5409, 'AI Scientist': 66135.5714285714, 'Analytics Engineer': 175000, 'Applied Data Scientist': 175655, 'Applied Machine Learning Scientist': 142068.75, 'BI Data Analyst': 74755.1666666666, 'Big Data Architect': 99703, 'Big Data Engineer': 51974, 'Business Data Analyst': 76691.2, 'Cloud Data Engineer': 124647, 'Computer Vision Engineer': 44419.3333333333, 'Computer Vision Software Engineer': 105248.666666666, 'Data Analyst': 92893.0618556701, 'Data Analytics Engineer': 64799.25, 'Data Analytics Lead': 405000, 'Data Analytics Manager': 127134.285714285, 'Data Architect': 177873.909090909, 'Data Engineer': 112725, 'Data Engineering Manager': 123227.2, 'Data Science Consultant': 69420.7142857142, 'Data Science Engineer': 75803.3333333333, 'Data Science Manager': 158328.5, 'Data Scientist': 108187.832167832, 'Data Specialist': 165000, 'Director of Data Engineering': 156738, 'Director of Data Science': 195074, 'ETL Developer': 54957, 'Finance Data Analyst': 61896, 'Financial Data Analyst': 275000, 'Head of Data': 160162.6, 'Head of Data Science': 146718.75, 'Head of Machine Learning': 79039, 'Lead Data Analyst': 92203, 'Lead Data Engineer': 139724.5, 'Lead Data Scientist': 115190, 'Lead Machine Learning Engineer': 87932, 'ML Engineer': 117504, 'Machine Learning Developer': 85860.6666666666, 'Machine Learning Engineer': 104880.146341463, 'Machine Learning Infrastructure Engineer': 101145, 'Machine Learning Manager': 117104, 'Machine Learning Scientist': 158412.5, 'Marketing Data Analyst': 88654, 'NLP Engineer': 37236, 'Principal Data Analyst': 122500, 'Principal Data Engineer': 328333.333333333, 'Principal Data Scientist': 215242.428571428, 'Product Data Analyst': 13036, 'Research Scientist': 109019.5, 'Staff Data Scientist': 105000, 'Others': 121813.243989117}}

    return x[val]


def feature_create(json):

    # Experience_level

    el_val = feature_lookup('experience_level')

    json_val = json['employment_type']

    experience_level = el_val[json_val]

    # Employee Residence

    el_val = feature_lookup('employee_residence')

    json_val = json['employee_residence']

    employee_residence = el_val[json_val]

    # Company_location

    el_val = feature_lookup('company_location')

    json_val = json['company_location']

    company_location = el_val[json_val]

    # Company_location

    el_val = feature_lookup('avg_salaries')

    json_val = json['job_title']

    avg_salaries = el_val[json_val]

    if (json['company_size'] == 'Small'):

        company_size_large = 0

        company_size_medium = 0

        company_size_small = 1

    elif (json['company_size'] == 'Medium'):

        company_size_large = 0

        company_size_medium = 1

        company_size_small = 0

    elif (json['company_size'] == 'Large'):

        company_size_large = 1

        company_size_medium = 0

        company_size_small = 0

    temp_df = {'experience_level': experience_level,

               'employee_residence': employee_residence,

               'remote_ratio': json['remote_ratio'],

               'company_size_large': company_size_large,

               'company_size_medium': company_size_medium,

               'company_size_small': company_size_small,

               'company_location': company_location,

               'Average_salary_for_job_titles': avg_salaries}

    return pd.DataFrame(temp_df, index=[0])


@app.route('/predict', methods=['POST'])
def home():
    if request and request.data:
        json_data = json.loads(request.data)
        resultsdf = feature_create(json_data)
        print(resultsdf)
        path = 'random_forest.pickle'
        model = pickle.load(open(HERE/path, 'rb'))
        print(model.predict(resultsdf)[0])
        return {'salary': model.predict(resultsdf)[0]}
    else:
        return "Hello World"


app.run()
