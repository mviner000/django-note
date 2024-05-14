import os
from django.contrib import admin
from .models import Product
from cloudinary.uploader import upload

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'barcode', 'grocery_price', 'selling_price', 'stock_quantity', 'available', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        # Get the uploaded image file from the form data
        image_file = form.cleaned_data.get('image')
        
        if image_file:
            try:
                # Get the base filename (without extension) of the uploaded image
                base_filename = os.path.splitext(image_file.name)[0]
                
                # Specify the desired folder path on Cloudinary
                folder = 'products'  # Replace 'products' with your desired folder name
                
                # Construct the public_id using folder path and base filename
                public_id = f"{folder}/{base_filename}"
                
                # Upload image to Cloudinary with specified public_id
                result = upload(image_file, public_id=public_id)
                
                # Get the secure URL of the uploaded image from Cloudinary
                image_url = result['secure_url']
                
                # Set the Cloudinary image URL in the object
                obj.image = image_url
            except Exception as e:
                # Handle upload error
                print(f"Error uploading image to Cloudinary: {str(e)}")

        # Save the model instance (Product) with the updated image URL
        super().save_model(request, obj, form, change)

# Register the Product model with the custom admin class
admin.site.register(Product, ProductAdmin)
