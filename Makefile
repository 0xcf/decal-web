.PHONY: dev
dev: bundle
	bundle exec jekyll serve --host 0.0.0.0

.PHONY: local-dev
local-dev: bundle
	bundle exec jekyll serve

.PHONY: bundle
bundle:
	bundle install --deployment

.PHONY: clean
clean:
	rm -rf .bundle vendor
