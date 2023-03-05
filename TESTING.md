# Testing 

Testing methodologies and results are detailed below.

## A note on Responsiveness

Bootstrap was used in this development which is a "Mobile First" approach to development, responsiveness was tested throughout development. Using a "Build, Test, Learn" approach meant that responsiveness issues were addressed as the project progressed (some of these issues can befound in the Bugs & Fixes section below.)

Once the site was completed and deployed, formal testing took place under the following conditions: 

## Hardware Testing 

- Desktop responsiveness was tested on multiple screen sizes and resolutions including:

    - 14 inch 1920 x 1080
    - 24 inch 1920 x 1080
    - 27 inch 2560 x 1440
    - 34 inch 3440 x 1440
- The Following Mobile Devices were used test layout and responsiveness:

    - Google Pixel 6 
    - Huawei P30 Pro 
    - Samsung Galaxy S20 plus

## Virtual Testing

- In addition to hardware testing, multiple templates were used to test responsiveness in Google Chrome Developers tools with the screen size template for Moto 4G being the baseline for the smallest screen size. 

## Browser Testing

The website was tested manually on the latest versions of following browsers:

- Chrome
- Edge
- Firefox
- Opera


## Testing Results
I used a manual testing method to test all functions of the app.

Steps Included:

- Creating Multiple test accounts.
- Adding multiple Items to bag with multiple sizes.
- Completing checkout process multiple times with multiple users.
- Added multiple test products using on site UI.
- Deleted multiple test producst using on site UI.

These tests were performed in both dev and production environments, results and learninfs from testing is as follows:


- All internal and external links have been tested and work as intended.
- All Images are responsive and scale to screen size.
- All navigation menus appear and operate as expected at each defined break point for media queries.
- I did not find any instance of elements such as text or images touching the side of the screen at any screen size.
- Order checkout form sends data to database.
- Product create form sends data as expected
- Product edit form sends data as expected
- Product deletion works as expected
- Account creation, login and logout all work as expected.
- Admin dashboard and functionality all work as expected.

## Lighthouse 

All pages in the deployed site were passed through Google's Lighthouse tool to test for Performance, Best Practices, Accessibility and SEO in incognito mode.

The scores from Lighthouse at time of testing were:

**Home Page**
- **Desktop**
    - 97 performance, 75 Accessibility, 100 Best Practice, 78 SEO
- **Mobile**
    - 78 performance, 81 Accessibility, 100 Best Practice, 82 SEO

**Product Page**
- **Desktop**
    - 61 performance, 75 Accessibility, 100 Best Practice, 80 SEO
- **Mobile**
    - 58 performance, 81 Accessibility, 100 Best Practice, 83 SEO

**Product Detail Page**
- **Desktop**
    - 86 performance, 66 Accessibility, 100 Best Practice, 80 SEO
- **Mobile**
    - 54 performance, 66 Accessibility, 100 Best Practice, 83 SEO

**Shopping Bag Page**
- **Desktop**
    - 83 performance, 66 Accessibility, 100 Best Practice, 80 SEO
- **Mobile**
    - 64 performance, 63 Accessibility, 100 Best Practice, 80 SEO

**Checkout Page**
- **Desktop**
    - 92 performance, 79 Accessibility, 100 Best Practice, 80 SEO
- **Mobile**
    - 72 performance, 85 Accessibility, 100 Best Practice, 83 SEO



## Validator Testing

The site files were tested with the official W3C validator for HTMl and official (Jigsaw) validator for CSS.

## Accessibility 

- I used the [Web accessibility evaluation (WAVE)](https://wave.webaim.org/) tool to check if there were any major issues with the Accessibility of website.

# Bugs and Fix Log 

There were numerous bugs discovered and fixes applied throughout development, too many to keep track of, however below I have logged some of the more complex issues I came across that took the most time find a fix for.

**Bug:** County and Categry fields noe passing to DB 

- **Fix:** Change model to include form choices rather from the form iteself

**Bug** Images not passing to DB from form

- **Fix** Add request=FILES to form views