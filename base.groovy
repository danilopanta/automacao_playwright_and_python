pipeline {
  agent {
    kubernetes {
      inheritFrom 'qa'
      defaultContainer 'jenkins-agent'
    }
  }

  triggers {
    cron('H 9 * * 1-5')
  }

  parameters {
    // Define choice parameter for config vars
    choice(
      name: 'config_vars',
      choices: ['cred_qa_uat', 'cred_qa_rc'],
      description: 'Where you set config vars'
    )
    // Define string parameter for the branch to clone poject
    choice(
      name: 'branch',
      choices: ['develop', 'main'],
      description: 'Where you set branch'
    )
    // Define string parameter for the command to run tests
    string(
      name: 'command_run',
      defaultValue: 'pytest -n auto',
      description: 'Where you set command run test'
    )
    // Define string parameter for the tag to run tests
    string(
      name: 'tag_run',
      defaultValue: '',
      description: 'Where you set tag test'
    )
  }

  stages {
    stage('CLEANING WORKDIR') {
      steps {
        // Clean workspace directory
        deleteDir()
      }
    }

    stage('CLONE PROJECT') {
      steps {
        script {
          // Clone the repository and adjust permissions
          sh "git clone git@ssh.dev.azure.com:v3/Orbia/Engineering/base-pw-py-qa --depth 1 -b ${params.branch}"
          sh "chmod 777 base-pw-py-qa -R"
        }
      }
    }

    stage('INSTALL DEPENDENCIES') {
      steps {
        script {
          dir('base-pw-py-qa') {
            // Install Python dependencies and Playwright
            sh "pip install -r requirements.txt"
            sh "playwright install"
          }
        }
      }
    }

    stage('RUNNING PLAYWRIGHT TESTS') {
      steps {
        script {
          dir('base-pw-py-qa') {
            // Load configuration file and set environment variables
            configFileProvider([configFile(fileId: "${params.config_vars}", variable: "cred_qa")]) {
              def envFileContent = readFile "${cred_qa}"
              def envFileLines = envFileContent.readLines()

              envFileLines.each {
                line ->
                  def(key, value) = line.tokenize('=')
                env.
                "${key}" = value
              }
              // Build the command string based on conditions
              def commandString = "${params.command_run}"
              if (params.tag_run) {
                commandString += " -k ${params.tag_run}"
              }

              // Run tests with the command string
              sh commandString
            }
          }
        }
      }
    }
  }

  post {
    success {
      echo 'BUILD SUCCESSFUL!'
    }
    failure {
      echo 'BUILD FAILED!'
    }
    always {
      echo "TESTS FINISHED"
      sh 'allure --version'
      sh 'mkdir -p ${WORKSPACE}/allure-results && cp -R base-pw-py-qa/reports/allure-results/* ${WORKSPACE}/allure-results'
      sh 'chmod -R 777 ${WORKSPACE}/allure-results'
      allure([
        includeProperties: true,
        jdk: '',
        reportBuildPolicy: 'ALWAYS',
        results: [
          [path: 'allure-results']
        ]
      ])
    }
  }
}