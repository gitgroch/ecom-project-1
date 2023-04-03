# Notes for Resubmission

The following updates have been made to address failings under the LO1 criteria 1.9 and 1.12

Custom Models:

- Product App & Model - Updated
    - The product model has  been updated to calculate and store review scores
    - Note that there are currently unused fields in the product model ("has_frame and has_paper"), I have left these in to use in future releases.

- Commissions App - New
    - Commissions app has been created and has a submission form and a custom model and is included in the admin panel

- Review Feature - New
    - Functionality to create and delete reviews with a rating has been implemented with a custom model in the products/models.py

- Check Out - As before
    - The checkout model has an additional notes section for delivery notes
