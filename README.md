# Kickstarter Projects

**Authors:** Tim Schoen & Milo Anderson
**Version:** 0.0.2

## Requirements
April 1, 2019:
- [x] Create a new Django application, including environment variables & postgres DB connection
- [x] Configure a data model based on Kaggle Kickstarter data set
- [x] Using pandas and sqlalchemy, clean & load data from CSV to postgres DB
- [x] Configure urls, views, and templates for a Projects list page
- [x] Create a series of .scss partials, and use the django-sass-processor to compile them into .css

April 2, 2019:
- [x] Implement pagination on Projects list page, including next/prev navigation
- [x] Implement caching on the backend, using django-redis and a docker volume; verify with npm loadtest