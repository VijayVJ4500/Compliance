pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/python-test-project.git'
            }
        }

        stage('Set up Python Env') {
            steps {
                sh 'python3 -m venv ${VENV_DIR}'
                sh './${VENV_DIR}/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Choose one depending on your reporting
                // HTML report
                sh './${VENV_DIR}/bin/pytest --html=report.html'

                // OR Allure
                // sh './${VENV_DIR}/bin/pytest --alluredir=allure-results'
            }
        }

        stage('Publish Report') {
            steps {
                // For HTML Report
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: "Test Report"
                ])

                // For Allure Report
                // allure([
                //     includeProperties: false,
                //     jdk: '',
                //     results: [[path: 'allure-results']]
                // ])
            }
        }
    }
}
