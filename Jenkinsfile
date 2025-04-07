pipeline {
    agent any

    tools {
        python 'Python3.10' // Ensure this matches your Jenkins Python installation name
    }

    environment {
        ALLURE_HOME = "${tool 'Allur_Home'}"
        PATH = "${env.PATH}:${env.ALLURE_HOME}/bin"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Python test
                sh 'python all_tests.py'
            }
        }

        stage('Generate HTML Report') {
            steps {
                // You need to configure HTML report generation inside your test script or separately
                publishHTML(target: [
                    reportDir: 'Reports',
                    reportFiles: 'index.html',
                    reportName: 'HTML Report'
                ])
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results -c -o allure-report'
            }
        }

        stage('Archive Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml' // If you’re using JUnit XML (optional)
            archiveArtifacts artifacts: 'Reports/**', allowEmptyArchive: true
        }

        failure {
            echo 'Build failed!'
        }

        success {
            echo 'Build completed successfully!'
        }
    }
}
