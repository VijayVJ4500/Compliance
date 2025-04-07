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

        stage('Create Virtualenv') {
            steps {
                bat '"%PYTHON%" -m venv venv'
            }
        }

        stage('Install Requirements') {
            steps {
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt && pip install allure-pytest pytest-html'
            }
        }
        stage('Prepare') {
          steps {
             bat 'copy config.ini test_runfile\\config.ini'
          }
        }


        stage('Run Tests') {
            steps {
                withEnv(["PYTHONPATH=test_runfile"]) {
                    bat 'call .\\venv\\Scripts\\activate && pytest test_runfile\\test_end_to_end.py --html=Reports/report.html --self-contained-html --alluredir=allure-results'
                }
            }
        }
    }

    post {
        always {
            // Publish HTML Report
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'Reports',
                reportFiles: 'report.html',
                reportName: 'HTML Report'
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
