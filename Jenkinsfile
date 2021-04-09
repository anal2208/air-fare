pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                bat 'python -m pip install -r requirements.txt --user'
                echo 'Build Done'
                
            }
        }
       
        
                stage('Run'){
                     steps{
                        bat 'streamlit run st.py'
                        echo 'Success'
            }
                }

    }
}
