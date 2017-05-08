# Django Docker container
Python/Django Image based on Stacksmith-generated Dockerfile

# Supported tags
-   latest, 1.11-python3

# About this image
Django is already installed within the version specified by the image.
For example `1.9-python3` will contain the latest django version of `1.9.x`.

The image does export port `8000`.

It has a volume defined to generate static resources at `/var/www/static`.
The volume `/usr/django/app` can be used for live reload during development.

# How to use this image

## Basic Setup

    FROM alang/django
    ENV DJANGO_APP=demo                # will start /usr/django/app/demo/wsgi.py
    COPY django_source /usr/django/app

## Using the onbuild image

The image does assume that your build directory (directory where the Dockerfile is located) contains  the django source code. 
This directory will be copied to `/app`.
The image contains a `requirements.txt` file . All dependencies listed there will be installed.

## Executing one off commands

How to execute one off django commands like `makemigrations`:

    docker run --rm -v "src:/usr/django/app" alang/django python app/manage.py makemigrations

## Advanced Configuration

None yet.

# User Feedback

## Issues
If you have any problems with or questions about this image, please contact me through a GitHub issue.

## Contributing
You are invited to contribute new features, fixes, or updates, large or small.
Please send me a pull request.