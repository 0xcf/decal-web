pipeline {
  agent {
    label 'slave'
  }

  options {
    ansiColor('xterm')
    timeout(time: 1, unit: 'HOURS')
    disableConcurrentBuilds()
  }

  stages {
    stage('check-gh-trust') {
      steps {
        checkGitHubAccess('0xcf')
      }
    }

    stage('bundle') {
      steps {
        sh 'make bundle'
      }
    }

    stage('build') {
      steps {
        echo "Building branch ${env.BRANCH_NAME}"
        sh 'make build'
      }
    }

    stage('deploy') {
      parallel {
        stage('building master') {
          when {
            branch 'master'
          }
          steps {
            sshagent (credentials: ['decal-ssh-key']) {
              sh 'make deploy'
            }
          }
        }
        stage('building branch') {
          when {
            not {
              branch 'master'
            }
          }
          steps {
            sshagent (credentials: ['decal-ssh-key']) {
              sh "make deploy DEPLOY_DIR=public_html/pr/${env.BRANCH_NAME}"
            }
            script {
               pullRequest.comment("Deploy Preview: https://decal.ocf.io/pr/${env.BRANCH_NAME}")
            }
          }
        }
      }
    }
  }

  post {
    always {
      node(label: 'slave') {
        ircNotification('#decal-spam')
      }
    }
  }
}

// vim: ft=groovy
