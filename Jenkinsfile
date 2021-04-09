pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip install opencv-python'
                sh 'pip install streamlit'
                echo 'Building done!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing....'
                sh 'pip install opencv-python'
                sh 'pip install streamlit'
                sh 'pip list'
                sh 'streamlit run st.py'
                echo 'Testing done!'
            }
        }
    }
}
