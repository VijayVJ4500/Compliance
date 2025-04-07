pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\vijay\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"%PYTHON%" -m venv venv'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'venv\\Scripts\\activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Run Pytest and Generate Reports') {
            steps {
                withEnv(["PYTHONPATH=hrm_automation"]) {
                    bat 'venv\\Scripts\\activate && pytest hrm_automation/tests --html=Reports/report.html --self-contained-html --alluredir=allure-results'
                }
            }
        }
    }

    post {
        always {
            // Publish HTML Report
            publishHTML([
                reportDir: 'Reports',
                reportFiles: 'report.html',
                reportName: 'HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])

            // Publish Allure Report
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
