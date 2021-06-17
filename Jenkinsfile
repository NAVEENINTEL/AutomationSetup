pipeline {
  agent any

  stages {
      
    stage('Environment setup') {
      steps {
        // Clean the workspace
        echo "Environment setup" 
        //tool name: 'python', type: 'jenkins.plugins.shiningpanda.tools.PythonInstallation'
      }
    }

    stage('Build') {
      steps {
          echo "Build"
          build 'Regression'
        // build, build stages can be made in parallel aswell
        // build stage can call other stages
        // can trigger other jenkins pipelines and copy artifact from that pipeline
      }
    }

    stage('Test') {
      steps {
        // Test (Unit test / Automation test(Selenium/Robot framework) / etc.)
        echo "Testing"
        git 'https://github.com/NAVEENINTEL/AutomationSetup.git'
        bat '''pip install -r requirements.txt
              python -m pytest  -v -s  --alluredir=localReport'''
   
      }
    }

//     stage('Deploy') {
//       steps {
//           echo "Deploy"
//         // Deploy to cloud providers /local drives /artifactory etc.
//         // Deploy to Deploy/prod /test/ etc
//       }
//     }
    }

  post {
    success {
      echo "SUCCESS"
      allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
      echo "${env.BUILD_ID} on ${env.JENKINS_URL}"
    }
    failure {
      echo "FAILURE"
      echo "${env.BUILD_ID} on ${env.JENKINS_URL}"
    }
    changed {
      echo "Status Changed: [From: $currentBuild.previousBuild.result, To: $currentBuild.result]"
    }
  }
}
