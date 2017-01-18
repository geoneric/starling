set -e


rm -f api/*rst && sphinx-apidoc --separate -o api ../../source/starling
make html
