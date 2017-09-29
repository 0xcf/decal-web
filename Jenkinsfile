try {
    node('slave') {
        step([$class: 'WsCleanup'])

        stage('check-out-code') {
            checkout scm
        }

        // TODO: Add a testing step to lint any HTML, etc.
        // stage('test') {
        //     sh 'make test'
        // }

        stash 'src'
    }


    if (env.BRANCH_NAME == 'master') {
        node('deploy') {
            step([$class: 'WsCleanup'])
            unstash 'src'

            stage('bundle') {
                steps {
                    sh 'bundle install --deployment'
                }
            }

            stage('build') {
                steps {
                    sh 'bundle exec jekyll build --verbose --trace'
                }
            }

            stage('deploy') {
                sshagent (credentials: ['decal-ssh-key']) {
                    // The positions of the slashes are important here:
                    // There should be a slash after _site BUT not after
                    // public_html.
                    sh 'rsync -avzp --del _site/ decal@ssh.ocf.berkeley.edu:public_html'
                }
            }
        }
    }

} catch (err) {
    def subject = "${env.JOB_NAME} - Build #${env.BUILD_NUMBER} - Failure!"
    def message = "${env.JOB_NAME} (#${env.BUILD_NUMBER}) failed: ${env.BUILD_URL}"

    if (env.BRANCH_NAME == 'master') {
        slackSend color: '#FF0000', message: message
        mail to: 'root@ocf.berkeley.edu', subject: subject, body: message
    } else {
        mail to: emailextrecipients([
            [$class: 'CulpritsRecipientProvider'],
            [$class: 'DevelopersRecipientProvider']
        ]), subject: subject, body: message
    }

    throw err
}

// vim: ft=groovy
