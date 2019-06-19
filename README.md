# CTiv3

## Getting started

```bash
docker build -t ctiv3 .
docker run -p 80:5000 --volume=$PWD:/app --name ctiv3 --rm ctiv3
```
and go to http://localhost/

## Development

Install packages & update requirements:
```bash
# Check for outdated packages
docker exec -it ctiv3 pip list --outdated

# Install package with specific version
docker exec -it ctiv3 pip install 'package==1.2.3'

# And store installed packages in requirements for next docker build
docker exec -it ctiv3 pip freeze --all > requirements.txt
```