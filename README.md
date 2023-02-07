# django_blog

This is a simple application to learn the basic of Django along with Elasticsearch.

## Description
If you want to start with Django. You can follow the steps here written.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals


## Installation and Configure
__install pip lib__
`pip install -r requirements.txt`

### To install elasticsearch follow the steps with Docker
<a href="https://levelup.gitconnected.com/how-to-run-elasticsearch-8-on-docker-for-local-development-401fd3fff829">How to install elastic search with Docker in local system</a>

__to create network__
`docker network create elastic`

__to create container__
`docker run \
      --name elasticsearch \
      --net elastic \
      -p 9200:9200 \
      -e discovery.type=single-node \
      -e ES_JAVA_OPTS="-Xms200m -Xmx200m"\
      -e xpack.security.enabled=false \
      -e xpack.security.http.ssl.enabled=false \
      -e xpack.security.transport.ssl.enabled=false \
      -it \
      docker.elastic.co/elasticsearch/elasticsearch:8.6.1`

__to test__
`curl -X GET "localhost:9200"`

__Then follow these command to your root folder in different tab if terminal__

Migrations: `python manage.py makemigrations`
Migrate: `python manage.py migrate`
Seed: `python manage.py create_seed_data`
Superuser: `python manage.py createsuperuser`
Indexing elasticsearch: `./manage.py search_index --rebuild`
Run the server: `python manage.py runserver`

__to run a shell for this django application__
From the root folder of the project run this command `python manage.py shell`

### Some example to search
http://localhost:8000/blog/?name\_\_wildcard=\*f\*


### If you want to install Kibana
__to start the docker container for Kibana__

`docker run \
    --name kibana \
    --net elastic \
    -p 5601:5601 \
    docker.elastic.co/kibana/kibana:8.6.1`

__check in browser__
http://localhost:5601

## Usage
Fork and clone my repository into your system. Or simply download as zip. 

## Support
Why not take help from internet especiall from ChatGPT :)

## Roadmap
If you want to add and update more into it let me know.

## Contributing
You can contribute into it. Kindly fork and clone first. Then create your branch. Commit to your branch and push to this repo. Create a pull request. Thanks for contributing and sharing with all.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
This is an open source projects, say how it is licensed.

## Project status
I have just created it to help other junior developers. If any one want to be collaborator kindly let me know. Best regards.
