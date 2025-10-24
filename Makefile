.PHONY: build clean serve

build:
	@echo "Building index.html from tutorials.yaml..."
	@python3 build_index.py

clean:
	@echo "Removing generated index.html..."
	@rm -f index.html

serve: build
	@echo "Starting local server at http://localhost:8000"
	@python3 -m http.server 8000
