LISTEN_IP := 0.0.0.0
RANDOM_PORT := $(shell expr $$(( 8000 + (`id -u` % 1000) + 2 )))

.PHONY: dev
dev: bundle
	bundle exec jekyll serve --host $(LISTEN_IP) -P $(RANDOM_PORT)

.PHONY: local-dev
local-dev: LISTEN_IP=127.0.0.1
local-dev: dev

.PHONY: local-dev
local-dev: bundle
	bundle exec jekyll serve

.PHONY: bundle
bundle:
	bundle install --deployment

.PHONY: build
build:
	bundle exec jekyll build --verbose --trace

.PHONY: clean
clean:
	rm -rf .bundle vendor

.PHONY: deploy
deploy:
	rsync -avzpce "ssh -o StrictHostKeyChecking=no" --del _site/ --exclude static decal@ssh.ocf.berkeley.edu:public_html
