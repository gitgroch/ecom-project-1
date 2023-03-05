<!-- Insert Mobile responsiveness picture here -->

# **TITLE**

![screenshot of homepage.](/media/documents/site_img.jpg)


## **Overview**

Geoff Rochford Photography is is a website where the photographer can show off his work and sell prints.

Target Audience:

- People who appreciate fine art photography and are willing to invest in high-quality prints.
- People who are interested in decorating their homes or offices with unique and eye-catching pieces of art.
- People who are passionate about photography and want to support the work of talented photographers.
- People who are looking for unique and personalized gifts for special occasions, such as weddings, birthdays, or holidays.
- People who enjoy exploring new places and cultures, and want to bring a piece of the world into their homes.
- People who have a specific interest in a particular style or genre of photography, such as landscapes, portraits, or abstract art.
- People who are collectors of art and want to add to their existing collections.
- People who run businesses in the hospitality or interior design industries and want to enhance their spaces with art.
- People who want to express their own creativity by incorporating art into their daily lives.
- People who want to be inspired by the beauty of the world around them and are looking for ways to bring that inspiration into their homes.

User Stories:

User stories for this project can be found on theproject board [here](https://github.com/users/gitgroch/projects/3)


The development Goals for the Website were to:

- 
The website can be accessed here: [https://ecom-proj-1.herokuapp.com/](https://ecom-proj-1.herokuapp.com/)

## **Agile Methodology**

- Agile methodolgy was used in the development of the project in the form of a Kanbanboard available [here](https://github.com/users/gitgroch/projects/3)

### **Color Schemes**

I wanted a neutral color scheme, that provided a comfortable shopping environment for shoppes. 

Using coolors.co I developed the below color scheme.

![screenshot of color scheme](/media/documents/colors.jpg)

### **Features**



## **Testing:**

The website was tested 

## **Future Enhancement**
Some nice to haves fell out of the scope of this project. This is a list of features that could be included in future updates:
- Add ability to choose paper type to product on product details page.
- Add ability to choose frame type to product on product details page.
- Add Blog for SEO purposes.
- Add a Biography page.
- Add section for discounted items and sales.


## **Deployment** 

The site was deployed to Heroku and AWS for static files, and Stripe as the payment gateway. The steps to deploy are as follows:

- Log in to ElephantSQL.com to access your dashboard and create new instance, copy database url
- Log in to Heroku and create new app
- Add the config var DATABASE_URL, and for the value, the database url
- In the CLI terminal install dj_database_url and psycopg2 and freeze requirements
- In settings.py import dj_database_url underneath the import for os
- Add database url to settings.py
- Migrate
- Loaddata from fixtures, categories first then products
- Create a superuser for the new database
- Remove database from settings.py, replace with os.environ
- Add database url to env.py
- Login int to heroku from CLI terminal
- Temporarirly disabel COLLECTSTATIC
- Add host name of heroku app to allowed hosts in settings.py
- Add and commit changes and push.
- Push to heroku using git push heroku main
- Connect Heroku to Github for automatic deploys
- Set up an S3 Bucket in AWS for static website hosting
- Set up security policy for bucket
- Create a new group
- Create a new policy for Bucket access
- Create a user in IAM to access bucket, assign policy and to bucket
- In CLI terminal install boto3 and django storages and add storages to installed apps
- Update setting files to use AWS bucket
- Update Heroku secret keys for AWS
- Add changes, commit and push and confirm static files were collected.
- Add media files to S3 folders via AWS dashboard
- Configure Stripe secret keys in Heroku Vars
- Create new webhook endpoint in Stripe dashboard for new app
- Add webhook secret key to Heroku Vars




## **Credits**

- This project relies heavily on the code from the Code Institute tutorial "Building an E-Commerce - Project - Boutique Ado", code has been altered and updated to suit the project needs.
- All images are my own 
- Footer code partially credited to MDBootstrap
